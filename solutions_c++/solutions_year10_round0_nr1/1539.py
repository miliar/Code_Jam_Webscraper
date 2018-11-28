#include<iostream>
#include <math.h>
using namespace std ;
int num[31] ;
int main()
{
	int cas ;
	int cass = 1 ;
	freopen("A.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&cas) ;
	int x=1;
	for ( int i = 0 ; i < 32 ; i ++ )
	{
		num[i] = x ;
		x*=2;
	}
	while ( cas-- )
	{
		int n , k ;
		int m ;
		scanf("%d %d",&n,&k);
		m = num[n];
		k%=m;
		if ( k == m-1 )
			printf("Case #%d: ON\n",cass++);
		else printf("Case #%d: OFF\n",cass++);
	}
	return 0 ;
}