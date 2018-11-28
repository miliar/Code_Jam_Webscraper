#include<stdio.h>
#include<algorithm>
using namespace std;
#define MAX 2000000000
main(){
    freopen("Cb.in","r",stdin);
    freopen("Cs.out","w",stdout);
    int mi,i,sum,xo,t=0,T,n,x;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d",&n);
        mi=MAX;
        sum=0;
        xo=0;
        for(i=0;i<n;i++){
            scanf("%d",&x);
            xo^=x;
            sum+=x;
            mi=min(mi,x);
        }
        printf("Case #%d: ",t);
        if(xo)puts("NO");
        else printf("%d\n",sum-mi);
    }
}
