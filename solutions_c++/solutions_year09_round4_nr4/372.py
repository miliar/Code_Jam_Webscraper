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

double minRad(double x, double y, double r, double X, double Y, double R)
{
	return (sqrt((x-X)*(x-X) + (y-Y)*(y-Y)) + r + R) / 2;
}

void case_main( ostream& os )
{
	int N; cin >> N;
	vector<double> X(N), Y(N), R(N);
	for(int i=0; i<N; ++i) cin >> X[i] >> Y[i] >> R[i];

	END_OF_INPUT_FOR_THIS_TEST_CASE();

	os << setiosflags(ios::fixed) << setprecision(9);

	if( N == 1 )
	{
		os << R[0] << endl;
	}
	else if( N == 2 )
	{
		os << max(R[0], R[1]) << endl;
	}
	else
	{
		assert( N == 3 );
		double a = max(R[0], minRad(X[1],Y[1],R[1],  X[2],Y[2],R[2]));
		double b = max(R[1], minRad(X[2],Y[2],R[2],  X[0],Y[0],R[0]));
		double c = max(R[2], minRad(X[0],Y[0],R[0],  X[1],Y[1],R[1]));
		os << min(a, min(b, c)) << endl;
	}
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
