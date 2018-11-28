#include<stdio.h>
#include<math.h>
int x[10],y[10],r[10],n;
double sqr(double x)
{
    return x*x;
}
double getdis(int i,int j)
{
    return sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]));      
}
void init()
{
    int i;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
        scanf("%d%d%d",&x[i],&y[i],&r[i]);
    
}
double max(double x,double y)
{
    if(x>y) return x;
    return y;
}
double min(double x,double y)
{
    if(x<y) return x;
    return y;
}
double work()
{
    if(n==1) return r[1];
    if(n==2) return max(r[1],r[2]);
    double r1=max(r[3],(getdis(1,2)+r[1]+r[2])/2);
    double r2=max(r[2],(getdis(1,3)+r[1]+r[3])/2);
    double r3=max(r[1],(getdis(2,3)+r[2]+r[3])/2);
    return min(r1,min(r2,r3));
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ncase,nc;
    scanf("%d",&ncase);
    for(nc=1;nc<=ncase;nc++)
    {
        init();
        printf("Case #%d: ",nc);
        printf("%.6lf\n",work());
    }
    return 0;
}