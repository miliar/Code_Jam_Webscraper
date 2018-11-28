#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define eps 1e-8
using namespace std;
int n,to[1001];
double w,l,r[1001],sv[1001],x[1001],y[1001];
bool hash[1001];
inline double dis(double x,double y)
{
       return x*x+y*y;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,qq;
    int i,j;
    scanf("%d",&test);
    for(qq=1;qq<=test;qq++)
    {
      printf("Case #%d:",qq);
      scanf("%d%lf%lf",&n,&w,&l);
      for(i=1;i<=n;i++)scanf("%lf",&r[i]);
      memcpy(sv,r,sizeof(sv));
      sort(&r[1],&r[n]+1);
      x[1]=0;
      y[1]=0;
      for(i=2;i<=n;i++)
      {
        x[i]=x[i-1];
        y[i]=y[i-1]+r[i]+r[i-1];
        if(y[i]-eps>l)
        {
          x[i]=0;
          y[i]=0;
        }
        for(j=1;j<i;j++)
        {
                        if(i==9&&j==2)
                        printf("");
          if((x[i]-x[j])*(x[i]-x[j])<(r[i]+r[j])*(r[i]+r[j])-(y[i]-y[j])*(y[i]-y[j]))
            x[i]=sqrt((r[i]+r[j])*(r[i]+r[j])-(y[i]-y[j])*(y[i]-y[j]))+x[j]+eps;
        }
      }
      memset(hash,0,sizeof(hash));
      for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
          if(fabs(sv[i]-r[j])<eps&&hash[j]==0)
          {
            to[i]=j;
            hash[j]=1;
            break;
          }
      for(i=1;i<=n;i++)printf(" %.10lf %.10lf",x[to[i]],y[to[i]]);
      printf("\n");
    }
}
