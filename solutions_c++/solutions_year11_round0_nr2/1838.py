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

int opos[ 200 ][ 200 ];
map<string, char> combo;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.ans","w",stdout);
	int tc, cs = 1;
	cin >> tc;
	while( tc -- )
	{
		CLR( opos );
		combo.clear();
		int c, d, n;
		cin >> c;
		int i;
		string s;
		for(i = 0; i < c; i ++ )
		{
			cin >> s;
			string n1, n2;
			n1 += s[ 0 ], n1 += s[ 1 ];
			n2 += s[ 1 ], n2 += s[ 0 ];
			combo[ n1 ] = s[ 2 ];
			combo[ n2 ] = s[ 2 ];
		}
		cin >> d;
		for(i = 0; i < d; i ++ )
		{
			cin >> s;
			opos[s[ 0 ]][ s[ 1 ] ] = 1;
			opos[s[ 1 ]][ s[ 0 ] ] = 1;
		}
		cin >> i;
		string res = "";

		cin >> s;
		int j;
		for(i = 0; i < s.size() ; i ++ )
		{
			bool fl = 0;
			if( res.size() )
			{
				char now;
				now = res[ res.size() - 1 ];
				string tmp;
				tmp += now;
				tmp += s[ i ];
				if( combo.find( tmp ) == combo.end() );
				else{
					res = res.substr( 0, res.size() - 1 );
					res += combo[ tmp ];
					fl = 1;
				}
			}
			if( fl == 0 ){

				for(j = 0; j < res.size(); j ++ )
					if( opos[ s[ i ] ][ res[ j] ] == 1 )
					{
						res = "";
						fl = 1;
						break;
					}
			}
			if( fl == 0 ) res += s[ i ];
		}
		printf("Case #%d: [", cs ++);
		for(i = 0; i < res.size(); i ++ )
		{
			if( i ) cout <<", ";
			cout << res[ i ];
		}
		cout <<"]"<<endl;


	}
	return 0;
}