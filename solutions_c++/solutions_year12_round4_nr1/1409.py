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
typedef pair<i64,i64> pii;

i64 pos[ 110 ];
i64 len[ 110 ];
i64 tot;
int v;
map< pii, bool > mp;
bool dp( i64 curVine, i64 curPos )
{
	pii pp = pii(curVine, curPos);
	if( mp.find(pp) != mp.end() ) return mp[ pp ];

	i64 rng = pos[ curVine ] - curPos;
	i64 mx = curPos +rng + rng;
	if( mx >= tot )
	{
		mp[ pp ] = true;
		return true;
	}
	int i;
	for(i = curVine + 1; i < v; i ++ )
	{
		if( pos[ i ] <= mx )
		{
			i64 nP =  max( pos[ curVine ], pos[ i ] - len[ i ] );
			i64 nV = i;
			if( dp(i,nP) ) 
			{
				mp[ pp ] = true;
				return true;			
			}
		}
	}	
	mp[ pp ] = false;
	return false;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cs = 1;
	cin >> tc;
	while( tc --)
	{
		mp.clear();
		
		printf("Case #%d: ", cs++ );

		cin >> v;
		int i;
		for(i = 0; i < v ; i ++ )
			scanf("%I64d %I64d", &pos[ i ] , & len[ i ]);

		scanf("%I64d", &tot);

		i64 curVine = 0;		
		i64 curPos = 0;

		if( dp(curVine, curPos ) )
		{
			cout <<"YES"<<endl;
		}
		else
		{
			cout <<"NO"<<endl;
		}
	}
	return 0;
}
