#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

int main()
{
    int cases,ii,n,i,j,fa,fb;
    double x[42],y[42],r[42];
    double bl,bh,bm;
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        memset(r,0,sizeof(r));
        scanf("%d",&n);
        for(i=1;i<=n;i++)scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
        bl=0;bh=0;
        for(i=1;i<=n;i++)for(j=i+1;j<=n;j++)
        {
            //bh=max(bh,(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+r[i]+r[j]);           
            if(bh<=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+r[i]+r[j])
            {
                bh=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+r[i]+r[j];
                fa=i;
                fb=j;
            }
        }
        double an=bh;
        //fprintf(stderr,"an=%lf\n",an);
        double tt;
        if(n==1)an=r[1]*2;
        else if(n==2)
        {
            i=1;j=2;
            //an=sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))+r[i]+r[j];
            an=max(r[1],r[2])*2;
        }
        else
        {
        i=1;j=2;
        tt=sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))+r[i]+r[j];
        an=min(an,max(tt,r[3]));
        //fprintf(stderr,"an=%lf\n",an);
        i=2;j=3;
        tt=sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))+r[i]+r[j];
        //fprintf(stderr,"tt=%lf r[1]=%lf\n",tt,r[1]);
        an=min(an,max(tt,r[1]));
        //fprintf(stderr,"an=%lf\n",an);
        i=1;j=3;
        tt=sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))+r[i]+r[j];
        an=min(an,max(tt,r[2]));
        }
        //fprintf(stderr,"an=%lf\n",an);
        
        /*
        bh=sqrt(bh);
        fprintf(stderr,"bh=%lf\n",bh);
        double x1,y1,x2,y2;
        double dx=x[fb]-x[fa],dy=y[fb]-y[fa];
        while(bh-bl>1e-2)
        {
            bm=(bh+bl)/2;
            
            if(x[fa]<x[fb])x1=x[fa]-r[fa]*(dx/(dx+dy))+bm*(dx/(dx+dy));
            else x1=x[fa]+r[fa]*(dx/(dx+dy))+bm*(dx/(dx+dy));
            if(y[fa]<y[fb])y1=y[fa]-r[fa]*(dy/(dx+dy))+bm*(dx/(dx+dy));
            else y1=y[fa]+r[fa]*(dy/(dx+dy))+bm*(dx/(dx+dy));
            
            if(x[fb]<=x[fa])x2=x[fb]-r[fb]*(dx/(dx+dy))+bm*(dx/(dx+dy));
            else x2=x[fb]+r[fb]*(dx/(dx+dy))+bm*(dx/(dx+dy));
            if(y[fb]<=y[fa])y2=y[fb]-r[fb]*(dy/(dx+dy))+bm*(dx/(dx+dy));
            else y2=y[fb]+r[fb]*(dy/(dx+dy))+bm*(dx/(dx+dy));
            
            fprintf(stderr,"bm=%lf\n",bm);
            bool yes=1;
            for(i=1;i<=n;i++)
            {
                if(sqrt((x1-x[i])*(x1-x[i])+(y1-y[i])*(y1-y[i]))+r[i]>bm
                  && sqrt((x2-x[i])*(x2-x[i])+(y2-y[i])*(y2-y[i]))+r[i]>bm)
                  {
                        fprintf(stderr,"W %.1lf %.1lf    %.1lf %.1lf\n",sqrt((x1-x[i])*(x1-x[i])+(y1-y[i])*(y1-y[i])),r[i],sqrt((x2-x[i])*(x2-x[i])+(y2-y[i])*(y2-y[i])),r[i]);
                      yes=0;
                      break;
                    }
            }
            fprintf(stderr,"bm=%lf i=%d\n",bm,i);
            if(yes)bh=bm;
            else bl=bm;
        }
        */
        printf("Case #%d: %.6lf\n",ii,an/2);
    }
    
    fputs("END",stderr);
    while(1);
    return 0;
}
