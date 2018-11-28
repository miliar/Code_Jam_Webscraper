#include<iostream>
#include<cmath>

using namespace std;

    int x[10],y[10],r[10];
    int n;

double dist(int x,int y,int x2, int y2)
{
   double a = x - x2;
   double b = y - y2;
return sqrt(a*a+b*b);
}
void solve()
{
    int i, j;

    scanf("%d", &n);
    for(i = 0; i < n; ++i)
    {
     scanf("%d%d%d",&x[i],&y[i],&r[i]);
    }

    double ans = 0;
    for(i = 0; i < n; ++i)
    {
     ans = max(ans, (double)r[i]);
    }
    if(n<=2)printf("%lf\n",ans);
    else
    {
     ans = 1e100;
     ans = min(ans,max((dist(x[0],y[0],x[1],y[1])+r[0]+r[1])/2.0,(double)r[2]));
     ans = min(ans,max((dist(x[0],y[0],x[2],y[2])+r[0]+r[2])/2.0,(double)r[1]));
     ans = min(ans,max((dist(x[1],y[1],x[2],y[2])+r[1]+r[2])/2.0,(double)r[3]));
     printf("%lf\n",ans);
    }
}
int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i)
    {
     printf("Case #%d: ",i+1);
     solve();
    }
return 0;
}