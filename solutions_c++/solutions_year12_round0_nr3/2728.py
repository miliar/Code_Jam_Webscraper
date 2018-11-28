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

bool mark[2000001];

LL f( int x , LL l , LL h )
{
	//cout << "f  " << x << endl;
	LL ten[] = { 1, 10, 100, 1000, 10000, 100000, 1000000 };
	int r = log10((double)x) + 1;
	set < LL > s;
	s.insert(x);
	For( i , r )
	{
		LL a = x % ten[i];
		LL b = x / ten[i];
		LL n = a * ten[r-i] + b;
		if( x != n && (int)log10(n) == (int)log10(x) && l <= n && n <= h )
		{
			s.insert(n);
			mark[n] = true;
		}
	}
	// set < LL > :: iterator it;
	// for( it = s.begin() ; it != s.end() ; it ++ )
		// cout << *it << " ";
	// cout << endl << endl;
	LL ret = s.size();
	return ret * ( ret-1 ) / 2;
}

int main()
{
	int tc;
	cin >> tc;
	For( t , tc )
	{
		LL res = 0, a, b;
		cin >> a >> b;
		for( int i = a ; i <= b ; i ++ )
			if( !mark[i] )
				res += f( i , a , b );
		for( int i = a ; i <= b ; i ++ )
			mark[i] = false;
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}
