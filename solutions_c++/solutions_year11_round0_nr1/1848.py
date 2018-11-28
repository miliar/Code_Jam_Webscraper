#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
using namespace std;
int T,n,b;
vector<pair<char,int>> ord;
int dp[101][101][101];
char a;
const int INF=0x3f3f3f3f;
int myabs(int x)
{
    return x>0?x:(-x);
}
int main()
{
    freopen("AL.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>n;
        ord.clear();
        for(int i=1;i<=n;i++)
        {
            cin>>a>>b;
            ord.push_back(pair<char,int>(a,b));
        }
        memset(dp,0x3f,sizeof(dp));
        dp[0][1][1]=0;
        for(int k=0;k<n;k++)    //处理到了第N条命令
        {
            char np=ord[k].first;
            int np1=ord[k].second;
            for(int i=1;i<=100;i++)
                for(int j=1;j<=100;j++)
                {
                    if(dp[k][i][j]<INF)
                    {
                        if(np=='O')
                        {
                            int mindist=myabs(np1-i)+1;
                            for(int nj=max(1,j-mindist);nj<=min(j+mindist,100);nj++)
                                dp[k+1][np1][nj]=min(dp[k+1][np1][nj],dp[k][i][j]+mindist);
                        }
                        else
                        {
                            int mindist=myabs(np1-j)+1;
                            for(int ni=max(1,i-mindist);ni<=min(i+mindist,100);ni++)
                                dp[k+1][ni][np1]=min(dp[k+1][ni][np1],dp[k][i][j]+mindist);
                        }
                    }
                }
        }
        int ans=INF;
        for(int i=1;i<=100;i++)
            for(int j=1;j<=100;j++)
            {
                ans=min(ans,dp[n][i][j]);
                //cout<<ans<<" "<<i<<" "<<j<<endl;
            }

        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
