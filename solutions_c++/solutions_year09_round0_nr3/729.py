#include <stdio.h>
#include <string.h>
#define MAXL 510

int dp[MAXL][20];
char st[MAXL],model[20] = "welcome to code jam";
int main(){
	int t_case,t,i,j,k,len,res;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t_case);
	gets(st);
	for (t = 1;t <= t_case;t++){
		memset(dp,0,sizeof(dp));
		gets(st);
		len = strlen(st);
		if (st[0] == 'w') dp[0][0] = 1;
		for (i = 1;i < len;i++)
			for (j = 0;j < 19;j++)
				if (st[i] == model[j])
					if (j == 0)
						dp[i][0] = 1;
					else{
						dp[i][j] = 0;
						for (k = 0;k < i;k++)
							if (st[k] == model[j-1]){
								dp[i][j] += dp[k][j-1];
								if (dp[i][j] >= 10000) dp[i][j] -= 10000;
							}
					}
		res = 0;
		for (i = 18;i < len;i++){
			res += dp[i][18];
			if (res >= 10000) res -= 10000;
		}
		printf("Case #%d: %04d\n",t,res);
	}
	fclose(stdout);
}
