#include<stdio.h>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;

const int N=1000;
int x[N],y[N],n;

bool cmp(int u,int v)
{
     if (u>v) return 1;
     return 0;
}
int main()
{
    long long ans,s;
    int i,j,k,t=1,test;
    freopen("Alarge.in.txt","r",stdin);
    freopen("Alarge.out","w",stdout);
    scanf("%d",&test);
    while (t<=test)
    {
          scanf("%d",&n);
          for (i=0;i<n;i++) scanf("%d",x+i);
          for (i=0;i<n;i++) scanf("%d",y+i);
          sort(x,x+n);
          sort(y,y+n,cmp);
          for (i=ans=0;i<n;i++) ans+=(long long)x[i]*(long long)y[i];
          printf("Case #%d: %I64d\n",t++,ans);
    }
    return 0;
}
