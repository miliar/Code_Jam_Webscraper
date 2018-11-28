# include <iostream>
# include <cstring>
using namespace std;

int dp[30][600], n, m;
char c[30]="welcome to code jam", d[600];


int go(int i, int j)
{
    if (i==n) {
        return 1;
    }
    if (j==m) {
        return 0;
    }
    if (dp[i][j]!=-1) {
        return dp[i][j];
    }
    if (c[i]==d[j]) {
        dp[i][j]=go(i, j+1)+go(i+1, j+1);
    }
    else {
        dp[i][j]=go(i, j+1);
    }
    return dp[i][j];
}

int main()
{
    int t, tt=1;
    scanf("%d", &t);
    n=strlen(c);
    gets(d);
    while(t--) {
        gets(d);
        m=strlen(d);
        memset(dp, -1, sizeof dp);
        printf("Case #%d: %.4d\n", tt++, go(0, 0));
    }
    return 0;
}
