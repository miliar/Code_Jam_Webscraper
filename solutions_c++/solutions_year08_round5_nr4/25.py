#include <cstdio>

#include <algorithm>

using namespace std;

typedef long long llint;

const int mod = 10007, pp = 1, qq = 2;

int H, W, n;
int x[ 10 ], y[ 10 ];

// Standard Template Made By LeiTao

__int64 p[1000];
__int64 PRIME,jc[20000];

__int64 getgcd(__int64 a,__int64 b,__int64&x,__int64&y)
{
if (b==0) {
x=1;
y=0;
return a;
} else {
__int64 x2,y2,z;
z=getgcd(b,a%b,x2,y2);
x=y2;
y=x2-y2*(a/b);
return z;
}
}

__int64 calc_c(int x,int y)
{
__int64 a=(jc[y]*jc[x-y])%mod;
__int64 b=mod,c=jc[x];
__int64 xx,yy;
getgcd(a,b,xx,yy);
return ((xx*c)%mod+mod)%mod;
}

__int64 mygetc(int l,__int64 x,__int64 y)
{
// printf("mygetc: %d %I64d %I64d\n",l,x,y);
if (l==1)
//return c[x][y];
return calc_c(x,y);
__int64 u=x/p[l-1];
__int64 xx=x%p[l-1];
__int64 yy=y%p[l-1];
if (yy>xx) return 0;
__int64 v=y/p[l-1];
return (mygetc(1,u,v)*mygetc(l-1,xx,yy))%mod;
}

__int64 getmodo(__int64 i,__int64 j)
{
	if( i == 0 && j == 0 ) return 1;

// printf("getmodo: %I64d %I64d\n",i,j);
int k=1;
while (p[k]<=i) ++k;

return mygetc(k,i,j);
}

// End of Standard Template

void solve_it( int n, int m, int &x, int &y )
{
	int t = n * qq - m * pp;
	if( t % (qq * qq - pp * pp) != 0 ) {
		x = y = -1;
		return;
	}
	y = t / (qq * qq - pp * pp);
	if( (n - y * qq) % pp != 0 ) {
		x = y = -1; 
		return;
	}
	x = (n - y * qq) / pp;
}

int solve( int state )
{
	int nBlock = 0;
	int BlockX[ 12 ], BlockY[ 12 ];
	int A[ 12 ], B[ 12 ];

	BlockX[ nBlock ] = 1, BlockY[ nBlock ] = 1, ++nBlock;
	for( int i = 0; i < n; ++i )
		if( (state>>i) & 1 ) BlockX[ nBlock ] = x[i], BlockY[ nBlock ] = y[i], ++nBlock;
	BlockX[ nBlock ] = H, BlockY[ nBlock ] = W, ++nBlock;

	for( int i = 1; i < nBlock; ++i ) {
		if( BlockX[i-1] > BlockX[i] || BlockY[i-1] > BlockY[i] ) return 0;
		solve_it( BlockX[i]-BlockX[i-1], BlockY[i]-BlockY[i-1], A[i], B[i] );
		if( A[i] < 0 || B[i] < 0 ) return 0;
	}

	int r = 1;
	for( int i = 1; i < nBlock; ++i ) {
		r = r * getmodo( A[i]+B[i], A[i] );
		r %= mod;
	}

	return r;
}

int main( void )
{
	freopen( "D-large.in", "r", stdin );
	freopen( "D-large.out", "w", stdout );

	int T; scanf( "%d", &T );

	*p = 1;
	for( int i = 1; ; ++i ) {
		p[i] = p[i-1] * mod;
		if( p[i] > 200000000 ) break;
	}

	*jc = 1;
	for( int i = 1; i < mod; ++i )
		jc[i] = (jc[i-1] * i) % mod;

	for( int counter = 0; counter < T; ++counter ) {
		scanf( "%d %d %d", &H, &W, &n );
		for( int i = 0; i < n; ++i )
			scanf( "%d %d", x + i, y + i );

		for( int i = 0; i < n; ++i )
			for( int j = i+1; j < n; ++j )
				if( x[i] > x[j] || x[i] == x[j] && y[i] > y[j] ) {
					swap( x[i], x[j] );
					swap( y[i], y[j] );
				}

		int sum = 0;

		for( int state = 0; state < ( 1<<n ); ++state ) {
			int r = solve( state );
            int cnt = 0;

            for( int i = 0; i < n; ++i )
            	if( (state>>i)&1 ) ++cnt;

			if( cnt%2 == 0 ) sum = ( sum + r ) % mod;
			else sum = ( ( sum - r ) % mod + mod ) % mod;
		}

		printf( "Case #%d: %d\n", counter + 1, sum );
	}

//	printf( "%I64d\n", getmodo( 100000000, 99999999 ) );

	return 0;
}

