#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#define MAXN 512
using namespace std;
int N,T;
int x[MAXN],y[MAXN],z[MAXN];
int vx[MAXN],vy[MAXN],vz[MAXN];
int sumx,sumvx,sumy,sumvy,sumz,sumvz;
int main()
{
    int i,j,k;
    scanf("%d",&T);
    for(k=0;k<T;++k)
    {
        scanf("%d",&N);
        printf("Case #%d: ",k+1);
        sumx=0;sumy=0;sumz=0;sumvx=0;sumvy=0;sumvz=0;
        for(i=0;i<N;++i)
        {
            scanf("%d %d %d %d %d %d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
            sumx+=x[i];sumy+=y[i];sumz+=z[i];
            sumvx+=vx[i];sumvy+=vy[i];sumvz+=vz[i];
        }
        // At moment t=0
        double cx0=sumx/(double)N;
        double cy0=sumy/(double)N;
        double cz0=sumz/(double)N;
        // At moment t=1
        double cx=(sumx+sumvx)/(double)N;   
        double cy=(sumy+sumvy)/(double)N;
        double cz=(sumz+sumvz)/(double)N;
        double a=cx-cx0,b=cy-cy0,c=cz-cz0;
        if(a*a+b*b+c*c==0)
        {
            double dt=sqrt(cx0*cx0+cy0*cy0+cz0*cz0);
            printf("%.8lf %.8lf\n",dt,0);
            continue;
        }
        double mt=-(a*cx0+b*cy0+c*cz0)/(double)(a*a+b*b+c*c);
        if(mt<0)mt=0;
        double xt=cx0+mt*a,yt=cy0+mt*b,zt=cz0+mt*c;
        double dt=sqrt(xt*xt+yt*yt+zt*zt);
        printf("%.8lf %.8lf\n",dt,mt);
    }
    return 0;
}
