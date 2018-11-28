#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
using namespace std;

int p, inf= 0x7fffffff;
int dp[15][2000][15];

void solve(){
	int i,j,k,u,v,cost,idx=0;
	
	for( k= p; k>= 1; k-- )
		for( i= 0; i< (1<<(k-1)); i++ ){
			scanf("%d",&cost);
			
			for( u= 0; u<= p; u++ )
			if( dp[k][2*i][u]!= inf )
			for( v= 0; v<= p; v++ )
			if( dp[k][2*i+1][v]!= inf ){
				int num= max( u, v );
				
				dp[k-1][i][num]= min(dp[k-1][i][num],dp[k][i<<1][u]+dp[k][i<<1|1][v]);
				if(num>=1)
				dp[k-1][i][num-1]= min(dp[k-1][i][num-1],dp[k][i<<1][u]+dp[k][i<<1|1][v]+cost);
			}
		}

	printf("%d\n",dp[0][0][0]);
}

int main(){
	int test,cnt= 0;
	
	freopen("A.in", "r", stdin );
	freopen("b.txt", "w", stdout );
	
	scanf("%d", &test );
	while( test-- ){
		  scanf("%d",&p);
		  
		  int i,j,k,x;
		  memset(dp,-1,sizeof(dp));
		  
		  for( i= 0; i<= p; i++ )
		  for( j= 0; j<= p; j++ )
		  for( k= 0; k< (1<<p); k++ )
		  dp[i][k][j]=inf;
		  
		  for( i= 0; i< (1<<p); i++ ){
			  scanf("%d",&x);
			  dp[p][i][p-x]=0;
		  }
		  
		  printf("Case #%d: ",++cnt);
		  solve();
	}
	
	return 0;
}
