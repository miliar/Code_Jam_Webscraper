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
int gcd( int a, int b )
{
	if( a % b == 0 ) return b;
	return gcd(b, a % b );
}
set <int> st;
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int tc, cs = 1;
	cin >> tc;
	while( tc -- )
	{
		int a[ 4 ], b[ 5 ];
		int n, i;
		st.clear();
		cin >> n;
		for(i = 0; i < n ; i ++ ) cin >> a[ i ];
		for( i = 0; i < n ; i ++ ) st.insert( a[ i ] );
		i = 0;
		for( set<int>::iterator it = st.begin(); it != st.end(); ++it )
			a[ i++ ] = *it;
		n = st.size();
		
		a[ n ] = a[ 0 ];
		
		for(i = 0; i < n ; i ++ )
			b[ i ] = abs( a[ i ] - a[ i + 1 ] );
		int k = gcd( b[ 1 ], b[ 0 ] );
		for(i = 2; i < n ; i ++ )
			k = gcd( b[ i ], k );	
		int p = ceil((double)a[ 0 ] / k );
		printf("Case #%d: ", cs ++);
		cout << k * p - a[ 0 ] << endl;
	}
	return 0;
}