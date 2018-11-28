#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef long long ll;
const int maxn=1024;
const double ep=1e-8;
struct point{
    double x,y,z;
    double p;
}a[maxn];
int N;
double ans;

void input()
{
    int i;
    scanf("%d",&N);
    for(i=0;i<N;i++){
        scanf("%lf%lf%lf%lf",&a[i].x,&a[i].y,&a[i].z,&a[i].p);
    }   
}

double fabs(double x)
{
    if(x<0) return -x;
    return x;
}

double dist(point p1,point p2)
{
    return fabs(p1.x-p2.x)+fabs(p1.y-p2.y)+fabs(p1.z-p2.z);
}

double getmax(double a,double b)
{
    return a>b?a:b;
}

bool check(double ans)
{
    int i,j;
    double t;
    for(i=0;i<N;i++){
        for(j=i+1;j<N;j++){
            t=(a[i].p+a[j].p)*ans;
            if(t<dist(a[i],a[j])) return false;
        }
    }
    return true;
}

double solve()
{
    int i;
    double l,r,mid;
    for(l=r=0,i=0;i<N;i++){
        r=getmax(r,(fabs(a[i].x)+fabs(a[i].y)+fabs(a[i].z))/a[i].p);
    }
    while(l+ep<r){
        mid=(l+r)/2;
        if(check(mid)) r=mid;
        else l=mid;
    }
    return l;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,T;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        input();
        printf("Case #%d: ",i);
        printf("%.6lf\n",solve());
    }
    return 0;
}
