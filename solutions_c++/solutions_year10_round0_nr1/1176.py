#include<stdio.h>

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,n,k,j;
    scanf("%d",&t);
    for(j=1;j<=t;++j){
        scanf("%d%d",&n,&k);
        int i=0;
        for(;i<n;++i){
            if(k%2!=1)break;
            k/=2;
        }
        if(i>=n)printf("Case #%d: ON\n",j);
        else printf("Case #%d: OFF\n",j);
    }
}
