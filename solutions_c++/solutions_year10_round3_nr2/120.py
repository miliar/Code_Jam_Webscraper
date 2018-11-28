//DS includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>

//Other Includes
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define oo 					(int)13e7
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define fill(a,v) 				memset(a, v, sizeof a)
#define ull 					unsigned long long
#define ll 						long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb( z ) 				push_back( z )
#define gcd					__gcd
using namespace std;

ll L, P, C;

map< pair<ll,ll>, ll > _dp[101];
int solve( ll l, ll p, ll c )
{
	//cerr<< l << " " << p << " " << c << endl;
	if( l*c >= p )
		return 0;
	
	pair<int,int> cp( l,p );
	//cout<<"ok\n";
	if( _dp[c].count( cp ) )
		return _dp[c][cp];
	
	ll& ret = _dp[c][cp];
	
	ret = p-l+1;
	for(ll mp=l*c; mp < p; mp *= c)
	{
		ret = min( ret, 1LL + max( solve( l, mp, c ), solve( mp, p, c ) ) );
	}
	return ret;
}

void recon( int l, int p, int c )
{
	if( l*c >= p )
		return;
	int ret = p-l+1;
	int nl, np, sol;
	for(ll mp=l*c; mp < p; mp *= c)
	{
		int A = solve( l, mp, c );
		int B = solve( mp, p, c );
		int nret = 1 + max( A, B );
		if( nret < ret )
		{
			sol = mp;
			ret = nret;
			if( A > B )
			{
				nl = l; np = mp;
			}
			else
			{
				nl = mp; np = p;
			}
		}
	}
	//cout<< l <<  " " << p << " to " << nl << " " << np << " by choosing " << sol << endl;
	recon( nl, np, c );
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin ); freopen("B-small-attempt0.out", "w", stdout );
	//freopen("B-small-attempt1.in", "r", stdin ); freopen("B-small-attempt1.out", "w", stdout );
	//freopen("B-small-attempt2.in", "r", stdin ); freopen("B-small-attempt2.out", "w", stdout );
	
	freopen("B-large.in", "r", stdin ); freopen("B-large.out", "w", stdout );
	

	int T; 
	cin>>T; //T = min( T, 10 );
	for(int t=1; t <= T; t++)
	{
		cin>>L>>P>>C;
		//cout<< L << " " << P << " " << C << endl;
		//recon( L, P, C );
		
		printf("Case #%d: %d\n", t, solve( L, P, C ) );
		
	}
	
	return 0;
}
