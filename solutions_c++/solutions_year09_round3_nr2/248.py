#include <stdio.h>
#include <math.h>
int main(){
    freopen("B-large.in","rt",stdin);
    freopen("B-large.out","wt",stdout);
    int t,n,i,j;
    double dmin,tmin;
    double vx,vy,vz,x,y,z,svx,svy,svz,sx,sy,sz;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d",&n);
        svx=svy=svz=sx=sy=sz=0;
        for(j=0;j<n;j++){
            scanf("%lf %lf %lf %lf %lf %lf",&x,&y,&z,&vx,&vy,&vz);
            sx+=x;
            sy+=y;
            sz+=z;
            svx+=vx;
            svy+=vy;
            svz+=vz;
        }
        sx/=n;
        sy/=n;
        sz/=n;
        svx/=n;
        svy/=n;
        svz/=n;
        if(svx*svx+svy*svy+svz*svz==0)tmin=0;
        else tmin=(-sx*svx-sy*svy-sz*svz)/(svx*svx+svy*svy+svz*svz);
        if(tmin<0)tmin=0;
        dmin=sqrt((sx+svx*tmin)*(sx+svx*tmin)+(sy+svy*tmin)*(sy+svy*tmin)+(sz+svz*tmin)*(sz+svz*tmin));
        printf("Case #%d: %.8lf %.8lf\n",i+1,dmin,tmin);
    }
}
