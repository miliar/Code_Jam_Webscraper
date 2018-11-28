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
/*
vector<string> rot( const vector<string>& M, int N )
{
	vector<string> M2 = M;
	for(int y=0; y<N; ++y)
		for(int x=0; x<N; ++x)
			M2[x][N-y-1] = M[y][x];
	return M2;
}

vector<string> gra( const vector<string>& M, int N )
{
	for(int x=0; x<N; ++x)
	for(int y=0; y<N; ++y)
}
*/

bool chk( const vector<string>& M, int N, int K, char C )
{
	int dy[]={-1,-1,-1, 0, 0,+1,+1,+1};
	int dx[]={-1, 0,+1,-1,+1,-1, 0,+1};
	for(int y=0; y<N; ++y)
		for(int x=0; x<N; ++x)
			for(int i=0; i<8; ++i)
				if( 0<=y+dy[i]*(K-1) && y+dy[i]*(K-1)<N && 0<=x+dx[i]*(K-1) && x+dx[i]*(K-1)<N )
				{
					for(int k=0; k<K; ++k)
						if( M[y+dy[i]*k][x+dx[i]*k] != C )
							goto next;
					return true;
				next:;
				}
	return false;
}

void case_main( ostream& os )
{
	int N, K;
	cin >> N >> K;

	vector<string> M(N);
	for(int i=0; i<N; ++i)
		cin >> M[i];

	END_OF_INPUT_FOR_THIS_TEST_CASE();

	for(int y=0; y<N; ++y)
		fill( remove( M[y].rbegin(), M[y].rend(), '.' ), M[y].rend(), '.' );

	bool r = chk( M, N, K, 'R' );
	bool b = chk( M, N, K, 'B' );

	if(r&b) os << "Both" << endl;
	else if(r) os << "Red" << endl;
	else if(b) os << "Blue" << endl;
	else os << "Neither" << endl;
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
