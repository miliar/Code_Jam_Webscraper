#include<iostream>
int a[20000];
int i,j,k,l,m,n,xys,ysc,h;
int main()
{
    freopen("c.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&ysc);
    for (xys=1;xys<=ysc;++xys){
        scanf("%d%d%d",&n,&l,&h);
        for (i=1;i<=n;++i) scanf("%d",&a[i]);
        for (i=l;i<=h;++i){
            int ok=1;
            for (j=1;j<=n;++j)
                if (i%a[j]!=0&&a[j]%i!=0){
                   ok=0;
                   break;
                }
            if (ok) break;
        }
        printf("Case #%d: ",xys);
        if (i<=h) printf("%d\n",i); else printf("NO\n");
    }
    return 0;
}
