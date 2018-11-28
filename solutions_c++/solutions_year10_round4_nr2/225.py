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

int m[1050];
int p;
int a[1050][1050];
const ll inf = (ll)1e15;
ll dp[1050][1050][12];
int vis[1050][1050][12], vid;
ll solve(int lev, int loc, int missed )
{
	if( lev < 0 )
	{
		int maxMiss = m[loc];
		if( missed > maxMiss )
			return inf;
		return 0;
	}
	ll &ret = dp[lev][loc][missed];
	int& v = vis[lev][loc][missed];
	if( v==vid )
		return ret;
	v = vid;
	ret = a[lev][loc] + solve( lev-1, loc*2, missed-1 ) + solve( lev-1, loc*2 + 1, missed-1 );
	ret = min( ret, solve( lev-1, loc*2, missed ) + solve( lev-1, loc*2 + 1, missed ) );
	return ret;
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin ); freopen("B-small-attempt0.out", "w", stdout );
	//freopen("B-small-attempt1.in", "r", stdin ); freopen("B-small-attempt1.out", "w", stdout );
	//freopen("B-small-attempt2.in", "r", stdin ); freopen("B-small-attempt2.out", "w", stdout );
	
	freopen("B-large.in", "r", stdin ); freopen("B-large.out", "w", stdout );
	
	int T;
	s(T);
	for(int t=1; t <= T; t++)
	{
		s(p);
		for(int i=0; i < (1<<p); i++)
			s(m[i]);
		for(int z=0; z < p; z++)
		{
			for(int i=0; i < (1<<(p-1-z)); ++i)
			s( a[z][i] );
		}
		++vid;
		printf("Case #%d: %lld\n", t, solve( p-1, 0, p ) );
	}
	return 0;
}
