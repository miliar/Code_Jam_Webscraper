#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int memo[512][32];
char *w = "welcome to code jam";
char s[512];

int faz(int i, int j)
{
    if (memo[i][j] > -1)
        return(memo[i][j]);

    if (s[i] != w[j])
        memo[i][j] = 0;
    else if (s[i] == w[j] && w[j+1] == 0)
        memo[i][j] = 1;
    else
    {
        memo[i][j] = 0;
        for(int k = i+1; s[k]; k++)
        {
            memo[i][j] += faz(k,j+1);
            memo[i][j] %= 10000;
        }
    }

    return(memo[i][j]);
}

int main(void)
{
    int T;

    scanf("%d\n",&T);
    for(int i = 0; i < T; i++)
    {
        fgets(s,512,stdin);
        memset(memo,-1,sizeof(memo));

        int r = 0;
        for(int j = 0; s[j]; j++)
        {
            r += faz(j,0);
            r %= 10000;
        }
        printf("Case #%d: %04d\n",i+1,r);
    }

    return(0);
}

