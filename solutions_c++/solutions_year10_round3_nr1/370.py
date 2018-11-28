#include<iostream>
#include<cstdio>
using namespace std;

int a[1024],b[1024],n,i,j,t,ans,bla;

int main()
{
    scanf("%d",&t);
    for(;t;t--)
    {
        bla++;
        scanf("%d",&n);
        for(i=0;i<n;i++)
         scanf("%d%d",&a[i],&b[i]);
        ans=0;
        for(i=0;i<n;i++)
         for(j=i+1;j<n;j++)
          if((a[i]>a[j]&&b[i]<b[j])||(a[i]<a[j]&&b[i]>b[j]))ans++;
        printf("Case #%d: %d\n",bla,ans);
    }
}
