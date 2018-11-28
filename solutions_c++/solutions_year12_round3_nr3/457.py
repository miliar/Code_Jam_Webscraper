#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define inf (1<<29)
#define eps (1e-9)
#define pb push_back
#define all(a) a.begin(),a.end()
#define myabs(a) ((a)<0?(-(a)):(a))
#define i64 __int64
typedef pair<int,int> pii;

int N, M;
int toyN[ 5 ], toyT[ 5 ];
int boxN[ 500 ], boxT[ 500 ];
int GT = 0;

void dfs( int idx, int prev, int cnt )
{
	if( idx == N )
	{
		GT = GT > cnt ? GT : cnt;
		return;
	}
	int i;
	int tmp = toyN[ idx ];
	dfs(idx + 1, prev, cnt );
	for(i = prev + 1; i < M ; i ++ )
	{
		if( boxT[ i ] == toyT[ idx ] )
		{
			int kk = min(  boxN[ i ], tmp );
			cnt += kk;
			tmp -= kk;

			boxN[ i ] -= kk;
			dfs( idx + 1, i - 1, cnt );
			boxN[ i ] += kk;
		}
		dfs( idx + 1, i, cnt );
	}
}
int main()
{
	freopen("E:\\test.txt","r",stdin);
	freopen("E:\\output.txt","r",stdout);
	int T, cs = 1;
	cin >> T;
	while( T -- )
	{
		CLR( toyN );
		CLR( toyT );
		CLR( boxN );
		CLR( boxT );

		cin >> N >> M;
		int i;
		for(i = 0; i < N ; i ++ ) cin >> toyN[ i ] >> toyT[ i ];
		for(i = 0; i < M ; i ++ ) cin >> boxN[ i ] >> boxT[ i ];

		GT = 0;
		dfs(0,-1, 0);

		printf("Case #%d: %d\n", cs++, GT);
	}
	return 0;
}
