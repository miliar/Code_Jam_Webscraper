
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;

const int N=510;
int w[N][N];
double a[N][N];
double b[N][N];
double c[N][N];
int m,n,d;
const double eps=1e-3;

double get1(int x1,int y1,int x2,int y2)
{
    return a[x2][y2]-a[x1-1][y2]-a[x2][y1-1]+a[x1-1][y1-1];
}

double get2(int x1,int y1,int x2,int y2)
{
    return b[x2][y2]-b[x1-1][y2]-b[x2][y1-1]+b[x1-1][y1-1];
}

double get3(int x1,int y1,int x2,int y2)
{
    return c[x2][y2]-c[x1-1][y2]-c[x2][y1-1]+c[x1-1][y1-1];
}

bool check(int x1,int y1,int k)
{
    int i,j;
    double x=(2*x1+k)/2.0,y=(2*y1+k)/2.0;
    double s1=get1(x1,y1,x1+k-1,y1+k-1),s2=get2(x1,y1,x1+k-1,y1+k-1);
double tm=get3(x1,y1,x1+k-1,y1+k-1);
    for(i=x1;i<=x1+k-1;i+=k-1)
     for(j=y1;j<=y1+k-1;j+=k-1)
     {
         s1-=(i+0.5)*w[i][j];
         s2-=(j+0.5)*w[i][j];
         tm-=w[i][j];
     }
     s1-=x*tm;
     s2-=y*tm;
     return fabs(s1)<eps&&fabs(s2)<eps;
}

int f()
{
    int k,i,j;
        for(k=min(m,n);k>=3;k--)
        {
            for(i=1;i+k-1<=m;i++)
             for(j=1;j+k-1<=n;j++) if(check(i,j,k)) return k;
        }
        return -1;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
   int i,j,t;
   int cs=0;
   scanf("%d",&t);
   while(t--)
   {
       scanf("%d%d%d",&m,&n,&d);
       for(i=1;i<=m;i++)
        for(j=1;j<=n;j++) scanf("%1d",&w[i][j]);
        for(i=0;i<=m;i++)
         for(j=0;j<=n;j++) a[i][j]=b[i][j]=c[i][j]=0;
        for(i=1;i<=m;i++)
          for(j=1;j<=n;j++)
           {
               a[i][j]=a[i][j-1]+(i+0.5)*w[i][j];
               b[i][j]=b[i][j-1]+(j+0.5)*w[i][j];
               c[i][j]=c[i][j-1]+w[i][j];
           }
        for(i=1;i<=m;i++)
          for(j=1;j<=n;j++)
           {
               a[i][j]+=a[i-1][j];
               b[i][j]+=b[i-1][j];
               c[i][j]+=c[i-1][j];
           }



        printf("Case #%d: ",++cs);
        int ans=f();

        if(ans>=3) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
   }
   return 0;
}


