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
int min( int a, int b ){ return a < b ? a : b; }
int a[ 2000 ], b [ 2000 ];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.ans","w",stdout);
	int tc, p, i, cs = 1;
	cin >> tc;
	while( tc -- )
	{
		cin >> p;
		for(i = 0; i < ( 1<< p ) ; i ++ )	cin >> a[ i ];
		int t = 0;
		while( p  )
		{

			for(i = 0; i < ( 1<< (p-1) ) ; i ++ ) cin >> b[ i ];
			int j = 0;
			for(i = 0; i < 1 << p ; i += 2 )
			{
				if( a[ i ] == 0 || a[ i + 1 ] == 0 )
					a[ i ] = 0, t ++;
				else
					a[ i ] = min( a[ i ] - 1, a[ i + 1 ] - 1 );
				b[ j ++ ] = a[ i ];
			}
			for(i = 0; i < ( 1 << ( p - 1 ) ) ; i ++ )
				a[ i ] = b[ i ];
			p --;
		}
		printf("Case #%d: %d\n",cs ++, t );
	}
	return 0;
}