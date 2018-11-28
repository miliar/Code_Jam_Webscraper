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

int h, w;
int a[102][102];

/*
struct point
{
	int x, y;
	void put( int X, int Y )
	{
		x=X; y=Y;
	}
	point(){}
	point( int X, int Y )
	{
		put( X, Y );
	}	
	bool operator < ( const point& p ) const
	{
		if( x == p.x )
				return y < p.y;
		return x > p.x;
	}
};*/
#define mp make_pair
#define x first
#define y second
typedef pair<int,int> point;
point dp[102][102];
int visd[102][102], vid;
int dx[] = { -1, 0 , 0 , 1 };
int dy[] = {  0, -1, 1, 0 };
point reaches( int x, int y )
{
	
	int& v = visd[x][y];
	point& d = dp[x][y];
	if( v == vid )
		return d;
	v = vid;
	int nx = -1, ny = -1;
	for(int D=0; D < 4; D++)
	{
		int X = x+dx[D], Y = y+dy[D];
		if( X < 0 || Y < 0 || X >= h || Y >= w )
			continue;
		
		if( a[X][Y] >= a[x][y] )
			continue;
		
		if( nx==-1 && ny==-1 )
			nx = X, ny = Y;
		else
		{
			if( a[nx][ny] > a[X][Y] )
				nx=X, ny=Y;	
		}
		
	}
	if( nx==-1 && ny==-1)
		d = mp( x, y );
	else
		d = reaches( nx, ny );
	return d;
}

int main()
{
	int t;
	s( t );
	for(int c=1; c <= t; c++)
	{
		++vid;
		printf("Case #%d:\n", c );
		s( h ); s ( w );
		for(int i=0; i < h; i++)
		for(int j=0; j < w; j++)
		s( a[i][j] );
		
		map< point, point > comps;
		set< point > sinks;
		map< point, char > p2c;
		for(int i=0; i < h; i++)
		for(int j=0; j < w; j++)
		{
			point ret = reaches( i, j );
			sinks.insert( ret  );
			if( comps.count( ret ) == 0 )
				comps[ ret ] = point(i,j);
			else
			{
				comps[ret] = min( comps[ret], point(i,j) );
			}
		}
		
		set< point > zxx;
		for(  set< point > :: iterator z = sinks.begin(); z != sinks.end(); z++)
		{
			
			zxx.insert( comps[*z] );
			
		}
		char chr='a';
		for(  set< point > :: iterator z = zxx.begin(); z != zxx.end(); z++, chr++)
		{
			p2c[ *z ] = chr;
		}
		for(int i=0; i < h; i++)
		for(int j=0; j < w; j++)
		{
			point ret = reaches( i, j );
			printf("%c%c", p2c[ comps[ret] ], j==w-1?'\n':' ');
		}
		
	}
}

