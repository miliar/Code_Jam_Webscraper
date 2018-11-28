#include <cstdio>
#include <cstring>
const char str[]="welcome to code jam";
int dp[512][32];
char s[512];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);gets(s);
	for(int cas=1;cas<=T;++cas){
		gets(s);
		memset(dp[0],0,sizeof(dp[0]));
		dp[0][0]=(str[0]==s[0]);
		for(int i=1;s[i];++i){
			memcpy(dp[i],dp[i-1],sizeof(dp[0]));
			if(s[i]==str[0]) ++dp[i][0];
			for(int j=1;j<=18;++j)
				if(s[i]==str[j]) dp[i][j]+=dp[i-1][j-1];
			for(int j=0;j<=18;++j) dp[i][j]%=10000;
		}
		printf("Case #%d: %04d\n",cas,dp[strlen(s)-1][18]);
	}
	return 0;
}