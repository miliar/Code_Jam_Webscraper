#include<iostream>
#include<stdio.h>
#include<cmath>
#include<algorithm>
using namespace std;
int main()
{
    FILE *p,*in;
    p=fopen("out.txt","w");
    in=fopen("B-small-attempt4.in","r");
    int i,t,x,y,z,vx,vy,vz,sumx,sumy,sumz,sumvx,sumvy,sumvz,n,count=1;
    double cx,cy,cz,px,py,pz,mut,time,pc,cvx,cvy,cvz;
    fscanf(in,"%d",&t);
    while(t--)
    {
        fscanf(in,"%d",&n);
        sumx=0;sumy=0;sumz=0;sumvx=0;sumvy=0;sumvz=0;
        for(i=0;i<n;i++)
        {
            fscanf(in,"%d%d%d%d%d%d",&x,&y,&z,&vx,&vy,&vz);
            sumx+=x;
            sumy+=y;
            sumz+=z;
            sumvx+=vx;
            sumvy+=vy;
            sumvz+=vz;
            //fprintf(p,"%d %d %d %d %d %d\n",sumx,sumy,sumz,sumvx,sumvy,sumvz);
        }
        
        cx=sumx/(1.0*n);
        cy=sumy/(1.0*n);
        cz=sumz/(1.0*n);
        cvx=sumvx/(1.0*n);
        cvy=sumvy/(1.0*n);
        cvz=sumvz/(1.0*n);
        //fprintf(p,"%lf %lf %lf %lf %lf %lf\n",cx,cy,cz,cvx,cvy,cvz);
        mut=cvx*cvx+cvy*cvy+cvz*cvz;
        if(mut<0.0000001)
        {
            pc=pow(cx*cx+cy*cy+cz*cz,0.5);
            time=0;
            fprintf(p,"Case #%d: %lf %lf\n",count++,pc,time);
            continue;
        }
        
        px=(cx*cvy*cvy-cy*cvx*cvy+cx*cvz*cvz-cz*cvx*cvz)/mut;
        py=(cy*cvx*cvx-cx*cvy*cvx+cy*cvz*cvz-cz*cvy*cvz)/mut;
        pz=(cz*cvx*cvx-cx*cvz*cvx+cz*cvy*cvy-cy*cvz*cvy)/mut;
        pc=pow(px*px+py*py+pz*pz,0.5);
        if(abs(cvx)>0.0000001) time=(px-cx)/cvx;
        else if(abs(cvy)>0.0000001) time=(py-cy)/cvy;
        else time=(pz-cz)/cvz;
        if(time<0)
        {
            pc=pow(cx*cx+cy*cy+cz*cz,0.5);
            time=0;
            fprintf(p,"Case #%d: %lf %lf\n",count++,pc,time);
            continue;
        }
        fprintf(p,"Case #%d: %lf %lf\n",count++,pc,time);
    }
    return 0;
}
            
