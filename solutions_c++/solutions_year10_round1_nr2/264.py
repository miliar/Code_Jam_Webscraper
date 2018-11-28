#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;


int n,m,dp[120][300],cd,ci,tt,a[120],ans,ca;


int main()
{
	freopen( "2.in","r",stdin );
	freopen( "2.out","w",stdout );

	scanf( "%d",&tt );
	ca=0;
	while ( tt-- )
	{
		scanf( "%d%d%d%d",&cd,&ci,&m,&n );
		for ( int i=1;i<=n;i++ )
			scanf( "%d",&a[i] );

		for ( int i=0;i<=255;i++ )
			dp[1][i]=min( abs(i-a[1]),cd );

		for ( int i=2;i<=n;i++ )
			for ( int j=0;j<=255;j++ )
			{
				dp[i][j]=cd*i;
				for ( int k=0;k<=255;k++ )
				{
					if ( abs(j-k)<=m )
					{
						if ( dp[i][j]>dp[i-1][k]+min( abs(j-a[i]),cd+ci ) )
							dp[i][j]=dp[i-1][k]+min( abs(j-a[i]),cd+ci );
					}
					else if ( m>0 )
					{
						if ( dp[i][j]>dp[i-1][k]+ci* ((abs(j-k)-1)/m) +min( abs(j-a[i]),cd+ci ) )
							dp[i][j]=dp[i-1][k]+ci* ((abs(j-k)-1)/m) +min( abs(j-a[i]),cd+ci );
					}
					if ( dp[i][j]>dp[i-1][j]+cd ) dp[i][j]=dp[i-1][j]+cd;
				}
//				if ( j==200 )  printf( "%d\n",dp[i][j] );
			}	
		
/*
		for ( int i=1;i<=n;i++,printf( "\n" ) )
			for ( int j=0;j<=10;j++ )
				printf( "%d ",dp[i][j] );
*/
		ans=cd*n;
		for ( int j=0;j<=255;j++ )
			if ( ans>dp[n][j] ) 
		{
			ans=dp[n][j];
//			if ( dp[n][j]==55  ) printf( "%d\n",j );
		}

		printf( "Case #%d: %d\n",++ca,ans );

//		return 0;
	
	}

	return 0;
	


}




