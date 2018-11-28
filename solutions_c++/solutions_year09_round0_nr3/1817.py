#include <cstdio>
#include <cstring>
using namespace std;

int main(){
	char input[501];
	char target[]={"welcome to code jam"};
	int length;
	int n;
	int dp[501][19];

	scanf("%d\n",&n);
	for(int i=1;i<=n;i++){
		gets(input);
		length=strlen(input);
		for(int j=0;j<length;j++){
			for(int k=0;k<19;k++){
				dp[j][k]=0;
				if(j>0){
					dp[j][k]+=dp[j-1][k];
				}
				if(input[j]==target[k]){
					if(j>0 && k>0){
						dp[j][k]+=dp[j-1][k-1];
					}else if(j>0){
						dp[j][k]+=1;
					}else if(k>0){
						// does nothing
					}else{
						dp[j][k]+=1;
					}
				}
				dp[j][k]%=10000;
				//printf("input[j]: %d, target[k]: %d, dp[j][k]: %d\n",j,k,dp[j][k]);
			}
		}
		printf("Case #%d: %04d\n",i,dp[length-1][18]);
	}
}