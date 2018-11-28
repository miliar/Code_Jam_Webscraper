#pragma region Compiler stuff
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include <iostream>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <memory.h>

using namespace std;
#pragma endregion

struct Case;
vector<string>  output;
vector<Case*>   cases;
struct node
{
	string name;
	vector<node*> ing;

	int solve()
	{
		if( islower(name[0]) )
			return 0;
		if( ing.empty() )
			return 0;

		vector<int> rec(ing.size());
		int x = 0;
		for( int j = 0; j != ing.size(); ++j )
		{
			rec[j] = ing[j]->solve();
			x += (rec[j] != 0);
		}
		if( !x )
			return 1;

		sort(rec.begin(), rec.end(), greater<int>());

		int rv = 0;
		for( int j = 0; j != ing.size(); ++j )
		{
			if( !rec[j] )
				break;
			rv = max(rv, j + rec[j]);
		}
		return max(rv, 1 + x);
	}
};

struct Case
{
	Case(int id_) : id(id_) { }

	int id;
	//////////////////////////////////////////////////////////////////////////
	// Instance variables here
	int					n;
	node*				root;
	map<string,node>	all;

	//////////////////////////////////////////////////////////////////////////

	string solve()
	{
		ostringstream rv;
		rv << "Case #" << id << ": " << root->solve() << "\n";
		return rv.str();
	}
};

#pragma region Multithreading
struct CriticalSection
{
	CriticalSection()
	{ InitializeCriticalSection(&m_cs); }
	~CriticalSection()
	{ DeleteCriticalSection(&m_cs); }

	void lock()     { EnterCriticalSection(&m_cs); }
	void unlock()   { LeaveCriticalSection(&m_cs); }

	struct Lock
	{
		Lock(CriticalSection& cs) : m_cs(cs)    { m_cs.lock();  }
		~Lock()                                 { m_cs.unlock();}
		CriticalSection& m_cs;
	};

private:
	CRITICAL_SECTION m_cs;
} work_cs;

Case* more_work()
{
	Case* rv = NULL;
	CriticalSection::Lock lock(work_cs);
	if( !cases.empty() )
	{
		rv = cases.back();
		cases.pop_back();
	}
	return rv;
}

DWORD WINAPI entry_point(void*)
{
	Case* c;
	while( c = more_work() )
		output[c->id - 1] = c->solve();
	return EXIT_SUCCESS;
}

struct Threads
{
	static int const NTHREADS = 2;
	Threads()
	{
		DWORD id;
		for( int i = 0; i != NTHREADS; ++i )
			m_threads[i] = CreateThread(NULL, 0, &entry_point, NULL, CREATE_SUSPENDED, &id);
	}

	~Threads()
	{ for_each(m_threads, m_threads + NTHREADS, ::CloseHandle); }
	void start()
	{ for_each(m_threads, m_threads + NTHREADS, ::ResumeThread); }
	void wait()
	{ WaitForMultipleObjects(NTHREADS, m_threads, TRUE, INFINITE); }

private:
	HANDLE  m_threads[NTHREADS];
} threads;
#pragma endregion

int main(int argc, char const* argv[])
{
#pragma region Parse input
	int T;
	cin >> T;
	output.resize(T);
	cases.resize(T);

	for( int id = 0; id != T; ++id )
	{
		Case* c = cases[id] = new Case(id + 1);
		cin >> c->n;
		for( int i = 0; i != c->n; ++i )
		{
			string name;
			cin >> name;
			node& x = c->all[name];
			x.name = name;
			if( !i )
				c->root = &x;

			int m;
			cin >> m;
			for( int j = 0; j != m; ++j )
			{
				cin >> name;
				x.ing.push_back(&c->all[name]);
			}
		}
	}
#pragma endregion

#pragma region Solve and output solutions
	threads.start();
	threads.wait();

	copy(output.begin(), output.end(), ostream_iterator<string>(cout));
#pragma endregion

	return 0;
}

