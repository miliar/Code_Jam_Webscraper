/*****************************

******************************/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
int cnt( int a )
{
	int ret  = 0;
	for(;a;a = a >> 1)
		ret += (a & 1) ;
	return ret;
}
int X[ 200 ], V[ 200 ];
int main()
{
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.ans","w",stdout);
	int tc, i, cs , n, k, b, t, j;
	cs = 1;
	cin >> tc;
	while( tc -- )
	{
		cin >> n >> k >> b >> t;
		for(i = 0; i < n ; i ++ )
			cin >> X[ i ];
		for(i = 0; i < n ; i ++ )
			cin >> V[ i ];

		bool fl[ 100 ] = {0};
		int res = 1000000;
		for(j = 0; j < n ; j ++ )
		{
			if( (i64)b - X[ j ] <=  (i64)V[ j ]  * (i64)t )
			{
				fl[ j ] = 1;
			}			
		}
		int pp = 0, qq = 0;
		int now = 0;
		for(i = n - 1;i >= 0 ; i -- )
		{
			if( fl[ i ] ){
				pp ++;
				now += qq;
				if( pp >= k ) break;
			}			
			else qq ++;
		}
		if( pp >= k ) res = now;
		if( res == 1000000 )
			printf("Case #%d: IMPOSSIBLE\n", cs ++);
		else
			printf("Case #%d: %d\n", cs ++, res );
	}

	return 0;
}