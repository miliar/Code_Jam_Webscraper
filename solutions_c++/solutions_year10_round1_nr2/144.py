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

template<typename T>
struct DP2
{
	const int N1, N2;
	vector<T> data;
	DP2(int N1, int N2, const T& t = T())
		: N1(N1), N2(N2), data(N1*N2, t) { assert(data.size()*sizeof(T)<(1<<26)); }
	T& operator()(int i1, int i2)
		{ return data[ (i1*N2)+i2 ]; }
	void swap(DP2& rhs)
		{ data.swap(rhs.data); }
};

int cost(int cc, int c, int a, int D, int I, int M)
{
	// prev=cc, target=c(!=256), cur=a
	if( cc == 256 )
		return abs(a-c);

	int m = 0x7fffffff;
	{
		// delete-me case
		
		int d = abs(cc-c);
		int IC = (d/M) + (d%M ? 1 : 0);
		m = min(m, D+IC*I);
	}
	{
		// dont delete-me case
		int d = abs(cc-c);
		int IC = (d/M) + (d%M ? 1 : 0);
		if(IC>0)--IC;
		m = min(m, abs(a-c)+IC*I);
	}
	return m;
}

void case_main( ostream& os )
{
	int D, I, M, N;
	cin >> D >> I >> M >> N;
	vector<int> A(N);
	for(int i=0; i<N; ++i)
		cin >> A[i];

	END_OF_INPUT_FOR_THIS_TEST_CASE();

	DP2<int> dp(N, 257);
	for(int i=0; i<N; ++i)
		for(int c=0; c<=256; ++c)
			if( i == 0 )
			{
				if( c == 256 )
					dp(i,c) = D;
				else
					dp(i,c) = abs(A[i] - c);
			}
			else
			{
				if( c == 256 )
					dp(i,c) = dp(i-1,c) + D;
				else {
					int m = 0x7fffffff;
					if( M == 0 )
					{
						m = min(dp(i-1,256) + abs(c-A[i]), dp(i-1,c)+min(D,abs(c-A[i])));
					}
					else
					{
						for(int cc=0; cc<=256; ++cc)
							m = min(m, dp(i-1,cc) + cost(cc,c,A[i],D,I,M));
					}
					dp(i,c) = m;
				}
			}

	int answer = 0x7fffffff;
	for(int c=0; c<=256; ++c)
		answer = min(answer, dp(N-1,c));
	cout << answer << endl;
}

//-----------------------------------------------------------------------------
// >>Code Template<< (Multi-Thread Solver)

#if 0
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
