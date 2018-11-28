#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
char mp[7][7];
int dp[7][7][4];
char win[2];
int main()
{

    //freopen("A-small-attempt3.in","r",stdin);
    //freopen("b.txt","w",stdout);
    int T,c=1;
    scanf("%d",&T);

    while(T--){
        int cnt=0,flg=0;
        for(int i=1;i<=4;++i){
            scanf("%s",mp[i]+1);
            //printf("%s\n",mp[i]+1);
        }
        memset(dp,0,sizeof(dp));
        for(int i=1;i<=4;++i){
        for(int j=1;j<=4;++j){
            if(mp[i][j]=='.')continue;
            cnt++;
            if(mp[i][j]=='T'){
                if(i>1&&mp[i-1][j]!='.'){
                    if(dp[i-1][j][2]==2){
                        flg=1;
                        win[0]=mp[i-1][j];
                        break;
                    }
                    if(mp[i-1][j]==mp[i+1][j])
                    dp[i+1][j][2]=max(dp[i+1][j][2],dp[i-1][j][2]+2);
                    else dp[i+1][j][2]=max(dp[i+1][j][2],2);
                }
                if(j>1&&mp[i][j-1]!='.'){
                    if(dp[i][j-1][0]==2){
                        flg=1;
                        win[0]=mp[i][j-1];
                        break;
                    }
                    else if(mp[i][j-1]==mp[i][j+1])
                    dp[i][j+1][0]=max(dp[i][j+1][0],dp[i][j-1][0]+2);
                    else dp[i][j+1][0]=max(dp[i][j+1][0],2);
                }
                if(i>1&&j>1&&mp[i-1][j-1]!='.'){
                    if(dp[i-1][j-1][1]==2){
                        flg=1;
                        win[0]=mp[i-1][j-1];
                        break;
                    }
                    else if(mp[i-1][j-1]==mp[i+1][j+1])
                    dp[i+1][j+1][1]=max(dp[i+1][j+1][1],dp[i-1][j-1][1]+2);
                    else  dp[i+1][j+1][1]=max(dp[i+1][j+1][1],2);
                }
                if(i>1&&j<4&&mp[i-1][j+1]!='.'){
                    if(dp[i-1][j+1][3]==2){
                        flg=1;
                        win[0]=mp[i-1][j+1];
                        break;
                    }
                    else if(mp[i-1][j+1]==mp[i+1][j-1])
                    dp[i+1][j-1][3]=max(dp[i+1][j-1][3],dp[i-1][j+1][3]+2);
                    else dp[i+1][j-1][3]=max(dp[i+1][j-1][3],2);
                }
                continue;
            }
            if((mp[i][j]==mp[i-1][j-1])||mp[i-1][j-1]=='T'){
                dp[i][j][1]=max(dp[i][j][1],dp[i-1][j-1][1]+1);
                //printf("%d\n",dp[i][j]);
            }
            if((mp[i][j]==mp[i][j-1])||mp[i][j-1]=='T'){
                dp[i][j][0]=max(dp[i][j][0],dp[i][j-1][0]+1);
                //printf("%d\n",dp[i][j]);
                //if(dp[i][j]==4){win=mp[i][j];flg=1;break;}
            }
            if((mp[i][j]==mp[i-1][j])||mp[i-1][j]=='T'){
                dp[i][j][2]=max(dp[i][j][2],dp[i-1][j][2]+1);
                 //printf("%d\n",dp[i][j]);

            }
            if((mp[i][j]==mp[i-1][j+1])||mp[i-1][j+1]=='T'){
                dp[i][j][3]=max(dp[i][j][3],dp[i-1][j+1][3]+1);
                 //printf("%d\n",dp[i][j]);

            }
            for(int k=0;k<4;++k)
             if(dp[i][j][k]>=3){win[0]=mp[i][j];flg=1;break;}
             if(flg)break;
        }
        if(flg)break;
        }

        printf("Case #%d: ",c++);
        if(flg){
            printf("%s won\n",win);
        }
        else if(cnt==16)printf("Draw\n");
        else printf("Game has not completed\n");

    }
    return 0;
}
