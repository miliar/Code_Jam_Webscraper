#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int dp[105][105];

int main(){
    int cs,n,m,v,c;
    scanf("%d",&cs);
    for(int no=1;no<=cs;no++){
        scanf("%d%d%d",&n,&m,&v);
        memset(dp,192,sizeof(dp));
        for(int i=dp[0][0]=0;i<n;i++){
            scanf("%d",&c);
            for(int j=0;j<=m;j++){
                for(int x=0;x<=10;x++) for(int y=0;y<=x;y++){
                    int z=c-y-x;
                    if(z<0 || z>y || x-z>2) continue;
                    int& now=dp[i+1][j+(x-z==2)];
                    now=max(now,dp[i][j]+(x>=v));
                }
            }
        }
        printf("Case #%d: %d\n",no,dp[n][m]);
    }
}
