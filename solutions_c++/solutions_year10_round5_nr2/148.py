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

static const LL INF = 0x3fffffffffffffffLL;

LL solve(LL target, vector<LL>& B)
{
	if( target >= 50000 )
		return -2;

	vector<LL> dp(target+1, INF);
	dp[0] = 0;
	for(int i=0; i<dp.size(); ++i) {
		for(int j=0; j<B.size(); ++j)
			if( B[j] <= i )
				dp[i] = min(dp[i], dp[i-B[j]]+1);
	}

	if( INF > dp[target] )
		return dp[target];
	else
		return -1;
}

void case_main( ostream& os )
{
	LL L;
	cin >> L;
	int N;
	cin >> N;
	vector<LL> B(N);
	for(int i=0; i<N; ++i)
		cin >> B[i];

	END_OF_INPUT_FOR_THIS_TEST_CASE();

	sort(B.begin(), B.end());

	LL last = B.back();
	B.pop_back();

	LL rem = L%last;
	LL div = L/last;

	if( rem==0 )
		cout << div << endl;
	else {
		LL m = INF;
		for(int i=0; i<=div; ++i)
		{
			LL ans = solve(rem+last*i, B);
			if( ans >= 0 )
				m = min(m, ans+(div-i));
			if( ans == -2 )
				break;
		}
		if( m==INF )
			cout << "IMPOSSIBLE" << endl;
		else
			cout << m << endl;
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
