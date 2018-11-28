#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

map<pair<int,int>, int> dp;

int K[102], koidy, cells;

int F(int u, int v)
{
    if(v <= u) return 0;
    
    pair<int,int> p = make_pair(u,v);
    
    if(dp.find(p)!=dp.end())
    return dp[p];
    
    int ans = 1 << 30;
    
    for(int i = 0; i < koidy; ++i)
    {
        if(K[i] >= u && K[i] <= v)
        {
            ans = min(ans, v-u + F(u,K[i]-1) + F(K[i]+1,v) );
        }   
    }   
    
    if(ans == 1 << 30) ans = 0;
    
    return dp[p] = ans;
}

int main()
{
    freopen("C_large.in","r",stdin);
    freopen("C_large.out","w",stdout);
    
    int T;
    
    scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        dp.clear();
        scanf("%d%d",&cells,&koidy);   
        for(int i = 0; i < koidy; ++i)
        {
            scanf("%d",K+i);   
        }
        int ans = F(1,cells);
        printf("Case #%d: %d\n",t,ans);
    }
    
    return 0;    
}
