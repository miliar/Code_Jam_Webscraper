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
double D;
vector < int > res;
bool pos( double tm )
{
	double pos = res[ 0 ] - tm;
	int i;
	for(i = 1; i < res.size(); i ++ )
	{
		double tar = pos + D;
		if(tar < res[ i ] || fabs( tar - res[ i ] ) < eps)
		{			
			double pare = res[ i ] - tm;
			if( pare < tar || fabs( pare - tar ) < eps ) pos = tar;
			else pos = pare;
		}
		else
		{
			double pare = res[ i ] + tm;
			if( pare > tar || fabs( pare - tar ) < eps ) pos = tar;
			else return false;
		}
	}
	return true;

}
int main(){
	
	freopen("aa.txt","r",stdin);
	freopen("A-large.ans","w",stdout);

	int tc, cs = 1;
	cin >> tc;
	while( tc -- )
	{
		res.clear();
		int C, p, v, i;
		cin >> C;
		cin >> D;
		while( C -- )
		{
			cin >> p >> v;
			for(i = 0; i < v; i ++ ) res.push_back( p );
		}
		double lo = 0, hi = 1e14, mid;
		int cnt = 500;
		while( cnt -- )
		{
			mid = ( lo + hi ) / 2;
			if( pos ( mid ) ) hi = mid;
			else lo = mid;
		}
		printf("Case #%d: %.9lf\n", cs ++, mid );


	}
	return 0;
}