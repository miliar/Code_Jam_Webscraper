#include<string.h>
#include<stdio.h>
const int mod = 10000;
char str[512];
char m[]={"welcome to code jam"};
int dp[512][20];
int main(){
   freopen("C-large.in","r",stdin);
   freopen("data.txt","w",stdout);
    int cas, i, j, p, n, len;
    //printf("%d\n",strlen(m));
    scanf("%d",&n);
    getchar();
    for(cas = 1; cas <= n; cas++)
    {
        gets(str);
        len  = strlen(str);
        memset(dp, 0, sizeof(dp));

        for(i = 0; i < len; i++)
            if(str[i]=='w')
                dp[i][0] = 1;

        for(i = 0; i < len; i++ ){

            for(j = 1; j < 19; j++)
            {
                if(str[i]==m[j]){
                    for(p = 0; p < i; p++)
                        dp[i][j] =  ( dp[i][j] + dp[p][j-1] ) % mod;
                }
            }
        }
//        while(scanf("%d %d",&i, &j)!=EOF)
//            printf("%d\n",dp[i][j]);
        int ans = 0;
        for(i = 0; i < len; i++)
            ans = ( ans + dp[i][18]) % mod;
        printf("Case #%d: %.4d\n",cas, ans);
    }

}
/*
3
wellcoomee to cod ce edejj amm
 *
 012345678901234567890123456789
 wellcoomee to cod ce edejj amm

 */