#include<stdio.h>
#include<cmath>
#include<iostream.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cases,ii,i,n;
    double x,y,z,vx,vy,vz,tx,ty,tz,tvx,tvy,tvz,d,t;
    //long double x,y,z,vx,vy,vz,tx,ty,tz,tvx,tvy,tvz,d,t;
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d",&n);
        x=y=z=0;
        vx=vy=vz=0;
        for(i=1;i<=n;i++)
        {
            //scanf("%lf%lf%lf%lf%lf%lf",&tx,&ty,&tz,&tvx,&tvy,&tvz);
            cin >> tx >> ty >> tz >> tvx >> tvy >> tvz;
            //x+=tx/n;y+=ty/n;z+=tz/n;
            //vx+=tvx/n;vy+=tvy/n;vz+=tvz/n;
            x+=tx;y+=ty;z+=tz;
            vx+=tvx;vy+=tvy;vz+=tvz;
        }
        x/=n;y/=n;z/=n;
        vx/=n;vy/=n;vz/=n;
        // (x+vx*t,y+vy*t,z+vz*t)
        // vx*x + vy*y +vz*z = 0
        // vx*(x+vx*t) + vy*(y+vy*t) + vz*(z+vz*t) = 0
        // vx*x+ vx*vx*t + vy*y+vy*vy*t + vz*z + vz*vz+t = 0
        if(vx==0 && vy==0 && vz==0)t=0;
        else t=-(vx*x + vy*y + vz*z)/(vx*vx+vy*vy+vz*vz);
        
        fprintf(stderr,"case %d t=%lf  (%lf,%lf,%lf)\n",ii,t,x,y,z);
        if(t<0)t=0;
        d=sqrt((x+vx*t)*(x+vx*t)+(y+vy*t)*(y+vy*t)+(z+vz*t)*(z+vz*t)>?0);
        double dd=d, tt=t;
        printf("Case #%d: %.8lf %.8lf\n",ii,dd+1e-6,tt+1e-6);
        
    }
    fputs("END\n",stderr);
    while(1);
    return 0;
}
