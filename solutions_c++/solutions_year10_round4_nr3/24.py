#include <algorithm>
#include <memory.h>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
typedef pair<int,int> pii;
typedef long long ll;

vector<int> g[1010];
int X1[1010], Y1[1010], X2[1010], Y2[1010], n, u[1010];
vector<int> nn;
int maxx, maxy;

void dfs( int i, int qq )
{
	u[i] = qq;
	nn.push_back( i );
	
	if ( X2[i] > maxx ) maxx = X2[i];
	if ( Y2[i] > maxy ) maxy = Y2[i];
	
	forn( j, g[i].size() )
		if ( u[ g[i][j] ] < qq )
			dfs( g[i][j], qq );
}

bool isect( int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2 )
{
	int lx = max( ax1, bx1 );
	int rx = min( ax2, bx2 );
	int ly = max( ay1, by1 );
	int ry = min( ay2, by2 );
	
	return lx <= rx && ly <= ry;
}

bool intersect( int i, int j )
{
	return isect( X1[i]-1, Y1[i], X2[i], Y2[i], X1[j]-1, Y1[j], X2[j], Y2[j] ) ||
		   isect( X1[i]-1, Y1[i], X2[i], Y2[i], X1[j], Y1[j]-1, X2[j], Y2[j] ) ||
		   isect( X1[i], Y1[i]-1, X2[i], Y2[i], X1[j]-1, Y1[j], X2[j], Y2[j] ) ||
		   isect( X1[i], Y1[i]-1, X2[i], Y2[i], X1[j], Y1[j]-1, X2[j], Y2[j] );
}

int main()
{
	int tc;
	scanf( "%d", &tc );
	for ( int q=1; q<=tc; q++ )
	{
		scanf( "%d", &n );
		forn( i,n ) scanf( "%d %d %d %d", &X1[i], &Y1[i], &X2[i], &Y2[i] );
		
		forn( i,n ) g[i].clear();
		
		forn( i,n )
			forn( j,i )
			{
				bool ok = intersect( i, j ) || intersect( j, i );
				if ( ok )
				{
					g[i].push_back( j );
					g[j].push_back( i );
					//printf( "%d - %d\n", i, j );
				}
			}
			
		int ans = 0;
		forn( i,n )	if ( u[i] < q )
		{
			nn.clear();
			maxx = maxy = -100000000;
			dfs( i, q );
			forn( i, nn.size() )
			{
				int z = maxx - X1[nn[i]] + maxy - Y1[nn[i]] + 1;
				if ( z > ans ) ans = z;
			}
		}
		
		printf( "Case #%d: %d\n", q, ans );
	}
}
