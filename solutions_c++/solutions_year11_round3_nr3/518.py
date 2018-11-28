#include<stdio.h>

int main() {
    int c,cnt,f[10000],h,i,j,k,l,n,ok,t;
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++) {
        scanf("%d %d %d",&n,&l,&h);
        for(i=0;i<n;i++)scanf("%d",&f[i]);
        ok=0;
        for(i=l;i<=h;i++) {
            ok=1;
            for(j=0;j<n;j++) {
                if((f[j]%i)&&(i%f[j]))ok=0;
            }
            if(ok){ok=i;break;}
        }
        printf("Case #%d: ",cnt);
        if(ok)printf("%d",ok);
        else printf("NO");
        printf("\n");
    }
    return 0;
}
