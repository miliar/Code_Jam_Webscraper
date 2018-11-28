#include<stdio.h>
#include<algorithm>
long long a[1000],b[1000];
int op(int x,int y) {return x>y;}
int main()
{
    int i,j,n,nn,ii;
    long long ans;
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        scanf("%d",&n);
        for (i=1;i<=n;i++) scanf("%I64d",a+i);
        for (i=1;i<=n;i++) scanf("%I64d",b+i);
        std::sort(a+1,a+n+1);
        std::sort(b+1,b+n+1,op);
        ans=0;
        for (i=1;i<=n;i++) ans+=a[i]*b[i];
        printf("Case #%d: %I64d\n",ii,ans);
    }
}
