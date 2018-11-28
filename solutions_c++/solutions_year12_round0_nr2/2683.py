#include<list>
#include<set>
#include<map>
#include<ctime>
#include<stack>
#include<string>
#include<vector>
#include<cstdio>
#include<cmath>
#include<queue>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<iterator>
#include<cassert>
#include<fstream>
#include<numeric>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<algorithm>
using namespace std;
 
#define For(i,n) for( int i=0; i < n; i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define ALL(c)  c.begin() , c.end()
#define LL long long
#define SET(t,v) memset((t), (v), sizeof(t))

typedef vector < int > VI;
typedef pair< int , int > PII;
#define fr first
#define se second

#define tri pair < PII , int >
int t[110];
tri T[110];

tri f( int x )
{
	int d = x / 3;
	tri ret;
	ret.fr.fr = ret.fr.se = ret.se = x / 3;
	if( x % 3 == 1 )
		ret.se ++;
	else if( x % 3 == 2 )
		ret.se ++, ret.fr.se ++;
	return ret;
}

bool make( tri a , int p )
{
	if( a.fr.fr && max( max( a.fr.fr , a.fr.se ) , a.se ) - min( min( a.fr.fr , a.fr.se ) , a.se ) < 2 )
	{
		a.fr.se --;
		a.se ++;
		if( max( max( a.fr.fr , a.fr.se ) , a.se ) - min( min( a.fr.fr , a.fr.se ) , a.se ) == 2 )
		{
	//		cout << a.fr.fr << " " << a.fr.se << " " << a.se << endl;
			return a.se >= p;
		}
		else
			return false;
	}
	else
		return false;
}

int main()
{
	int tc, n, s, p;
	cin >> tc;
	For( i , tc )
	{
		int res = 0;
		cin >> n >> s >> p;
		For( j , n )
		{
			cin >> t[j];
			T[j] = f( t[j] );
		}
		For( j , n )
		{
			if( T[j].se >= p )
			{
	//			cout << T[j].fr.fr << " " << T[j].fr.se << " " << T[j].se << endl;
				res ++;
			}
			else
			{
				if( s &&  make( T[j] , p ) )
					s --, res ++;
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
	return 0;
}
