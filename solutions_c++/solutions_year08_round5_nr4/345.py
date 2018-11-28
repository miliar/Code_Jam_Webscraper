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
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);
#define INF 1000000000

#define B 10007
int mp[200][200];
int cnt[200][200];
int m, n, k;

void read_it()
{
	memset( mp, 0, sizeof( mp ) );
	memset( cnt, 0, sizeof( cnt ) );
	cnt[1][1] = 1;
	scanf( "%d %d %d", &m, &n, &k );
	int nx, ny;
	for( int i = 0; i < k; ++i )
	{
		scanf( "%d %d", &nx, &ny );
		mp[nx][ny] = 1;
	}
}

void make_it()
{
	int i, j;
	for( i = 1; i <= m; ++i )
		for( j = 1; j <= n; ++j )
		{
			if( !mp[i+2][j+1] && cnt[i][j])
			{
				cnt[i+2][j+1] = (cnt[i+2][j+1]+cnt[i][j])%B;
			}
			if( !mp[i+1][j+2] && cnt[i][j] )
			{
				cnt[i+1][j+2] = (cnt[i+1][j+2]+cnt[i][j])%B;
			}
		}
	printf( " %d\n", cnt[m][n] );
}

int main()
{
	freopen( "data1.in", "r", stdin );
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