#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
#define inf (1<<30)
#define S 105
int v[S],t,txt,n,s,dp[S][S],p,tot;
bool U[S][S];
int doit(int a, int b){
    if(a == 0){
        if(b == 0)return 0;
        return -inf;
    }
    int &ret = dp[a][b];
    if(U[a][b])return ret;
    U[a][b] = true;

    ret = -inf;
    int lim = v[a] / 3;
    int ex = 2;
    for(int i = lim - ex; i <= lim + ex; ++i)for(int j = lim - ex; j <= lim + ex; ++j)for(int k = lim - ex; k <= lim + ex; ++k){
        if(i < 0 || j < 0 || k < 0)continue;
        if(i > 10 || j > 10 || k > 10)continue;
        if(i + j + k != v[a])continue;
        int mx = max(k,max(i,j));
        int mn = min(k,min(i,j));
        if(mx - mn > 2)continue;
        int r = -inf;
        int added = 0;
        if(mx >= p)added = 1;
        if(mx - mn == 2 && b > 0)r = doit(a - 1, b - 1) + added;
        else if(mx - mn < 2) r = doit(a - 1, b) + added;
        ret = max(ret , r);
    }
    return ret;
}
int main(){
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
	while(t--){
        memset(U, 0, sizeof U);
        scanf("%d%d%d",&n,&s,&p);
        for(int i = 1; i <= n; ++i)scanf("%d",&v[i]);
        int ans = doit(n,s);
        ans = max(ans,0);
        printf("Case #%d: %d\n",++txt,ans);
	}
    return 0;
}
