#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;
const int maxn=10005;
int d[maxn], n, len, l[maxn], dp[maxn];
int getmin(int x, int y){
    return x<y?x:y;
}
bool dfs(int x, int r, int id){ //x->loc , r->lenth
    if(x+r>=len)return true;
    if(dp[id]>=r)return false;
    dp[id]=r;
    int i, t;
    for(i=id+1; i<n; i++){
        if(d[i]-x>r)break;
        t=getmin(d[i]-x, l[i]);
        if(dfs(d[i], t, i))return true;
    }
    return false;
}
int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T, i, cas=1;
    scanf("%d", &T);
    while(T--){
        memset(dp, 0, sizeof(dp));
        scanf("%d", &n);
        for(i=0; i<n; i++)
        scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &len);
        if(dfs(d[0], d[0], 0))
            printf("Case #%d: YES\n", cas++);
        else printf("Case #%d: NO\n", cas++);
    }
    return 0;
}
