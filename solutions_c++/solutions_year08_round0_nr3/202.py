#include<stdio.h>
#include<string.h>
#include<math.h>

double f,R,t,r,g;

void input()
{
    scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g); 
}

double dist(double x1,double y1,double x2,double y2)
{
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

double intersectCycle(double x1,double y1,double x2,double y2)
{
    double l1,l2,l3;
    double ans;
    l1=dist(x1,y1,0,0);
    l2=dist(x2,y2,0,0);
    l3=dist(x1,y1,x2,y2);
    //printf("%lf\n",l3);
    ans=(R-t-f)*(R-t-f)*asin((l3/2)/(R-t-f));
    //printf("%lf\n",ans);
    ans=ans-fabs(x1*y2-y1*x2)/2;
    //printf("%.6lf %lf %lf %lf %lf\n",ans,x1,y1,x2,y2);
    return ans;
}

double intersectArea(double x1,double y1,double x2,double y2)
{
    int f1,f2;
    double tx1,tx2,ty1,ty2;
    double ans;
    if((x2*x2+y1*y1)>=(R-t-f)*(R-t-f)) f1=1;
    else f1=0;
    if((x1*x1+y2*y2)>=(R-t-f)*(R-t-f)) f2=1;
    else f2=0;
    if(f1==1 && f2==1){
        tx1=sqrt((R-t-f)*(R-t-f)-y1*y1);
        ty1=y1;
        tx2=x1;
        ty2=sqrt((R-t-f)*(R-t-f)-x1*x1);
        ans=(ty2-y1)*(tx1-x1)/2;
        ans+=intersectCycle(tx1,ty1,tx2,ty2);
        //printf("%lf %lf %lf %lf %lf\n",ans,tx1,ty1,tx2,ty2);
    }else if(f2==1){
        tx1=x2;
        ty1=sqrt((R-t-f)*(R-t-f)-x2*x2);
        tx2=x1;
        ty2=sqrt((R-t-f)*(R-t-f)-x1*x1);
        ans=(ty2-y1+ty1-y1)*(x2-x1)/2;
        ans+=intersectCycle(tx1,ty1,tx2,ty2);
    }else if(f1==1){
        tx1=sqrt((R-t-f)*(R-t-f)-y1*y1);
        ty1=y1;
        tx2=sqrt((R-t-f)*(R-t-f)-y2*y2);
        ty2=y2;
        ans=(tx1-x1+tx2-x1)*(y2-y1)/2;
        ans+=intersectCycle(tx1,ty1,tx2,ty2);
    }else{
        tx1=x2;
        ty1=sqrt((R-t-f)*(R-t-f)-x2*x2);
        tx2=sqrt((R-t-f)*(R-t-f)-y2*y2);
        ty2=y2;
        ans=(ty1-y1)*(x2-x1)+(x2-x1+tx2-x1)*(y2-ty1)/2;
        ans+=intersectCycle(tx1,ty1,tx2,ty2);
    }
    return ans;
}

double solve()
{
    double col,row,area,ans,trow,tcol;
    if(g<=f+f) return 1.0;
    area=0.0;
    for(row=r+f;row*row+(r+f)*(r+f)<(R-t-f)*(R-t-f);row+=r+r+g){
        //printf("%.0lf: \n", (row-r-f)/(r+r+g));
        for(col=r+f;row*row+col*col<(R-t-f)*(R-t-f);col+=r+r+g){
            trow=row+(g-f-f);
            tcol=col+(g-f-f);
            //printf("%lf %lf %lf %lf\n",row,col,trow, tcol);
            if(trow*trow+tcol*tcol<=(R-t-f)*(R-t-f)){
                area+=(g-f-f)*(g-f-f);
                //printf("%.6lf\n",(g-f-f)*(g-f-f));
            }else{
                area+=intersectArea(row,col,trow,tcol);
               // printf("%.6lf\n",intersectArea(row,col,trow,tcol));
            }
        }
    }
    area*=4;
    ans=area/(acos(-1.0)*R*R);
    return 1.0-ans;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    int i,cas;
    scanf("%d",&cas);
    for(i=1;i<=cas;i++){
        input();
        printf("Case #%d: %.6lf\n",i,solve());
    }  
    return 0;
} 
