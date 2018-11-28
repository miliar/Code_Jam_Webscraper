#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
int a[101];
int main()
{
  int T;
  scanf("%d",&T);
  for(int TC=1;TC<=T;++TC)
  {
    int x,s,r,t,n;
    scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
    memset(a,0,sizeof a);
    a[0]=x;
    while(n--)
    {
      int b,e,w;
      scanf("%d%d%d",&b,&e,&w);
      a[w]+=e-b;
      a[0]-=e-b;
    }
    double ans=0;
    int i=0;
    for(;i<101&&ans+(double)a[i]/(i+r)<=t;++i)
      ans+=(double)a[i]/(i+r);
    if(i<101)
    {
      ans=t+(a[i]-(i+r)*(t-ans))/(i+s);
      for(++i;i<101;++i)
        ans+=(double)a[i]/(i+s);
    }
    printf("Case #%d: %.9lf\n",TC,ans);
  }
  return 0;
}
