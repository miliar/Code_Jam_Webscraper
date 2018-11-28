#include <stdio.h>
#include <string.h>

char patt[] = "welcome to code jam";
int pl;
char buf[1000];
int dp[1000][20];

int main ()
{
    int t;
    
    pl = strlen(patt);
    scanf("%d", &t);
    fgets(buf, 1000, stdin);
    for (int it = 1; it <= t; it ++)
    {
        fgets(buf, 1000, stdin);
        for (int i = 0; buf[i]; i ++)
            for (int j = 0; j < pl; j ++)
            {
                dp[i][j] = (i == 0? 0 : dp[i - 1][j]);
                if (buf[i] == patt[j])
                {
                    if (j == 0)
                        dp[i][j] ++;
                    else
                        dp[i][j] += dp[i - 1][j - 1];
                }
                
                dp[i][j] %= 10000;
            }
        
        printf("Case #%d: %04d\n", it, dp[strlen(buf) - 1][pl - 1]);
    }
    
    return 0;
}
