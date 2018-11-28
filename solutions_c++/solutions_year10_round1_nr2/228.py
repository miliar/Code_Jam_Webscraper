#include <stdio.h>
#include <iostream.h>

int dp[2][256],x[100];

#define _abs(x) (((x)>=0)?(x):(-(x)))
#define _min(x,y) (((x)<(y))?(x):(y))

int main(){
	int t,u,i,j,k,D,I,M,n,h;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>D>>I>>M>>n;
		for (i=0; i<n; i++) cin>>x[i];
		for (i=0; i<256; i++) dp[0][i]=dp[1][i]=0;
		for (i=0; i<n; i++){
			//delete
			for (j=0; j<256; j++) dp[1][j]=dp[0][j]+D;
			//add
			for (k=0; k<256; k++){
				if (M==0){
					j=k;
					dp[1][k]=_min(dp[1][k],dp[0][j]+_abs(x[i]-k));
				}
				else{
					for (j=0; j<256; j++){
						dp[1][k]=_min(dp[1][k],dp[0][j]+_abs(x[i]-k)+I*(j!=k)*((_abs(j-k)-1)/M));
					}
				}
			}
			//for (j=0; j<50; j++) cout<<dp[1][j]<<" ";
			//cout<<endl;
			
			for (j=0; j<256; j++)
				dp[0][j]=dp[1][j];
		}
		for (j=1; j<256; j++) dp[0][0]=_min(dp[0][0],dp[0][j]);
		printf("Case #%d: %d",u+1,dp[0][0]);
		
		printf("\n");
	}
	return 0;
}
