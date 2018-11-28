#include <cstdio>
#include <cstring>

int n,m,dp[60][60][2],tt,k,ca;
char a[60][60],ch;
bool fr,fb;


int main()
{
	freopen( "1.in","r",stdin );
	freopen( "1.out","w",stdout );

	ca=0;
	scanf( "%d",&tt );
	while ( tt-- )
	{
		scanf( "%d%d",&n,&k );
		for ( int i=0;i<n;i++ )
			scanf( "%s",a[i] );
		for ( int i=0;i<n;i++ )
		{
			m=n;
			for ( int j=n-1;j>=0;j-- )
				if ( a[i][j]!='.' )
				{
					ch=a[i][j];		a[i][j]='.';
					a[i][--m]=ch;
				}		
		}

//		for ( int i=0;i<n;i++ )	printf( "%s\n",a[i] );	printf( "\n" );

		memset( dp,0,sizeof(dp) );

		fr=fb=0;
		for ( int i=0;i<n;i++ )
			for ( int j=0;j<n;j++ )
			if ( a[i][j]=='R' )
			{
				if ( j==0 ) dp[i][j][0]=1;
				else dp[i][j][0]=dp[i][j-1][0]+1;
				if ( dp[i][j][0]>=k ) fr=1;
			}
			else if ( a[i][j]=='B' )
			{
				if ( j==0 ) dp[i][j][1]=1;
				else dp[i][j][1]=dp[i][j-1][1]+1;
				if ( dp[i][j][1]>=k ) fb=1;
			}

		memset( dp,0,sizeof(dp) );
		for ( int i=0;i<n;i++ )
			for ( int j=0;j<n;j++ )
			if ( a[i][j]=='R' )
			{
				if ( i==0 ) dp[i][j][0]=1;
				else dp[i][j][0]=dp[i-1][j][0]+1;
				if ( dp[i][j][0]>=k ) fr=1;
			}
			else if ( a[i][j]=='B' )
			{
				if ( i==0 ) dp[i][j][1]=1;
				else dp[i][j][1]=dp[i-1][j][1]+1;
				if ( dp[i][j][1]>=k ) fb=1;
			}

		memset( dp,0,sizeof(dp) );
		for ( int i=0;i<n;i++ )
			for ( int j=0;j<n;j++ )
			if ( a[i][j]=='R' )
			{
				if ( i==0 || j==0 ) dp[i][j][0]=1;
				else dp[i][j][0]=dp[i-1][j-1][0]+1;
				if ( dp[i][j][0]>=k ) fr=1;
			}
			else if ( a[i][j]=='B' )
			{
				if ( i==0 || j==0 ) dp[i][j][1]=1;
				else dp[i][j][1]=dp[i-1][j-1][1]+1;
				if ( dp[i][j][1]>=k ) fb=1;
			}

		memset( dp,0,sizeof(dp) );
		for ( int i=0;i<n;i++ )
			for ( int j=0;j<n;j++ )
			if ( a[i][j]=='R' )
			{
				if ( i==0 || j==n-1 ) dp[i][j][0]=1;
				else dp[i][j][0]=dp[i-1][j+1][0]+1;
				if ( dp[i][j][0]>=k ) fr=1;
			}
			else if ( a[i][j]=='B' )
			{
				if ( i==0 || j==n-1 ) dp[i][j][1]=1;
				else dp[i][j][1]=dp[i-1][j+1][1]+1;
				if ( dp[i][j][1]>=k ) fb=1;
			}

		printf( "Case #%d: ",++ca );
		if ( fr && fb ) printf( "Both\n" );
		else if ( fr ) printf( "Red\n" );
		else if ( fb ) printf( "Blue\n" );
		else printf( "Neither\n" );
		
	}

	return 0;





}




