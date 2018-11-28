#include <cstdio>
#include <iostream>
#include <iostream>
using namespace std;
char str[30] = "welcome to code jam";
char query[501];
int dp[510][20];
int main()
{
        int len = strlen(str);
        int i,j,t,cnt,kase,n;
        gets(query);
        sscanf(query,"%d",&t);
        for(kase=1;kase<=t;kase++){
                gets(query);
                n = strlen(query);

        memset(dp,0,sizeof dp);

                if(query[0]=='w')
                        dp[0][0] = 1;


                for(i=1;i<n;i++){
                        dp[i][0] = dp[i-1][0];
                        if(query[i] =='w')
                                dp[i][0] += 1;

                        for(j=1;j<len;j++){
                                dp[i][j] = dp[i-1][j];
                                if(query[i] == str[j]){
                                        dp[i][j] += dp[i-1][j-1];
                                        dp[i][j] %= 10000;
                                }
                        }
                }

                cout <<"Case #"<<kase<<": ";
                printf("%04d\n",dp[n-1][len-1]);
        }

        return 0;
}


