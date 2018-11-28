#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long lint;

#define mp make_pair
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);
#define INF 1000000000

int nx, ny, a;

void read_it()
{
	scanf( "%d %d %d", &nx, &ny, &a );
}

void make_it()
{
	for( int x = 0; x <= nx; ++x )
		for( int y = 0; y <= ny; ++y )
			for( int dx = -x; dx <= nx-x; ++dx )
			{
				if( x + y == 0 )
					continue;
				int dy = -1;
				if( x == 0 )
				{
					if( y * dx == a )
						dy = 0;
				}
				else
				{
					if( (a - x * y - y * dx) % x == 0 )
						dy = (a-x*y-y*dx) / x;
				}
				if( dy != -1 && dy >= -y && dy <= ny-y )
				{
					printf( " %d %d %d %d %d %d\n", x, 0, 0, y, x + dx, y + dy );
					return;
				}
			}
	printf( " IMPOSSIBLE\n" );
}

int main()
{
	freopen( "data4.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int c;
	scanf( "%d", &c );
	for( int i = 0; i < c; ++i )
	{
		printf( "Case #%d:", i + 1 );
		read_it();
		make_it();
	}
	return 0;
}