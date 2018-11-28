#include<stdio.h>
int n,m,i,j,k,l,tt,t;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&tt);
    for (t=1;t<=tt;t++)
    {
        scanf("%d%d",&n,&m);
        k=1;m++;
        for (i=1;i<=n;i++) {k=k*2;}
        if ((m%k)==0) {printf("Case #%d: ON\n",t);} else {printf("Case #%d: OFF\n",t);}
    }
    return 0;
}
