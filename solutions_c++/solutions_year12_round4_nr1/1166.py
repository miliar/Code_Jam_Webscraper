#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

int wei[10010],len[10010],f[10010],w,l,i,ans,T,n,goa;
int getmax(int aa,int bb) {
    if (aa>bb) return aa;
    return bb;
}
int getmin(int aa,int bb) {
    if (aa<bb) return aa;
    return bb;
}
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int tsum=1;tsum<=T;tsum++) {
        scanf("%d",&n);
        printf("Case #%d: ",tsum);
        for (i=1;i<=n;i++) scanf("%d%d",&wei[i],&len[i]);
        scanf("%d",&goa);
        for (i=1;i<=10010;i++) f[i]=0;
        f[1]=wei[1]; ans=0;
        for (i=1;i<=n;i++) {
            for (int j=i+1;j<=n && wei[j]-wei[i]<=f[i];j++) f[j]=getmax(f[j],getmin(wei[j]-wei[i],len[j]));
            ans=getmax(ans,f[i]+wei[i]);
        }
        if (ans>=goa) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

