#include <cstdio>
#include <cstring>

int n,m,a[1000],tt,ca;

int main()
{
	freopen( "1.in","r",stdin );
	freopen( "1.out","w",stdout );

	scanf( "%d",&tt );
	ca=0;
	while  ( tt-- )
	{
		scanf( "%d%d",&n,&m );
		memset( a,0,sizeof(a) );
		
		while ( m )
		{
			a[0]++;
			a[a[0]]=m%2;
			m/=2;	
		}
		
		bool ff=1;
		for ( int i=1;i<=n;i++ )
			if ( a[i]!=1 ) ff=0;
		ca++;
		printf( "Case #%d: ",ca );
		if ( ff ) printf( "ON\n" );
			else printf( "OFF\n" );

	}

	return 0;


}



