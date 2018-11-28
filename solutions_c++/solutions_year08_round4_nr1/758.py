#include <cstdio>
#include <vector>
#include <algorithm>
#define nextA(a) (a*2+1)
#define nextB(a) (a*2+2)
#define MAXN 10000+3
using namespace std;


int t[ MAXN ];
int G[ MAXN ];
int C[ MAXN ];
int A[ MAXN ][ 2 ];

int M, liscie_od;


inline int min2x(int a, int b)
{
  if( a < 0  &&  b < 0 )
		return a;
	if( a < 0  ||  b < 0 )
		return max( a, b );
	return min( a, b );
}


inline void go(int n, int g)
{
  int ng = g == 1 ? 0 : 1;
	if( A[ nextA(n) ][ g ] >= 0  &&  A[ nextB(n) ][ g ] >= 0 )
		A[ n ][ g ] = A[ nextA(n) ][ g ] + A[ nextB(n) ][ g ];
	if( A[ nextA(n) ][ ng ] >= 0  ||  A[ nextB(n) ][ ng ] >= 0 )
		A[ n ][ ng ] = min2x( A[ nextA(n) ][ ng ], A[ nextB(n) ][ ng ] );
}


void dfs(int n = 0)
{
	if( n >= M )
		return;
	
	if( C[ n ] == -1 )
	{
		A[ n ][ G[ n ] ] = 0;
		return;
	}
	
	dfs( nextA(n) );
	dfs( nextB(n) );
	
	go(n, G[ n ]);
	
	if( C[ n ] == 1 )
	{
		int p0 = A[ n ][ 0 ];
		int p1 = A[ n ][ 1 ];
		go(n, G[ n ] == 1 ? 0 : 1);
		A[ n ][ 0 ] = min2x( p0, A[ n ][ 0 ] + 1 );
		A[ n ][ 1 ] = min2x( p1, A[ n ][ 1 ] + 1 );
	}
}


int main()
{
  int ilz;
  scanf("%i", &ilz);
  for(int xz=1; xz<=ilz; xz++)
  {
    int V;
    scanf("%i%i", &M, &V);
    
		int wierz = ( M - 1 ) / 2;
		
		int x;
    for(x=0; x<wierz; x++)
			scanf("%i%i", &G[ x ], &C[ x ]);
		
		for(; x<M; x++)
		{
			scanf("%i", &G[ x ]);
			C[ x ] = -1;
		}
		
		for(int x=0; x<M; x++)
			A[ x ][ 0 ] = A[ x ][ 1 ] = -1000000000;
		
		dfs();
		
		int result = -1;
		if( V == 1  &&  A[ 0 ][ 1 ] >= 0 )
			result = A[ 0 ][ 1 ];
		else if( V == 0  &&  A[ 0 ][ 0 ] >= 0 )
			result = A[ 0 ][ 0 ];
		
		if( result == -1 )
			printf("Case #%i: IMPOSSIBLE\n", xz);
		else
			printf("Case #%i: %i\n", xz, result);
	}
  return 0;
}