#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <sstream>
#include <deque>
#include <iostream>

using namespace std;

#define fo(a,b,c) for(a=(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define all(a) (a).begin(),(a).end( )
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back
#define __(a) memset((a),0,sizeof(a))
#define _(a,b) memset((a),(b),sizeof(a))

int n;

int main( )
{
	int i, j, k;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t, tn;
	scanf( "%d", &tn );
	fr( t, tn )
	{
		printf( "Case #%d: ", t + 1 );
		scanf( "%d %d", &n, &k );
		int n2 = 1 << n;
		if ( ( k + 1 ) % n2 == 0 )
		{
			printf( "ON\n" );
		}
		else
		{
			printf( "OFF\n" );
		}
	}
	return 0;
}