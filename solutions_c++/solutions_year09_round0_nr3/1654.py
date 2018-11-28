#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;
vector<int > ans;
int dp[19];
char s[25]="welcome to code jam";
char ss[550];
void find(int v)
{
     int i;
     ans.clear();
     for(i=0;i<19;i++)
     if(ss[v]==s[i])
     ans.push_back(i);
}
int n;
int main()
{
    int i,j,k;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d\n",&n);
    for(i=1;i<=n;i++)
    {
                     gets(ss);
                     memset(dp,0,sizeof(dp));
                     for(k=0;k<strlen(ss);k++)
                     {
                                              find(k);
                                              for(j=0;j<ans.size();j++)
                                              if(ans[j]==0)
                                              dp[ans[j]]=(dp[ans[j]]+1)%10000;
                                              else dp[ans[j]]=(dp[ans[j]]+dp[ans[j]-1])%10000;
                     }
                     printf("Case #%d: %04d\n",i,dp[18]);
    }
    return 0;
}
                     

