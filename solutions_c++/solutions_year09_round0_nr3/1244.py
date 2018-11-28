#include<cstdio>
#include<cstring>
int dp[20];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("ans6.txt","w",stdout);
	int Case,kk;
	char s[501];
	scanf("%d",&Case);
	gets(s);
	for(kk = 1; kk <= Case; kk++){
		gets(s);
		int i,j;
		memset(dp,0,sizeof(dp));
		for(i = 0; s[i]; i++){
			if(s[i] == 'w')
				dp[0]++;
			else if(s[i] == 'e'){
				dp[1] += dp[0];dp[1]%=10000;
				dp[6] += dp[5];dp[6]%=10000;
				dp[14] += dp[13];dp[14]%=10000;
			}
			else if(s[i] == 'l'){
				dp[2] += dp[1];dp[2]%=10000;
			}
			else if(s[i] == 'c'){
				dp[3] += dp[2];dp[3]%=10000;
				dp[11] += dp[10];dp[11]%=10000;
			}
			else if(s[i] == 'o'){
				dp[4] += dp[3];dp[4]%=10000;
				dp[9] += dp[8];dp[9]%=10000;
				dp[12] += dp[11];dp[12]%=10000;
			}
			else if(s[i] == 'm'){
				dp[5] += dp[4];dp[5]%=10000;
				dp[18] += dp[17];dp[18]%=10000;
			}
			else if(s[i] == ' '){
				dp[7] += dp[6];dp[7]%=10000;
				dp[10] += dp[9];dp[10]%=10000;
				dp[15] += dp[14];dp[15]%=10000;
			}
			else if(s[i] == 't'){
				dp[8] += dp[7];dp[8]%=10000;
			}
			else if(s[i] == 'd'){
				dp[13] += dp[12];dp[13]%=10000;
			}
			else if(s[i] == 'j'){
				dp[16] += dp[15];dp[16]%=10000;
			}
			else if(s[i] == 'a'){
				dp[17] += dp[16];
				dp[17]%=10000;
			}
		}
		printf("Case #%d: ",kk);
		printf("%d%d%d%d\n",dp[18]/1000,dp[18]%1000/100,dp[18]%100/10,dp[18]%10);
	}
	return 0;
}