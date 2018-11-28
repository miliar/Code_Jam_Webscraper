//-----------------------------------------------------------------------------
// >>Code Template<< (for Visual C++)

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <complex>
#include <functional>
#include <queue>
#include <stack>
#include <cmath>
#include <cassert>
#include <cstring>
#define  cout os
using namespace std;
typedef long long LL;
typedef complex<double> CMP;
void END_OF_INPUT_FOR_THIS_TEST_CASE(); // stub for multi-threading

//-----------------------------------------------------------------------------
// >>Main<<

int next_combination(int p)
{
	int lsb = p & -p;
	int rem = p + lsb;
	int rit = rem & ~p;
	return rem|(((rit/lsb)>>1)-1);
}

// Is it possible to cover the goal by at most k elements from mask?
// Assumption:  goal \subseteq \bigcup mask

bool canCover( int goal, set<int>& mask, int k )
{
	// exhaustive search
	vector<int> ms(mask.begin(), mask.end());
	for(int i=(1<<k)-1; i<(1<<ms.size()); i=next_combination(i))
	{
		int gg = goal;
		for(int j=0; (1<<j)<=i; ++j)
			if( i & (1<<j) )
				gg &= ~ms[j];
		if( gg == 0 )
			return true;
	}
	return false;
}

bool do_cross( vector<int>& p, vector<int>& q )
{
	for(int i=0; i+1<p.size(); ++i)
		if( p[i]==q[i] || p[i+1]==q[i+1] || (p[i]<q[i])!=(p[i+1]<q[i+1]) )
			return true;
	return false;
}

void case_main( ostream& os )
{
	int N, K; cin >> N >> K;
	vector< vector<int> > P(N, vector<int>(K));
	for(int i=0; i<N; ++i)
		for(int j=0; j<K; ++j)
			cin >> P[i][j];
	vector< vector<bool> > cross(N, vector<bool>(N));
	for(int i=0; i<N; ++i)
		for(int j=0; j<N; ++j)
			cross[i][j] = do_cross(P[i], P[j]);


	END_OF_INPUT_FOR_THIS_TEST_CASE();


	set<int> mask;
	for(int m=1; m<(1<<N); ++m)
	{
		for(int i=0;   i<N; ++i) if((1<<i)&m)
		for(int j=i+1; j<N; ++j) if((1<<j)&m)
			if( cross[i][j] )
				goto next;
		mask.insert(m);
	next:;
	}

	for(set<int>::iterator it=mask.begin(); it!=mask.end(); )
	{
		for(int k=0; k<N; ++k)
			if( (*it|(1<<k))!=*it && mask.count(*it|(1<<k)) )
				{mask.erase(it++); goto next2;}
		++it;
	next2:;
	}

	typedef int STATE;
	const int goal = (1<<N) - 1;

	vector<STATE> Q( 1, 0 );
	vector<bool> visited( 1<<N, false );

	for(int step=0 ;; ++step)
	{
		vector<STATE> Q2;
		for(int i=0; i<Q.size(); ++i)
		{
			STATE& s = Q[i];
			if( s == goal ) {
				os << step << endl; // found the answer
				return;
			}

			for(set<int>::iterator it=mask.begin(); it!=mask.end(); ++it)
			{
				STATE t = s | *it;
				if( !visited[t] ) {
					visited[t] = true;
					Q2.push_back(t);
				}
			}
		}
		Q.swap(Q2);
	}
}

//-----------------------------------------------------------------------------
// >>Code Template<< (Multi-Thread Solver)

#if 1
#undef cout
#include <windows.h>
#include <process.h>

static const int THREAD_NUM = 2;
volatile int     g_id;
int              g_nCase;
CRITICAL_SECTION g_cs;
vector<string>   g_output;

unsigned __stdcall thread_main( void* t_id ) {
	for(;;) {
		EnterCriticalSection(&g_cs);
		const int id = ++g_id;
		if(id>g_nCase) { LeaveCriticalSection(&g_cs); break; }
		cerr << setw(4) << id << " @ " << (int)t_id << " start" << endl;

		ostringstream ss;
		ss << "Case #" << id << ": ";
		case_main( ss );

		EnterCriticalSection(&g_cs);
		if(g_output.size()<id) g_output.resize(id);
		g_output[id-1] = ss.str();
		cerr << setw(4) << id << " @ " << (int)t_id << " end" << endl;
		LeaveCriticalSection(&g_cs);
	}
	return 0;
}

void END_OF_INPUT_FOR_THIS_TEST_CASE() { LeaveCriticalSection(&g_cs); }

int main() {
	cin >> g_nCase;
	string dummy; getline(cin, dummy);

	InitializeCriticalSection(&g_cs);
	vector<HANDLE> thread;
	for(int i=0; i<THREAD_NUM; ++i)
		thread.push_back( (HANDLE)_beginthreadex(0, 0, &thread_main, (void*)i, 0, 0) );
	WaitForMultipleObjects( thread.size(), &thread[0], TRUE, INFINITE );
	DeleteCriticalSection(&g_cs);

	copy( g_output.begin(), g_output.end(), ostream_iterator<string>(cout) );
}

//-----------------------------------------------------------------------------
// >>Code Template<< (Single-Thread Solver)

#else
#undef cout
void END_OF_INPUT_FOR_THIS_TEST_CASE() {}
int main() {
	int nCase; cin >> nCase;
	string dummy; getline(cin, dummy);

	for(int id=1; id<=nCase; ++id) {
		cout << "Case #" << id << ": ";
		case_main( cout );
	}
}
#endif
