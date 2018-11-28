#include<iostream>
using namespace std;
const int maxn=6000;
int test,t,i,j,k,n,a[maxn],x[maxn],y[maxn];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&test),t=1;t<=test;t++)
    {
        scanf("%d\n",&n);
        for (i=2;i<n;i++)
        {
            x[i]=i+1;
            y[i]=i-1;
        }
        x[1]=2;
        y[n]=n-1;
        x[n]=1;
        y[1]=n;
        x[0]=1;
        for (j=0,i=1;i<=n;i++)
        {
            for (k=0;k<i;k++) j=x[j];
            x[y[j]]=x[j];
            y[x[j]]=y[j];
            a[j]=i;
        }
        scanf("%d",&n);
        printf("Case #%d:",t);
        for (i=0;i<n;i++)
        {
            scanf("%d",&j);
            printf(" %d",a[j]);
        }
        printf("\n");
    }
    return 0;
}

