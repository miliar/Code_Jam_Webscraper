#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i,n) for( int i = 0, _n = (n); i < _n; i++ )
#define forn(i,a,b) for( int i = (a), _n = (b); i <= _n; i++ )
#define ford(i,a,b) for( int i = (a), _n = (b); i >= _n; i-- )
#define foreach(it,c) for( typeof((c).begin()) it = (c).begin(); it != (c).end(); it++ )

#define debug(x) cout << ">>" << #x << " = " << x << endl; 

#define two(x) (1<<(x))
#define contain(S,x) (((S)&two(x)) > 0)
#define twoll(x) (1LL<<(x))
#define containll(S,x) (((S)&twoll(x))>0)

typedef long long ll;
typedef vector<int> vi;

ll duitfrom[1005];

int R,k,n;
int g[1005];
int pos[1005];

vi apapun;

int main()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );

	int ntc; 
	scanf( "%d", &ntc );
	rep( T, ntc )
	{
		scanf( "%d%d%d", &R,&k,&n );
		rep( i, n ) scanf( "%d", &g[i] );
		
		memset( pos,-1,sizeof(pos) );
		memset( duitfrom,0,sizeof(duitfrom) );
		apapun.clear();

		int i = 0;
		ll duit = 0;

		while( pos[i]==-1 && R > 0 )
		{
			pos[i] = apapun.size();
			apapun.push_back( i );

			int j = i; 
			ll val = 0;
		
			while( val+g[i] <= k ) 
			{
				val += g[i];
				i = (i+1)%n;
				if( i == j ) break;
			}
			
			if( val == 0 )
				goto finish;
			
			duit += val;
			duitfrom[j] = val;
			R--;
		}
		
		if( R > 0 )
		{
			ll tmpduit = 0;
			forn( a, pos[i], apapun.size()-1 ) tmpduit += duitfrom[apapun[a]];
			duit += tmpduit*(R/(apapun.size()-pos[i]));
			R = R%(apapun.size()-pos[i]);
			forn( a, pos[i], pos[i]+R-1 ) duit += duitfrom[apapun[a]];
		}
		finish:;
		printf( "Case #%d: %I64d\n", T+1, duit );
	}
	return 0;
}
