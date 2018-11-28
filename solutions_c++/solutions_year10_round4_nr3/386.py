#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int n,m,ans,tt,ca;
bool a[1001][1001],ff;

int main()
{
	freopen( "c.in","r",stdin );
	freopen( "c.out","w",stdout );

	scanf( "%d",&tt );
	while ( tt-- )
	{
		cerr<<tt<<endl;
		scanf( "%d",&n );
		memset( a,0,sizeof(a) );
		for ( int i=1;i<=n;i++ )
		{
			int x,y,xx,yy;
			scanf( "%d%d%d%d",&x,&y,&xx,&yy );
			for ( int j=x;j<=xx;j++ )
				for ( int k=y;k<=yy;k++ )
					a[j][k]=1;
		}
/*
		for ( int i=1;i<=10;i++,printf("\n") )
			for ( int j=1;j<=10;j++ )
				printf( "%d ",a[i][j] );
*/	
		
		for ( ans=0;1;ans++ )
		{
			ff=0;
			for ( int i=1000;i>=1;i-- )
				for ( int j=1000;j>=1;j-- )
					if ( a[i][j] ) 
					{
						ff=1;
						if ( !a[i][j-1] && !a[i-1][j] ) a[i][j]=0;
					}
					else
					{
						if ( a[i][j-1] && a[i-1][j] ) a[i][j]=1;
					}
			if ( !ff ) break;		
		}

		printf( "Case #%d: %d\n",++ca,ans );
	
	}

	return 0;
	


}



