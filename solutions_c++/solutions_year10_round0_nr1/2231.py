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



int main()
{
	freopen( "A-small-attempt2.in", "r", stdin );
	freopen( "A-small-attempt2.out" ,"w", stdout );
	
	/*
	{
		int n=5, k = 1<<n;
		int z = 0;
		int f = 0;
		while( k-- )
		{
			int i;
			for(i=0; (z&1<<i) && i < n; i++)
			{
				z ^= 1<<i;
			}
			z ^= 1<<i;
			
			assert( z==++f );
			for(i=0; i < n; i++) 
			putchar( z & 1<< i ? '1' : '0' );
			putchar('\n' );
			
		}
	}*/
	
	
	int T;
	cin>>T;
	for(int t=1; t <= T; t++)
	{
		int n, k;
		cin>>n>>k;
		int zz = (1<<n)-1;
		
		printf("Case #%d: %s\n", t, (k & zz)==zz  ? "ON" : "OFF" );
	}
	
	
	return 0;
}
