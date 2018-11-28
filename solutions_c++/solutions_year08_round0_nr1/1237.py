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
#define mp make_pair
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);
#define INF 1000000000

#define MAXN 110
#define MAXM 1010
#define MAXS 110

char a[MAXN][MAXS];
char b[MAXM][MAXS];
bool sam[MAXM][MAXN];
int nowmin[MAXM][MAXN];
int n, m;
FILE *fin;

void read_it()
{
	int i, j;
	scanf( "%d", &n );
	getchar();
	for( i = 0; i < n; ++i )
		gets( a[i] );
	scanf( "%d", &m );
	getchar();
	for( i = 0; i < m; ++i )
		gets( b[i] );
	for( i = 0; i < m; ++i )
		for( j = 0; j < n; ++j )
			if( strcmp( b[i], a[j] ) == 0 )
				sam[i][j] = true;
			else
				sam[i][j] = false;
}

void make_it()
{
	memset( nowmin, 0, sizeof( nowmin ) );
	int i, j, k;
	for( i = 0; i < m; ++i )
		for( j = 0; j < n; ++j )
		{
			if( sam[i][j] )
				nowmin[i][j] = INF;
			else if( i == 0 )
				nowmin[i][j] = 0;
			else
			{
				nowmin[i][j] = INF;
				for( k = 0; k < n; ++k )
					if( nowmin[i-1][k] != INF )
					{
						if( k == j && nowmin[i-1][k] < nowmin[i][j] )
							nowmin[i][j] = nowmin[i-1][k];
						else if( k !=j && nowmin[i-1][k] + 1 < nowmin[i][j] )
							nowmin[i][j] = nowmin[i-1][k] + 1;
					}
			}
		}
	int ans = INF;
	for(  i = 0; i < n; ++i )
		if( nowmin[m-1][i] < ans )
			ans = nowmin[m-1][i];
	printf( "%d\n", ans );
}

int main()
{
	freopen( "data3.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int p;
	scanf( "%d", &p );
	for( int i = 1; i <= p; ++i )
	{
		printf( "Case #%d: ", i );
		read_it();
		make_it();
	}
	return 0;
}