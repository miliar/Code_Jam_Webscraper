#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<sstream>
#include<set>
#include<fstream>
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


char a[512];
char *p = "welcome to code jam";
int psz, asz;
const int mod = int(1e4);
int dp[512][32], vis[512][32], vid;
int solve( int ai, int pi )
{
	if( pi == psz )
		return 1;
	if( ai == asz )
		return 0;
	int& d = dp[ai][pi];
	int& v = vis[ai][pi];
	if( v == vid )
		return d;
	v = vid;
	d = solve( ai+1, pi );
	if( a[ai] == p[pi] )
		d = ( d + solve( ai+1, pi+1) ) % mod;
	return d;
}
int main()
{
	int runs;
	scanf("%d\n", &runs );
	psz = strlen( p );
	for(int c=1; c <= runs; c++)
	{
		gets( a );
		asz = strlen( a );
		++vid;
		printf("Case #%d: %04d\n", c, solve( 0, 0 ) );
		
	}
	return 0;
}
