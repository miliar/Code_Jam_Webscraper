#include<stdio.h>
#include<string.h>
#define MOD 10000
int dp[510][20];
char s[510],ts[10],cp[]="welcome to code jam";
int cnt[20];
int main()
{
	int nn;
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	//freopen("C-small.out","w",stdout);
	freopen("C-large.out","w",stdout);
	scanf("%d",&nn);
	gets(ts);
	for (int ii=1;ii<=nn;ii++) {
		printf("Case #%d: ",ii);
		memset(dp,0,sizeof(dp));
		memset(cnt,0,sizeof(cnt));
		gets(s);
		int l=strlen(s);
		for (int i=0;s[i];i++) {
			for (int j=0;j<19;j++) if (s[i]==cp[j]) {
				if (j==0) dp[i][j]=1;
				else dp[i][j]=cnt[j-1];
				cnt[j]+=dp[i][j];
				if (cnt[j]>=MOD) cnt[j]%=MOD;
			}
		}
		printf("%0.4d\n",cnt[18]);
	}
}
