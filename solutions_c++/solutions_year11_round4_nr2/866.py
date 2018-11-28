#include <cstdio>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>
#include <cassert>

#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (decltype((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int r,c,d;
int cx,cy;
int mat[501][501];
int go(int k)
{
	For(a,0,r-k) For(b,0,c-k) {
		ll sum = 0;
		ll mx,my;
		mx=my=0;
		cx = a + a + k - 1;
		cy = b + b + k - 1;
		forn(i,k) forn(j,k)
		{
			if (i==0 && j==0 || i==0 && j == k-1 || i==k-1 && j==0 || i==k-1 && j==k-1) continue;
			int x = a + i;
			int y = b + j;
			sum += mat[x][y];
			mx += (2*x-cx)*mat[x][y];
			my += (2*y-cy)*mat[x][y];
		}
		if (mx == 0 && my == 0) return true;
		
	}
	return false;
}

int run()
{
	r=ni(), c=ni(), d=ni();

	scanf("\n");
	memset(mat,0,sizeof(mat));
	forn(i,r) {
		forn(j,c) {
			int c =  getchar()-'0';
			mat[i][j] = c;	
		}
		scanf("\n");
	}
	ford(i,min(r+1,c+1)) {
		if (go(i)) return i;
	}
	return -1;
	
}

int main()
{
	int i, j, k, t, tests;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf("%d\n", &tests);

	for (int tt=0; tt<tests; tt++) {
		int ret = run();
		if (ret < 3)
			printf("Case #%d: IMPOSSIBLE\n", tt+1);
		else
			printf("Case #%d: %d\n", tt+1, ret);

	}
	return 0;
}