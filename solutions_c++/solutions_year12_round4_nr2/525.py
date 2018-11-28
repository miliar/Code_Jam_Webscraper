#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#define N 1500
using namespace std;
int w,l,r[N];
double x[N],y[N];
int n;
int dblcmp(typec d)
{
    if (fabs(d)<eps)
       return 0;
    return (d>0)?1:-1;
}
double get1()
{
    double  tt=0;
    for (int i=1;i<=10;i++)
    {
        tt=tt/10.0+double(rand()%10);
        return tt/10.0;
    }
}
void sf()
{
     for (int i=1;i<=n;i++)
     {
         x[i]=get1()*w;
         y[i]=get1()*l;
     }
}
int check()
{
    for (int i=1;i<=n;i++)
         for (int j=i+1;j<=n;j++)
             if (cmp(sqr(x[i]-x[j])+sqr(y[i]-y[j])-sqr(r[i]+r[j]))<=0)
             return 0;
     return 1;
}
int main()
{
    cin>>T;
    for (int ttt=1;ttt<=T;ttt++)
    {
        cin>>n>>w>>l;
        for (int k=1;k<=n;k++)
        {
             scanf("%d",&r[k]);
        }
        sort(r+1,r+1+n);
        for (int k=1;k<=n;k++)
        {

        }
        while (!check());
         printf("Case #%d:",ttt);
         for (int i=1;i<=n;i++i)
             printf(" %.5f %.5f",x[i],y[i]);
         printf("\n");
    }
    return 0;
}
