#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <utility>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <memory.h>
#include <algorithm>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
const int shift = 5000000;

int n, a[10000000];
set<int> ss;

int main()
{
	int tc;
	scanf( "%d", &tc );
	for ( int qt=1; qt<=tc; qt++ )
	{
		scanf( "%d", &n );
		memset( a, 0, sizeof(a) );
		int p, c;
		ss.clear();
		forn( i,n )
		{
			scanf( "%d %d", &p, &c );
			p += shift;
			a[p] = c;
			if ( c > 1 ) ss.insert( p );
		}
		
		int ans = 0;
		while ( !ss.empty() )
		{
			int i = *ss.begin();
			ss.erase( ss.begin() );
			int r = a[i] / 2;
			a[i-1] += r;
			a[i+1] += r;
			a[i] &= 1;
			ans += r;
			if ( a[i-1] > 1 ) ss.insert( i-1 );
			if ( a[i+1] > 1 ) ss.insert( i+1 );
		}
		
		printf( "Case #%d: %d\n", qt, ans );
	}
}
