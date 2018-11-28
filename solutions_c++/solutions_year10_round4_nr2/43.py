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

static const int FAIL = -1;

int rec(
	map<pair<int,int>, int>& memo,
	int seen, int matchID, vector<int>& Price, vector<int>::iterator s, vector<int>::iterator e )
{
	if( s+1 == e )
		return (seen >= *s ? 0 : FAIL);

	pair<int,int> key(seen,matchID);
	if( memo.count(key) )
		return memo[key];

	int maxWantSee = *max_element(s, e);
	if( seen >= maxWantSee )
		return memo[key] = 0;

	int left  = matchID*2+2;
	int right = matchID*2+1;

	int L1 = rec(memo, seen+1, left, Price, s, s+(e-s)/2);
	int R1 = rec(memo, seen+1, right, Price, s+(e-s)/2, e);
	int L2 = rec(memo, seen, left, Price, s, s+(e-s)/2);
	int R2 = rec(memo, seen, right, Price, s+(e-s)/2, e);
	if( L1==FAIL || R1==FAIL )
		return memo[key] = FAIL;
	if( L2==FAIL || R2==FAIL )
		return memo[key] = Price[matchID]+L1+R1;
	return memo[key] = 
		min( Price[matchID]+L1+R1, L2+R2 );
}

void case_main( ostream& os )
{
	int P;
	cin >> P;

	vector<int> M(1<<P);
	for(int i=0; i<(1<<P); ++i)
		cin >> M[i];

	vector<int> Price((1<<P)-1);
	for(int i=0; i<(1<<P)-1; ++i)
		cin >> Price[i];
	reverse(Price.begin(), Price.end());

	END_OF_INPUT_FOR_THIS_TEST_CASE();

	for(int i=0; i<M.size(); ++i)
		M[i] = P - M[i];

	map<pair<int,int>, int> memo;
	cout << rec(memo, 0, 0, Price, M.begin(), M.end()) << endl;
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
