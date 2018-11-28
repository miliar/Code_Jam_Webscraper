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


int l, d, n;

char words[5002][20];
char pattern[10007];

inline short matches( char *a, char *w )
{
	int asz = strlen( a ), wsz = strlen( w );
	int wi = 0;
	for(int i=0; i < asz && wi < wsz; i++)
	{
		if( a[i] == '(' )
		{
			int j = i+1;
			bool got = 0;
			while( a[j] != ')' )
			{
				if( a[j] == w[wi] )
					got = 1;
				++j;
			}
			if( !got )
			{
				return 0;
			}
			wi++;
			i = j;
		}
		else if( a[i] != w[wi] )
		{
			return 0;
		}
		else
			wi++;
	}
	return 1;
}
int main()
{
	s( l ); s( d ); s( n );
	for(int i=0; i < d; i++)
	scanf("%s", words[i] );
	for(int c=1; c <= n; c++)
	{
		scanf("%s", pattern );
		
		int ans = 0;
		for(int j=0; j < d; j++)
		{
			int cur = matches( pattern, words[j] );
			ans += cur;
		}
		printf("Case #%d: %d\n", c, ans );
	}
	return 0;
}
