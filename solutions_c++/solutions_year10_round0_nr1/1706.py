#include<iostream>
#include<map>
#include<queue>
#include<vector>
#include<set>
#include<sstream>
#include<cmath>
#include<algorithm>
#define oo (int)1e9
#define s(n)scanf("%d",&n)
using namespace std;
#include<string.h>
#include<cstdio>
#define gcd __gcd
#define lcm(a,b) (a/gcd(a,b))*b
#define mod 1000000007

int n,k;
int cs;

int main()
{
	
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);	
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);	
	
	int runs;
	s( runs );
	while( runs-- )
	{
		s( n );s( k );
		printf( "Case #%d: %s\n" , ++cs , (k+1LL) % (1LL<<n) == 0 ? "ON" : "OFF" );
		
	}
}
