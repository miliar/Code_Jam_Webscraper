#include <iostream>
#include <cmath>

using namespace std;

int x[512],y[512],z[512],vx[512],vy[512],vz[512];
double gx,gy,gz,vgx,vgy,vgz;

int main()
{
    int nt;
    int n;
    scanf("%d",&nt);
    for(int ii=1;ii<=nt;ii++)
    {
        scanf("%d",&n);
        memset(x,0,sizeof(x));
        memset(y,0,sizeof(y));
        memset(z,0,sizeof(z));
        memset(vx,0,sizeof(vx));
        memset(vy,0,sizeof(vy));
        memset(vz,0,sizeof(vz));
        gx=gy=gz=vgx=vgy=vgz=0;
        for(int j=0;j<n;j++)
        {
            scanf("%d %d %d %d %d %d",&x[j],&y[j],&z[j],&vx[j],&vy[j],&vz[j]);
            gx+=x[j];
            gy+=y[j];
            gz+=z[j];
            vgx+=vx[j];
            vgy+=vy[j];
            vgz+=vz[j];
        }
        gx/=n;
        gy/=n;
        gz/=n;
        vgx/=n;
        vgy/=n;
        vgz/=n;
        if(vgx*vgx+vgy*vgy+vgz*vgz==0)
        {
            printf("Case #%d: %.8lf %.8lf\n",ii,
                sqrt( (gx)*(gx)+(gy)*(gy)+(gz)*(gz)),0);
        }
        else
        {
            double v= 2*(vgx*gx+vgy*gy+vgz*gz);
            v*=-1;
            v/= (2*(vgx*vgx+vgy*vgy+vgz*vgz));
            double t;
            if(v<0) t=0;
            else t=v;
            printf("Case #%d: %.8lf %.8lf\n",ii,
                sqrt( (gx+vgx*t)*(gx+vgx*t)+(gy+vgy*t)*(gy+vgy*t)+(gz+vgz*t)*(gz+vgz*t)),t);
        }
    }
    return 0;
}
