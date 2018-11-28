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


#define MAXN 810

lint vx[MAXN];
lint vy[MAXN];
int n;

void sort_it( lint v[MAXN] )
{
	sort( v+0, v+n );
}

int main()
{
	freopen( "data2.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int m, i, j;
	scanf( "%d", &m );
	for( i = 0; i < m; ++i )
	{
		scanf( "%d", &n );
		for( j = 0; j < n; ++j )
			scanf( "%I64d", &vx[j] );
		for( j = 0; j < n; ++j )
			scanf( "%I64d", &vy[j] );
		sort_it( vx );
		sort_it( vy );
		lint s = 0;
		for( j = 0; j < n; ++j )
			s += vx[j] * vy[n-1-j];
		printf( "Case #%d: %I64d\n", i + 1, s );
	}
	return 0;
}