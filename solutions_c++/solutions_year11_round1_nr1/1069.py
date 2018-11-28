#include<iostream>
#include<fstream>
#include<cmath>
#include<time.h>
using namespace std;
int d, g, x , y  ;
typedef __int64 ll ;

ll gcd( ll a, ll b )
{
	if ( b == 0 ) return a ;
	for( int r = a%b ; r ; a = b , b = r , r = a%b ) ;
	return b ;
}

int main()
{
	int i, j, k, t, cas, end ;
	bool flag ;
	ll n, x , y, g , d ;

	freopen("D:\\A-small-attempt0.in","r",stdin ) ;
	freopen("D:\\out.txt","w",stdout ) ;

	scanf("%d", &t ) ;
	for( cas = 1 ; cas <= t ; cas++ )
	{
		flag = 1 ;
		scanf("%I64d", &n ) ;
		scanf("%I64d%I64d",&d, &g) ;
		x = 100/ gcd( d, 100 ) ;
		if ( x > n )
		{
			flag = 0 ;
		}
		if ( d > 0 && g == 0 )
		{
			flag = 0 ;
		}
		if ( d != 100 && g == 100 )
		{
			flag = 0 ;
		}
		printf("Case #%d: ", cas ) ;
		if ( flag ) puts("Possible") ;
		else puts("Broken") ;
	}

	return 0 ;
}