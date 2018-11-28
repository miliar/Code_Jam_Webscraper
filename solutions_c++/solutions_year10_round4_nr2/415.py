#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n,m,dp[2200][12],ma[2200],d[2200],p,tt,ca;
int co[2200];

int pos( int x,int y )
{
	return ((x+y)|(x!=y));
}

int rem( int x )
{
	int ans=0;
	for ( ;x>1;x=(x>>1) ) ans++;
	return ans;
}

int get( int x,int y,int z )
{
	int po=pos(x,y);
	if ( dp[po][z]>-1 ) return dp[po][z];
	if ( ma[po]<=z ) return (dp[po][z]=0);

	dp[po][z]=co[po]+get( x,(x+y)/2,z+1 )+get( (x+y)/2+1,y,z+1 );

	if ( rem(y-x+1)==ma[po]-z ) return dp[po][z];

	int tmp=get( x,(x+y)/2,z )+get( (x+y)/2+1,y,z );
	return (dp[po][z]=min( tmp,dp[po][z] ));
}




int build( int x,int y )
{
//	if (ma[pos(x,y)]>0 )	printf( "%d %d %d\n",x,y,ma[pos(x,y)] );
	if ( x==y ) return ma[pos(x,y)]=d[x];
	else return ma[pos(x,y)]=max( build(x,(x+y)/2),build((x+y)/2+1,y) );

}



int main()
{
	freopen( "b.in","r",stdin );
	freopen( "bb.out","w",stdout );

	scanf( "%d",&tt );
	ca=0;
	while ( tt-- )
	{
		scanf( "%d",&p );
		m=0;
		n=(1<<p);
		for ( int i=0;i<n;i++ )
		{
			scanf( "%d",&d[i] );
			d[i]=p-d[i];
			if ( m<d[i] ) m=d[i];
		}
		memset( dp,-1,sizeof(dp) );

		for ( int len=2;len<=n;len*=2 )
		{
			for ( int i=0;i<n;i+=len )
				scanf("%d",&co[pos(i,i+len-1)]);		
		}

		build(0,n-1);
		build(0,n-1);


		printf( "Case #%d: %d\n",++ca,get(0,n-1,0) );
	
	}

	return 0;



}




