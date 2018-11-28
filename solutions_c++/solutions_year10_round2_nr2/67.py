#include <cstdio>
#include <iostream>
#include <memory.h>
#include <vector>
#include <ctime>
#include <string>
#include <algorithm>
#include <cstring>
#include <utility>
#include <map>
#include <set>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
typedef pair<int,int> pii;
typedef long long ll;

int n, k, b, T, x[100], v[100], tt[110];

int main()
{
	int t;
	scanf( "%d", &t );
	for ( int q=1; q<=t; q++ )
	{
		scanf( "%d %d %d %d", &n, &k, &b, &T );
		forn( i,n ) scanf( "%d", &x[i] );
		forn( i,n ) scanf( "%d", &v[i] );
		
		forn( i,n ) tt[i] = ( b-x[i] )/v[i] + ( (( b-x[i] )%v[i]) != 0 );
		
		int ans = 0;
		int cur = 0;
		for ( int i=n-1; i>=0; i-- )
			if ( tt[i] > T ) cur++;
			else 
			{
				ans += cur;
				k--;
				//printf( "-> %d, tt[i], %d\n", i, k );
				if ( k == 0 ) break;
			}
		
		if ( k > 0 ) printf( "Case #%d: IMPOSSIBLE\n", q );
		else printf( "Case #%d: %d\n", q, ans );
	}
	return 0;
}
