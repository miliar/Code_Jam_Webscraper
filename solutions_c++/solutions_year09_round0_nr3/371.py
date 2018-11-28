#include<iostream>
#include<string.h>
int main(){
    int T,dp[50],len,len2,i,j;
    char str[1000];
    freopen("C-large.out","w",stdout);
    scanf("%d ",&T);
    for(int Cas=1;Cas<=T;++Cas){
        gets(str);
        memset(dp,0,sizeof(dp));
        dp[0]=1;
        char s[]="welcome to code jam";
        len=strlen(str);
        len2=strlen(s);
        for(i=1;i<=len;++i){
            for(j=len2;j>0;--j){
                if(str[i-1]==s[j-1]){
                    dp[j]=(dp[j]+dp[j-1])%10000;
                }
                
            }
        }
        printf("Case #%d: %04d\n",Cas,dp[len2]);
    }
    return 0;
}
