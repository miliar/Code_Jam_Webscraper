#include <cstdio>
#include <cstring>

const int N=1010;

int n,m,a[N],sum,xo,tt,ca;

int main()
{
	freopen( "C-large.in","r",stdin );
	freopen( "C-large.out","w",stdout );

	scanf( "%d",&tt );
	while ( tt-- )
	{
		scanf( "%d",&n );
		sum=xo=0;
		a[0]=10000000;
		for ( int i=1;i<=n;i++ )
		{
			scanf( "%d\n",&a[i] );
			a[0]=a[0]<a[i]?a[0]:a[i];
			sum+=a[i];
			xo^=a[i];
		}
		printf( "Case #%d: ",++ca );
		if ( xo!=0 ) printf( "NO\n" );
		else printf( "%d\n",sum-a[0] );
	}
	return 0;


}



