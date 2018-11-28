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

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.ans","w",stdout);
	int t, j, mp[ 500 ] = { 0 }, n, cs = 1;
	mp[ 'B' ] = 1, mp[ 'O' ] = 2;
	cin >> t;
	while ( t -- )
	{		
		string ss;
		cin >> n;
		int i, btn, init[ 3 ] = { 0, 1, 1 }, res = 0, spare[ 3 ] = { 0 };
		for(i = 0; i < n ; i ++ )
		{
			cin >> ss >> btn;
			int nn =  mp[ ss[ 0 ] ];

			int lagbe = abs(btn - init[ nn ]) + 1;

			if( lagbe > spare[ nn ] )
				res += lagbe - spare[ nn ], spare[ 3 - nn ] += lagbe - spare[ nn ];
			else
				res += 1, spare[ 3 - nn ] += 1;
			spare[ nn ] = 0;
			init[ nn ] = btn;
		}
		printf("Case #%d: %d\n", cs ++, res);
	}
	return 0;
}