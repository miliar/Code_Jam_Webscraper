#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN=100000;
int tot,num,n;
int a[MAXN];

int gcd(int x,int y)
{
    if (y==0)   return x;
    else   return gcd(y,x%y);
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ou.txt","w",stdout);
    scanf("%d",&tot);
    while (tot--)
      {
        ++num;
        printf("Case #%d: ",num);
        scanf("%d",&n);
        for (int i=0;i<n;++i)
          {
            scanf("%d",&a[i]);
            if (i>0)
              {
                if (a[i-1]>a[i])  a[i-1]=a[i-1]-a[i];
                else   a[i-1]=a[i]-a[i-1];
              }
          }
        int tmp=0;
        for (int i=0;i<n-1;++i)
          tmp=gcd(tmp,a[i]);
        if (a[n-1]%tmp==0)   tmp=0;
        else   tmp=tmp-a[n-1]%tmp;
        printf("%d\n",tmp);
      }
}
        
