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

char get(vector<string>& d, int y, int x)
{
	if( 0<=y && y<d.size() )
		if( 0<=x && x<d[y].size() )
			return d[y][x];
	return ' ';
}

bool canBeMadeCenter(int M, vector<string>& d, int y, int x)
{
	for(int dy=0; y+dy<M || y-dy>=0; ++dy)
		for(int dx=0; x+dx<M || x-dx>=0; ++dx)
		{
			char c1 = get(d, y+dy, x+dx);
			char c2 = get(d, y+dy, x-dx);
			char c3 = get(d, y-dy, x-dx);
			char c4 = get(d, y-dy, x+dx);
			if( (c1!=c2&&c1!=' '&&c2!=' ')
			 || (c2!=c3&&c2!=' '&&c3!=' ')
			 || (c3!=c4&&c3!=' '&&c4!=' ')
			 || (c4!=c1&&c4!=' '&&c1!=' ') )
				return false;
		}
	return true;
}

int howMany(int M, int y, int x)
{
	int c = M/2;
	int dr = abs(c-y)+abs(c-x);
	return (c+dr+1)*(c+dr+1) - (c+1)*(c+1);
}

void case_main( ostream& os )
{
	int k;
	cin >> k;
	string dummy; getline(cin,dummy);

	int M = 2*k-1;

	vector<string> d(M);
	for(int i=0; i<M; ++i) {
		getline(cin, d[i]);
		d[i].resize( M, ' ' );
	}

	END_OF_INPUT_FOR_THIS_TEST_CASE();

	int ans = 0x7fffffff;
	for(int y=0; y<M; ++y)
		for(int x=0; x<M; ++x) {
//cerr<<y<<","<<x<<" : "<<canBeMadeCenter(M, d, y, x)<<endl;
			if( canBeMadeCenter(M, d, y, x) )
				ans = min( ans, howMany(M,y,x) );
		}
	cout << ans << endl;
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
