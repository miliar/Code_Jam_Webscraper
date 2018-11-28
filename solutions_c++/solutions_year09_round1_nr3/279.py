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

#define type long double
const int mxn = 50;
type comb[mxn][mxn];
int c, n;
type dp[mxn]; 
int vis[mxn], vid;
type solve( int have)
{
	if( have == c )
		return 0.0;
	if( vis[have] == vid )
		return dp[have];
	vis[have] = vid;
	
	type expected  = 0;
	for(int com=0; com <= have; com++)
	{
		int uncom = n - com;
		if( have+uncom > c )
			continue;
		
		type p = ( comb[ have ][ com ] * comb[c-have][uncom] ) / comb[ c ][ n ]  ;
		if( com == have )
		{
			expected += p;
			expected = expected / ( 1 - p );
		}
		else
			expected += p*(1+solve(have+uncom) );
	}
	return dp[have] = expected;
}

int main()
{
	comb[0][0] = 1;
	for(int N=1; N < mxn; N++)
	{
		comb[N][0] = 1;
		for(int k=1; k <= N; k++)
		{
			comb[N][k] = comb[ N-1 ][ k ] + comb[ N-1 ][ k-1 ];
		}
	}
	int runs;
	cin>>runs;
	for(int C=1; C <= runs; C++)
	{
		cin>>c>>n;
		++vid;
		printf("Case #%d: %.7lf\n", C, 1.0 + double(solve( n )) );
	}
	
	
	return 0;
}

