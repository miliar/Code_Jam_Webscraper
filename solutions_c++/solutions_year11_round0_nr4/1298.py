#include<stdio.h>
int a[1024],d[1024],e[1024];
void f(int x,int y){
    while(x!=d[x])x=d[x];
    while(y!=d[y])y=d[y];
    if(x!=y){
        d[x]=y;
        e[y]+=e[x];
    }
}
main(){
    freopen("Db.in","r",stdin);
    freopen("Db.out","w",stdout);
    int T,t=0,i,n,an;
    scanf("%d",&T);
    while(T--){
        an=0;
        t++;
        scanf("%d",&n);
        for(i=1;i<=n;i++){
            scanf("%d",&a[i]);
            d[i]=i;
            e[i]=1;
        }
        for(i=1;i<=n;i++)f(i,a[i]);
        for(i=1;i<=n;i++){
            if(d[i]==i){
                if(e[i]!=1){an+=e[i];}
            }
        }
        printf("Case #%d: %.6lf\n",t,1.*an);
    }
}
