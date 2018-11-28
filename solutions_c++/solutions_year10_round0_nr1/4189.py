#include<stdio.h>
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,k,i;
    scanf("%d",&t);
    for (i=1;i<=t;i++){
        scanf("%d%d",&n,&k);
        n=1<<n;
        k%=n;
        if (n-1==k) printf("Case #%d: ON\n",i);else printf("Case #%d: OFF\n",i);
        }
}
