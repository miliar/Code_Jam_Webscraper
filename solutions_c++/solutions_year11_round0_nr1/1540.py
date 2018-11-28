#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N=110;

int n,m,a[N][2],dp[N][N],tmp[N][N],tt,px,py;
char ch;

void upd( int &x,int y )
{
	if ( x==-1 || x>y ) x=y;
}

int main()
{
	freopen( "A-large.in","r",stdin );
	freopen( "A-large.out","w",stdout );

	scanf( "%d",&tt );

	int t,ca=0;
	while ( tt-- )
	{
		scanf("%d",&n );
		m=1;
		for ( int i=1;i<=n;i++ )
		{
			scanf( "%c%c%d",&ch,&ch,&a[i][1] );
			a[i][0]=(ch=='O');
			m=m>a[i][1]?m:a[i][1];
		}
		memset( dp,-1,sizeof(dp) );
		dp[1][1]=0;
		px=1; py=1;

		for ( int i=1;i<=n;i++ )
		{
			if ( a[i][0] )
			{
				for ( int j=1;j<=m;j++ )
					tmp[a[i][1]][j]=-1;
			}
			else
			{
				for ( int j=1;j<=m;j++ )
					tmp[j][a[i][1]]=-1;
			}

			if ( px )
			{
				for ( int j=1;j<=m;j++ )
				if ( dp[py][j]!=-1 )
				{
					if ( a[i][0] ) 
					{
						t=abs(a[i][1]-py)+1;
						for ( int k=j;k<=m && k<=j+t;k++ )
							upd(tmp[a[i][1]][k],t+dp[py][j]);
						for ( int k=j;k>=1 && k>=j-t;k-- )
							upd(tmp[a[i][1]][k],t+dp[py][j]);
					}
					else
					{
						t=abs(a[i][1]-j)+1;
						for ( int k=py;k<=m && k<=py+t;k++ )
							upd(tmp[k][a[i][1]],t+dp[py][j]);
						for ( int k=py;k>=1 && k>=py-t;k-- )
							upd(tmp[k][a[i][1]],t+dp[py][j]);
					}				
				}
			}
			else
			{
				for ( int j=1;j<=m;j++ )
				if ( dp[j][py]!=-1 )
				{
					if ( a[i][0]==0 ) 
					{
						t=abs(a[i][1]-py)+1;
						for ( int k=j;k<=m && k<=j+t;k++ )
							upd(tmp[k][a[i][1]],t+dp[j][py]);
						for ( int k=j;k>=1 && k>=j-t;k-- )
							upd(tmp[k][a[i][1]],t+dp[j][py]);
					}
					else
					{
						t=abs(a[i][1]-j)+1;
						for ( int k=py;k<=m && k<=py+t;k++ )
							upd(tmp[a[i][1]][k],t+dp[j][py]);
						for ( int k=py;k>=1 && k>=py-t;k-- )
							upd(tmp[a[i][1]][k],t+dp[j][py]);
					}				
				}
			}

			px=a[i][0];
			py=a[i][1];

			if ( px )
			{
				for ( int j=1;j<=m;j++ )
					dp[py][j]=tmp[py][j];
			}
			else
			{
				for ( int j=1;j<=m;j++ )
					dp[j][py]=tmp[j][py];
			}


		}

		int ans=-1;
		if ( px )
		{
			for ( int j=1;j<=m;j++ )
				if ( dp[py][j]!=-1 )
				upd(ans,dp[py][j]);
		}
		else
		{
			for ( int j=1;j<=m;j++ )
				if ( dp[j][py]!=-1 )
				upd(ans,dp[j][py]);
		}
		
		printf( "Case #%d: %d\n",++ca,ans );
	
	
	}

	return 0;



}



