#include<stdio.h>
#include<string.h>

char wlcome[] = "welcome to code jam";
int dp[550][20];
char str[550];

int main(){
    freopen("C-large.in" , "r" , stdin);
    freopen("C-large.out" , "w" , stdout);
    int tst , kase = 1 , i , j , ln , k , ret;
    scanf("%d" , &tst);
    gets(str);
    while(tst--){
        gets(str);
        ln = strlen(str);
        memset(dp , 0 , sizeof(dp));
        ret = 0;
        for(i = 0;i<ln;i++){
            for(j = 0;j<19;j++){
                if(str[i] == wlcome[j]){
                    if(str[i] == 'w') dp[i][0]++;
                    else{
                        for(k = 0;k<i;k++)
                            dp[i][j] = (dp[i][j]+dp[k][j-1])%10000;
                    }
                }
            }
            if(str[i] == 'm') ret = (ret+dp[i][18])%10000;
        }
        printf("Case #%d: %04d\n" , kase++ , ret);
    }
    return 0;
}
