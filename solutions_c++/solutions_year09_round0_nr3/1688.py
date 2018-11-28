#include <cstdio>
#include <cstring>

const int LEN=19;
const char WEL[]="welcome to code jam";

char s[555];
int dp[555][22];

int go()
{
	int ret=0;
	int len=strlen(s);
	memset(dp,0,sizeof dp);
	
	for(int i=0;i<len;++i){
		if(s[i]=='w'){
			dp[i][0]=1;
		}
	}
	for(int i=0;i<len;++i){
		for(int j=1;j<LEN;++j){
			if(s[i]==WEL[j]){
				for(int t=0;t<i;++t){
					dp[i][j]=(dp[i][j]+dp[t][j-1])%1000;
				}
			}
		}
		ret=(ret+dp[i][LEN-1])%1000;
	}
	return ret;
}

int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	
	//freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);
	
	int re;
	int cas;
	for(cas=1,scanf("%d",&re),getchar();re--;++cas){
		gets(s);
		printf("Case #%d: %04d\n",cas,go());
	}
}
