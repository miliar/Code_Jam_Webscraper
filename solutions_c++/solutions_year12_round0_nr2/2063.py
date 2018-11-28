#include<stdio.h>
#include<algorithm>
using namespace std;
int n,s,p,a[101],ans;
inline bool cmp(int a,int b)
{
       return a>b;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,q,i,j,p1,p2;
    scanf("%d",&test);
    for(q=1;q<=test;q++)
    {
      scanf("%d%d%d",&n,&s,&p);
      if(p==0)p1=0;
      else p1=p*3-2;
      if(p==0)p2=0;
      else if(p==1)p2=1;
      else p2=p*3-4;
      for(i=1;i<=n;i++)scanf("%d",&a[i]);
      sort(&a[1],&a[n]+1,cmp);
      for(i=1;i<=n;i++)if(a[i]<p1)break;
      ans=i-1;
      for(j=1;i<=n&&j<=s;i++,j++)
        if(a[i]>=p2)ans++;
      printf("Case #%d: %d\n",q,ans);
    }
    return 0;
}
