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
i64 pre[ 4000 ], tot[ 4000 ];
i64 a[ 4000 ];
i64 main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	i64 tc, r, k, n, i, j, cs = 1;
	scanf("%I64d",&tc);
	while( tc -- )
	{
		CLR( pre );
		CLR( tot );
		scanf("%I64d %I64d %I64d",&r, &k, &n);
		for(i =0; i < n ; i ++ )	scanf("%I64d",&a[ i ]);
		for(i = n ; i < 2* n ; i ++ ) a[ i ] = a [ i - n ] ;	
		for(i = 0; i < n ; i ++ )
		{
			i64 sum = 0;
			for(j = i; j < i + n ; j ++ )
			{
				sum += a[ j ];
				if( sum >  k ) break;
			}
			if( sum > k ){
				sum -= a[ j ];
				j--;
			}
			pre[ i ] = ( j + 1 ) % n;
			tot[ i ] = sum;
		}
		i64 res = 0;
		i64 init = 0;
		for(i = 0; i < r; i ++ )
		{
			res += tot[ init ];
			init = pre[ init ];
		}
		printf("Case #%I64d: %I64d\n",cs ++, res );
	}
	return 0;
}