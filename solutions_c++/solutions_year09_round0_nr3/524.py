#include <iostream>
#include <cstring>

using namespace std;

char line[1024];
int dp[512][20];

void lookup(char ch,int* idx_array,int& siz){
	siz = 0;
	for(int i=0;i<19;i++){
		if("welcome to code jam"[i] == ch){
			idx_array[siz++] = i;
		}
	}
}

int main(){
	int ncas;
	scanf("%d",&ncas);
	gets(line);
	for(int cas=1;cas<=ncas;cas++){
		int idx_array[20];
		int idx_len;
		memset(dp,0,sizeof(dp));
		gets(line);
		int slen = strlen(line);
		for(int i=0;i<slen;i++){
			for(int j=0;j<=18;j++) dp[i+1][j] = dp[i][j] % 1000;
			lookup(line[i],idx_array,idx_len);
			for(int j=0;j<idx_len;j++){
				int m = idx_array[j];
				if(m == 0){
					dp[i+1][m] += 1;
				}else{
					dp[i+1][m] += dp[i][m-1];
				}
				dp[i+1][m] %= 1000;
			}
		}
		printf("Case #%d: %04d\n",cas,dp[slen][18] % 1000);
	}
	return 0;
}
