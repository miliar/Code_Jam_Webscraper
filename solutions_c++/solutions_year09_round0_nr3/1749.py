#include <stdio.h>
#include <string.h>

char cj[] = "welcome to code jam";
char text[501];

int dp[25][505];

int calc(int x, int y) {
    if (dp[x][y] != -1) return dp[x][y];
    int ret = calc(x,y+1);
    if (cj[x] == text[y]) ret += calc(x+1,y+1);
    dp[x][y] = ret%10000;
    return ret;
}

int main() {
    int N;
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    scanf("%d\n",&N);
    int cjlen = strlen(cj);
    for (int i=1;i<=N;++i) {
        gets(text);
        int textlen = strlen(text);
        for (int j=0;j<cjlen;++j)
            for (int k=0;k<textlen;++k)
                dp[j][k]=-1;
        for (int j=0;j<cjlen;++j)
            dp[j][textlen] = 0;
        for (int k=0;k<textlen;++k)
            dp[cjlen][k] = 1;
        dp[cjlen][textlen]=1;
        int res = calc(0,0);
        res %= 10000;
        if (res < 10) {
           printf("Case #%d: 000%d\n",i,res);
        } else if (res < 100) {
           printf("Case #%d: 00%d\n",i,res);
        } else if (res < 1000) {
           printf("Case #%d: 0%d\n",i,res);
        } else {
           printf("Case #%d: %d\n",i,res);
        }
    }
    return 0;   
}
