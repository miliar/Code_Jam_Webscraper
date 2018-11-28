#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<sstream>
#include<set>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>



#define oo 					(int)13e7
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define fill(a,v) 				memset(a, v, sizeof a)
#define ull 					unsigned long long
#define ll 						long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb( z ) 				push_back( z )
#define gcd					__gcd
using namespace std;
#define type double
//find position of px py w.r.t to x1,y1, x2,y2
int relativeCCW(type x1, type y1,  type x2, type y2,	  type px, type py)
{
	x2 -= x1;
	y2 -= y1;
	px -= x1;
	py -= y1;
	type ccw = px * y2 - py * x2;
	if (ccw == 0) {
	    ccw = px * x2 + py * y2;
	    if (ccw > 0) {
		px -= x2;
		py -= y2;
		ccw = px * x2 + py * y2;
			if (ccw < 0) {
		    	ccw = 0;
			}
	    }
	}
	return (ccw < 0) ? -1 : ((ccw > 0) ? 1 : 0);
}

bool linesIntersect(	type x1, type y1,type x2, type y2,
									type x3, type y3,type x4, type y4 )
{
	return ((relativeCCW(x1, y1, x2, y2, x3, y3) *
		 relativeCCW(x1, y1, x2, y2, x4, y4) <= 0)
		&& (relativeCCW(x3, y3, x4, y4, x1, y1) *
		    relativeCCW(x3, y3, x4, y4, x2, y2) <= 0)) ;
}
int n, k;
int y[16][32];

bool good[1<<16];
bool adj[16][16];
int bit[1<<16];

int dp[1<<16];
int vis[1<<16], vid;

int solve( int mask )
{
	if( mask == (1<<n)-1 ) return 0;
	if( vis[mask] == vid )
	return dp[mask];
	vis[mask] = vid;
	int &d = dp[mask];
	d  = oo;
	int tmp = mask ^ ( (1<<n)-1 );
	for( int z = tmp; ;  z = tmp&(z-1) )
	{
		if( good[z] )
		{
			d = min( d, 1+solve( mask | z ) );
		}
		if( z == 0 ) break;
	}
	return d;
}

int main()
{
	for(int i=0; i < (1<<16); ++i)
	bit[i] = bit[i/2] + i%2;
	int runs;
	s( runs );
	vid=1;
	for(int C=1; C <= runs; ++C, ++vid)
	{
		cin>>n>>k;
		for(int i=0; i < n; i++)
		{
			for(int x=0; x < k; x++)
			cin>>y[i][x];
		}
		
		for(int i=0; i <n; i++)
		for(int j=i+1; j < n; j++)
		{
			int cur = 1;
			for(int x1=0; x1+1 < k; x1++)
			for(int x2=0; x2+1 < k; x2++)
			{
				
				if( linesIntersect( x1, y[i][x1], x1+1, y[i][x1+1], x2, y[j][x2], x2+1, y[j][x2+1] ) )
					cur = 0;
			}
			adj[i][j] = adj[j][i] = cur;
			
		}
		
		
		for(int i=0; i < (1<<n); i++)
		{
			if( bit[i] <= 1 )
				good[i] = 1;
			else
			{
				good[i] = 1;
				for(int j=0; j < n; j++)
				if( i & 1<< j )
				for(int k=0; k < n; k++)
				if( i & 1<< k ) 
				if( j != k )
				{
					
					if( !adj[j][k] )
					{
						
						good[i] = 0; k= j = oo;
					}
				}
			}
		}
		printf("Case #%d: %d\n", C, solve( 0 ) );
	}
	return 0;
}

