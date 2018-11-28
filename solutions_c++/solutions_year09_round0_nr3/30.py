#include <cstdio>

#define phraselen 19
char phrase[] = "welcome to code jam";

char str[505];
int dp[505][phraselen+1];

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int nCases;
    scanf("%d", &nCases);
    char c;
    do {
	c = fgetc(stdin);
    } while(c != '\n');
    for(int casenum = 1; casenum <= nCases; casenum++) {

	int len = 0;
	while(true) {
	    str[len] = fgetc(stdin);
	    if(str[len] == '\n')
		break;
	    else
		len++;
	}

	dp[0][0] = 1;
	for(int j = 1; j <= phraselen; j++)
	    dp[0][j] = 0;

	for(int i = 1; i <= len; i++) {

	    dp[i][0] = 1;

	    for(int j = 1; j <= phraselen; j++) {
		dp[i][j] = dp[i-1][j];
		if(str[i-1] == phrase[j-1])
		    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % 10000;
	    }

	}

	printf("Case #%d: ", casenum);

	int ans = dp[len][phraselen];
	if(ans == 0)
	    printf("0000\n");
	else {
	    if(ans < 10)
		printf("000");
	    else if(ans < 100)
		printf("00");
	    else if(ans < 1000)
		printf("0");
	    printf("%d\n", ans);
	}

    }
}
