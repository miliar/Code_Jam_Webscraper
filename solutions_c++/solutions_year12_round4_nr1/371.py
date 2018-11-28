#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int a[12000][2];
bool bi[12000];
int dp[12000];
int n,m;

int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        scanf("%d",&n);
        for (int i=1;i<=n;++i) scanf("%d%d",&a[i][0],&a[i][1]);
        scanf("%d",&m);
        
//        int now=1,len=0;
        memset(dp,0,sizeof(dp));
        dp[1]=a[1][0];
        for (int i=1;i<=n;++i)
            if (dp[i]!=0){
                for (int j=i+1;j<=n;++j){
                    if (a[j][0]>a[i][0]+dp[i]) break;
                        dp[j]=max(dp[j],min(a[j][0]-a[i][0],a[j][1]));
                }
            }
        bool bi=false;
        for (int i=1;i<=n;++i)
            if (a[i][0]+dp[i]>=m) bi=true;
        if (bi) printf("Case #%d: YES\n",++cas);
        else printf("Case #%d: NO\n",++cas);
    }
    return 0;
}
            
