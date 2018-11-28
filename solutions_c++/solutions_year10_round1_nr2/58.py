// by shik
#include <iostream>
using namespace std;
int main()
{
	int t,T,D,I,M,n,a[110],i,j,k,dp[110][260],ans,tmp;
	scanf("%d",&T);
	for ( t=1; t<=T; t++ ) {
		scanf("%d%d%d%d",&D,&I,&M,&n);
		for ( i=1; i<=n; i++ ) scanf("%d",a+i);
		for ( i=1; i<=n; i++ ) { // can rolling
			for ( j=0; j<256; j++ ) dp[i][j]=dp[i-1][j]+min(D,abs(a[i]-j));
			if ( M==0 ) continue;
			for ( j=0; j<256; j++ )
				for ( k=0; k<256; k++ ) {
					if ( j==k ) continue;
					if ( (tmp=dp[i-1][k]+((abs(j-k)-1)/M+1)*I+D)<dp[i][j] ) dp[i][j]=tmp;
					if ( (tmp=dp[i-1][k]+((abs(j-k)-1)/M+0)*I+abs(a[i]-j))<dp[i][j] ) dp[i][j]=tmp;
				}
		}
		ans=1000000000;
		for ( i=0; i<256; i++ )
			if ( dp[n][i]<ans ) ans=dp[n][i];
		printf("Case #%d: %d\n",t,ans);	
	}
	return 0;
}
