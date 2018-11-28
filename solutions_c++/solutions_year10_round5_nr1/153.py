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

vector<int> P;
void init_primes()
{
	static const int N = 1000000;
	vector<bool> isp(N+1, true);
	vector<int> ps;
	for(int p=2; p<=N; ++p)
		if( isp[p] ) {
			P.push_back(p);
			for(int q=p+p; q<=N; q+=p)
				isp[q] = false;
		}
}

static LL MODVAL;

LL ADD(LL x, LL y) { return (x+y)%MODVAL; }
LL SUB(LL x, LL y) { return (x-y+MODVAL)%MODVAL; }
LL MUL(LL x, LL y) { return (x*y)%MODVAL; }
LL POW(LL x, LL e) {
	LL v = 1;
	for(;e;x=MUL(x,x),e>>=1)
		if(e&1)
			v = MUL(v, x);
	return v;
}
LL DIV(LL x, LL y) { return MUL(x, POW(y, MODVAL-2)); }

bool try_solve(vector<int>& S, LL P, int* pNext)
{
	if( S.size() <= 1 )
		return false; // cannot determine
	if( S[0] == S[1] ) {
		*pNext = (int) S[0];
		return true; // constant number generator
	}

	// a S[0] + b = S[1] mod P
	// a S[1] + b = S[2] mod P
	// ...
	// a S[n-1]+b = next!

	MODVAL = P;
	LL A = DIV(SUB(S[2], S[1]), SUB(S[1], S[0]));
	LL B = SUB(S[1], MUL(A, S[0]));

	for(int i=0; i+1<S.size(); ++i)
		if( ADD(MUL(A,S[i]),B) != S[i+1] )
			return false; // inconsistent

	*pNext = ADD(MUL(A,S.back()),B);
	return true;
}

void case_main( ostream& os )
{
	int D, K;
	cin >> D >> K;
	vector<int> S(K);
	for(int i=0; i<K; ++i)
		cin >> S[i];

	END_OF_INPUT_FOR_THIS_TEST_CASE();

	int tenD = 1;
	for(int i=0; i<D; ++i) tenD *= 10;

	int Smax = *max_element(S.begin(), S.end());

	bool found = false;
	int theFound;
	for(int i=0; i<P.size() && P[i]<=tenD; ++i)
	{
		int next;
		if( Smax<P[i] && try_solve(S, P[i], &next) ) {
			if( found ) {
				if( theFound != next ) {
					cout << "I don't know." << endl;
					return;
				}
			}
			found = true;
			theFound = next;
		}
	}
	if( found )
		cout << theFound << endl;
	else
		cout << "I don't know." << endl;//assert(false);
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
	init_primes();

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
