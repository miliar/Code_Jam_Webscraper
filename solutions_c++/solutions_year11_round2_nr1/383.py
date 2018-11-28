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
#pragma comment(linker,"/STACK:16777216")
#pragma warning(disable:4786)

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

#define FOR(i,n) for( i = 0 ; i<(n) ; i++)
#define RFOR(i,a,b)  for( i = (a) ; i<(b) ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))

#define all(a) a.begin(),a.end()
#define pb push_back

#define i64 long long
#define pi (2.0*acos(0.0))
#define eps (1e-9)

typedef pair< int , int >  pii;
double  rpi[ 200 ], owp[ 200 ], oowp[ 200 ];
int wp[ 200 ], tot[ 200 ];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.ans","w",stdout);
	int tc, cs = 1, i, j;
	cin >> tc;
	while( tc -- )
	{
		CLR( tot );
		CLR( wp );
		vector<string> res;
		string s;
		int n;
		cin >> n;
		for(i = 0; i < n ; i ++ )
		{
			cin >> s;
			res.push_back( s );
		}
		for(i = 0; i < n ; i ++ )
			for(j = 0; j < n; j ++ )
				if( res[ i ][ j ] == '1' ) wp[ i ] ++, tot[ i ] ++;
				else if( res[ i ][ j ] == '0' ) tot[ i ] ++;
		for(i = 0; i < n ; i ++ )
		{
			double ss = 0, cnt = 0;
			for(j = 0; j < n ; j ++ ) 
				if( res[ i ][ j ] != '.' ) 
				{
					ss += (wp[ j ] - res[ j ][ i ] + '0') / (double)(tot[ j ] - 1), cnt ++;
				}
			//ss -= res[ i ][ j ] -'0';
			//cnt --;
			owp[ i ] = ( ss / cnt );
		}
		for(i = 0; i < n ; i ++ )
		{
			double ss = 0, cnt = 0;
			for(j = 0; j < n ; j ++ ) if( res[ i ][ j ] != '.' ) ss += (owp[ j ]), cnt ++;
			oowp[ i ] = ( ss / cnt );
		}
		printf("Case #%d:\n", cs ++ );
		for(i = 0; i < n ; i ++ )
		{

			rpi[ i ] = .25 * wp[ i ] / tot[ i ] + .5 * owp[ i ] + .25 * oowp[ i ];
			printf("%.9lf\n", rpi[ i ] );			
		}

	}

	return 0;
}