#include <stdio.h>
#include <memory.h>
#include <string.h>

char ch[] = "welcome to code jam";

char str[1000];

int dp[1000][20];

int getInd(char cha) {
	int k;
	for (k = 0; k < 19; k ++) {
		if (cha == ch[k]) return k;
	}
	return -1;
}


int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int N;
	int i,j,k,p;
	int Case = 1;
	scanf("%d ",&N);
	for (p = 0; p < N; p ++) {
		//scanf("%s",str+1);
		gets(str+1);
		int len = strlen(str+1);
		memset(dp,0,sizeof(dp));
		for (j = 1; j <= len; j ++) {

			for (k = 0; k < 19; k ++) {
				dp[j][k] = dp[j-1][k];
			}

			if (str[j] == 'w') {
				dp[j][0] ++;
			} else if (str[j] == 'e') {
				dp[j][1] += dp[j-1][0];
				dp[j][6] += dp[j-1][5];
				dp[j][14] += dp[j-1][13];
			} else if (str[j] == 'l') {
				dp[j][2] += dp[j-1][1];
			} else if (str[j] == 'c') {
				dp[j][3] += dp[j-1][2];
				dp[j][11] += dp[j-1][10];
			} else if (str[j] == 'o') {
				dp[j][4] += dp[j-1][3];
				dp[j][9] += dp[j-1][8];
				dp[j][12] += dp[j-1][11];
			} else if (str[j] == 'm') {
				dp[j][5] += dp[j-1][4];
				dp[j][18] += dp[j-1][17];
			} else if (str[j] == ' ') {
				dp[j][7] += dp[j-1][6];
				dp[j][10] += dp[j-1][9];
				dp[j][15] += dp[j-1][14];
			} else if (str[j] == 't') {
				dp[j][8] += dp[j-1][7];
			} else if (str[j] == 'd') {
				dp[j][13] += dp[j-1][12];
			} else if (str[j] == 'j') {
				dp[j][16] += dp[j-1][15];
			} else if (str[j] == 'a') {
				dp[j][17] += dp[j-1][16];
			}
			for (k = 0; k < 19; k ++) {
				dp[j][k] %= 10000;
			}
		}
	/*	for (i = 0; i < len; i ++) {
			for (j = 0; j < 19; j ++) {
				printf("%d ",dp[i][j]);
			}
			printf("\n");
		}*/
		printf("Case #%d: %04d\n",Case ++,dp[len][18]);
	}




	return 0;
}

