#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#define N 10009
using namespace std;
int d[N],l[N],dp[N];
int main(){
    //freopen("in.in","r",stdin);
    //freopen("out.put","w",stdout);
    int T,n,cas=0,D;
    cin>>T;
    while(T--)
    {
        cin>>n;
        for(int i=0;i<n;i++) cin>>d[i]>>l[i];        
        cin>>D;
        memset(dp,0,sizeof(dp));
        dp[0]=2*d[0];
        int ans=0;
        for(int i=0;i<n;i++)
            if(dp[i]){
                for(int j=i+1;j<n&&d[j]<=dp[i];j++)
                    dp[j]=max(dp[j],d[j]+min(d[j]-d[i],l[j]));
                if(dp[i]>=D) ans=1;
            }        
        printf("Case #%d: ",++cas);
        if(!ans) puts("NO");
        else puts("YES");
    }
    //fclose(stdout);
}
