#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#define INF (1<<30)
#define MAXN 100005
using namespace std;

int a,b;
double p[MAXN],w[MAXN],ty,en;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a2.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while (T--)
    {
          int i,j;
          double x=1,tmp;
          scanf("%d%d",&a,&b);
          for (i=1;i<=a;i++) scanf("%lf",&p[i]) , w[i]=0;
          ty=en=0;
          for (i=1;i<=a;i++)
          {
              tmp=x*(1-p[i]);
              ty+=(b-a+1+b+1)*tmp;
              en+=(1+b+1)*tmp;
              for (j=1;j<=a;j++)
                  if (a-j<i)
                     w[j]+=(j+j+b-a+1)*tmp;
                  else
                      w[j]+=(j + b-(a-j) +1 +b+1)*tmp;
              x*=p[i];
          }
          ty+=(b-a+1)*x;
          en+=(1+b+1)*x;
          for (j=1;j<=a;j++)
              if (a-j<i)
                 w[j]+=(j+j+b-a+1)*x;
              else
                  w[j]+=(j + b-(a-j) +1 +b+1)*tmp;
          double ans=ty;
          ans=min(ans,en);
          for (i=1;i<=a;i++)
          {
              ans=min(ans,w[i]);
              //printf("%.4lf\n",w[i]);
          }
          printf("Case #%d: %.6lf\n",++cas,ans);
    }
    //system("pause");
}
