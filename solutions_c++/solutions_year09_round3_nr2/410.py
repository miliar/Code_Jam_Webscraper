#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <stdio.h>
using namespace std;

double x[505],y[505],z[505],vx[505],vy[505],vz[505];

int main()
{
    freopen("d:\\in.txt","r",stdin);
    freopen("d:\\out.txt","w",stdout);
    int T,cas,i,j,n;
    double px,py,pz,pvx,pvy,pvz,cx,cy,cz;
    double minD=1e100,minT;
    
    cin>>T;
    for (cas=1;cas<=T;cas++)
    {
        cin>>n;
        minD=1e100;
        px=py=pz=pvx=pvy=pvz=0.0;
        for (i=0;i<n;i++)
        {
            cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
            px+=x[i],py+=y[i],pz+=z[i];
            pvx+=vx[i],pvy+=vy[i],pvz+=vz[i];
        }
        px/=(n+0.0),py/=(n+0.0),pz/=(n+0.0);
        pvx/=(n+0.0),pvy/=(n+0.0),pvz/=(n+0.0);
        cx=px,cy=py,cz=pz;
        double r=100000.0,l=0.0,ll,rr;
        while (fabs(l-r)>1e-11)
        {
            ll=l+(r-l)/3,rr=r-(r-l)/3;
            px=cx+ll*pvx,py=cy+ll*pvy,pz=cz+ll*pvz;
            double fl=sqrt(px*px+py*py+pz*pz);
            px=cx+rr*pvx,py=cy+rr*pvy,pz=cz+rr*pvz;
            double fr=sqrt(px*px+py*py+pz*pz);
            if (fl>fr) l=ll;
            else r=rr;
        }
        px=cx+l*pvx,py=cy+l*pvy,pz=cz+l*pvz;
        minD=sqrt(px*px+py*py+pz*pz);
        minT=l;
        printf("Case #%d: %.8lf %.8lf\n",cas,minD,minT);
    }
    return 0;
}
