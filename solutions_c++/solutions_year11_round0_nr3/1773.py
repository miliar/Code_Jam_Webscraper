#include <stdio.h>
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,cs;
    scanf("%d",&t);
    for(cs=1;cs<=t;++cs){
        int i,v,n,sum=0,res=0;
        scanf("%d",&n);
        int mini=999999999;
        for(i=1;i<=n;++i){
            scanf("%d",&v);
            if(v<mini) mini=v;
            sum+=v;
            res^=v;
        }
        printf("Case #%d: ",cs);
        if(res) printf("NO\n");
        else printf("%d\n",sum-mini);
    }
    return 0;
}
