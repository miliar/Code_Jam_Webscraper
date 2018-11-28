#include<iostream>
using namespace std;
const int maxn=1010;
int a[maxn],b[maxn],c[maxn],n,m;
int check(int x)
{
    m=0;
    int i,j,k;
    for (i=0;i<n;i++)
    {
        k=-1;
        for (j=0;j<m;j++)
            if (a[i]==b[j]+1)
            {
               if (k==-1) k=j;
               else
               if (c[j]<c[k]) k=j;
            }
        if (k!=-1)
        {
           b[k]++;
           c[k]++;
        }
        else
        {
            b[m]=a[i];
            c[m]=1;
            m++;
        }
    }
    for (i=0;i<m;i++)
    if (c[i]<x) return 0;
    return 1;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases,tt,l,r,mid,i;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a,a+n);
        l=0;
        r=n+1;
        while (l+1<r)
        {
              mid=(l+r)/2;
              if (check(mid)) l=mid;
              else r=mid;
        }
        printf("Case #%d: %d\n",tt+1,l);
    }
    return 0;
}
