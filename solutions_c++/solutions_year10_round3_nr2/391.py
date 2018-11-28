#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
using namespace std ;
struct pp
{
	int x , y ;
};
pp used[2000] ;
int l,p,c ;
bool cmp( pp a , pp b )
{
	return a.x < b.x ;
}
int main()
{
	int cas ;
	int cass = 1 ;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cas);
	while ( cas -- )
	{
		scanf("%d %d %d",&l,&p,&c);
		int i ;
		for ( i = 0 ;  ; i ++ )
		{
			double x = pow(2.0,i);
			x = pow(double(c),x)*l;
			if ( x >= p )
				break;
		}
		printf("Case #%d: %d\n",cass++,i);

	}
	return 0 ;
}