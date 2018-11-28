#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const string welcom="welcome to code jam";
int dp[501][30];

int main(int argc, char *argv[])
{
    int t,o;    freopen("E:/in.txt","r",stdin);
freopen("E:/out.txt","w",stdout);
    scanf("%d%d",&t);
    getchar();
    for(o=1;o<=t;o++)
    {
         char tmp[1001];
         gets(tmp);
         string s;
         s = tmp;
         memset(dp,0,sizeof(dp));
         
         int i,j,k,l = s.length();
         for(i=1;i<=l;i++)
         {
              if(s[i-1] == welcom[0]) dp[i][1] = dp[i-1][1] + 1;
              else dp[i][1] = dp[i-1][1];
         }
         
         for(i=2;i<=l;i++)
             for(j=2;j<=min(19,i);j++)
             {
                 if(s[i-1] == welcom[j-1]) dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
                 else dp[i][j] = dp[i-1][j];
             }
         cout<<"Case #"<<o<<": ";
         int ans = dp[l][19];
         if(ans < 1000)
         {
             if(ans >99) cout<<0<<ans<<endl;
             else if(ans <100 && ans >= 10) cout<<"00"<<ans<<endl;
             else cout<<"000"<<ans<<endl;
         }
    }
    return EXIT_SUCCESS;
}
