#include <iostream>
const int maxn=1001;
int a[maxn],f[maxn],g[maxn],r,k,n,cc,ci,ans,next[maxn];
int main()
{
    int i,j,l,h,p,q;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&cc);
    for (ci=1;ci<=cc;ci++)
    {
        memset(g,0,sizeof(g));
        memset(a,0,sizeof(a));
        memset(f,0,sizeof(f));
        scanf("%d %d %d",&r,&k,&n);
        for (i=1;i<=n;i++) 
        {
            scanf("%d",g+i);
            next[i]=i+1;
        }
        next[n]=1;
        ans=0;
        i=0;
        l=k;
        j=1;
        while (1)
        {
              q=j;
              while (l>=g[j])
              {
                    ans+=g[j];
                    l-=g[j];
                    j=next[j];
                    if (j==q) break;
              }
              i++;
              l=k;
              if (a[j]) break;
              a[j]=i;
              f[j]=ans;
              if (i==r) break;
        }
        if (i<r)
        {
        h=i-a[j];
        l=ans-f[j];
        p=(r-i)/h;
        ans+=p*l;
        i+=p*h;
        l=k;
        }
        while (i<r)
        {
              while (l>=g[j])
              {
                    ans+=g[j];
                    l-=g[j];
                    j=next[j];
              }
              i++;
              l=k;
              if (i==r) break;
        }
        printf("Case #%d: %d\n",ci,ans);
    }
}
