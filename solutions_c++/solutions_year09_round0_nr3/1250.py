#include <stdio.h>
#include <string.h>

const int MOD = 10000;
const char text[30]="welcome to code jam";
const int LEN = 19;

int main()
{
    int N, test;
    scanf("%d", &N);
    getc(stdin);
    for (test = 1;test<=N;test++)
    {
        char str[512];
        int len, i, j, dp[LEN];
        //scanf("%s", str);
        gets(str);
        len = strlen(str);
        for (i=0;i<LEN;i++)
            dp[i] = 0;
        for (i=0;i<len;i++)
            for (j=LEN-1;j>=0;j--)
                if (text[j]==str[i])
                {
                    if (!j) dp[0] = (dp[0] + 1) % MOD;
                    else dp[j] = (dp[j] + dp[j-1]) % MOD;
                }

        int res = dp[LEN-1];
        printf("Case #%d: ", test);
        if (res<10) printf("000%d\n", res);
        else if (res<100) printf("00%d\n", res);
        else if (res<1000) printf("0%d\n", res);
        else printf("%d\n", res);
    }

    return 0;
}
