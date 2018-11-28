#include<stdio.h>
int a[2000];
int main()
{
    freopen("c:\\B-small-attempt0.in","r",stdin);
    freopen("c:\\output.txt","w",stdout);
    int nn,cost;
    scanf("%d",&nn);
    for (int ii=1;ii<=nn;ii++) {
        printf("Case #%d: ",ii);
        int p,n=1;
        scanf("%d",&p);
        int ans=0;
        for (int i=1;i<=p;i++) n*=2;
        for (int i=1;i<=n;i++) scanf("%d",a+i);
        for (int i=1;i<n;i++) scanf("%d",&cost);
        for (int k=1;k<=p;k++) {
            for (int i=1;i<=n;i+=2) {
                a[(i+1)/2]=a[i]<a[i+1]?a[i]:a[i+1];
            }
            n/=2;
            for (int i=1;i<=n;i++) if (a[i]==0) {ans++;a[i]=1;}
            for (int i=1;i<=n;i++) a[i]--;
        }
        printf("%d\n",ans*cost);
    }
}