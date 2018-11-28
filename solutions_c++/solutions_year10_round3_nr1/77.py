#include <iostream>
int a[2][1000],n,m,t,i,j,k,cc;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d\n",&t);
    for (cc=1;cc<=t;cc++)
    {
        scanf("%d\n",&n);
        for (i=0;i<n;i++) scanf("%d %d\n",&a[0][i],&a[1][i]);
        m=0;
        for (i=0;i<n;i++)
            for (j=i+1;j<n;j++)
            if ((a[0][i]-a[0][j])*(a[1][i]-a[1][j])<0) m++;
        printf("Case #%d: %d\n",cc,m);
    }
}
