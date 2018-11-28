#include<stdio.h>
int main(){
    freopen("D-large.in.txt","r",stdin);
    freopen("D-large.out","w",stdout);
    int kase,kases=1;
    scanf("%d",&kase);
    while(kase--){
        int ans=0,n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++){
            int v;
            scanf("%d",&v);
            if(i!=v)ans++;
        }
        printf("Case #%d: %.6f\n",kases++,(double)ans);
    }
    return 0;
}
