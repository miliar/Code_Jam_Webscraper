#include<iostream>
using namespace std;
#include<math.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,i,j;
    scanf("%d",&T);
    double x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4,N,dis,dis1,dis2,dis3,t1,t2,time,D,a,b,c;
    for (i=1;i<=T;i++)
    {
        scanf("%lf",&N);
        x3=0;y3=0;z3=0;x4=0;y4=0;z4=0;
        for (j=0;j<N;j++)
        {
            scanf("%lf%lf%lf%lf%lf%lf",&x1,&y1,&z1,&x2,&y2,&z2);
            x3+=x1;y3+=y1;z3+=z1;
            x4+=x2;y4+=y2;z4+=z2;
        }
        x3/=N;y3/=N;z3/=N;
        x4/=N;y4/=N;z4/=N;
        dis1=(y3*z4 - z3*y4)*(y3*z4 - z3*y4) + (x3*z4 - x4*z3)*(x3*z4 - x4*z3) + (x3*y4 - x4*y3)*(x3*y4 - x4*y3);
        dis2=x4*x4+y4*y4+z4*z4;
        //cout<<"dis2 "<<dis2<<endl;
        dis3=dis1/dis2;
        dis=sqrt(dis3);
        //cout<<"dis "<<dis<<endl;
        a=x4*x4+y4*y4+z4*z4;
        b=(x4*x3+y4*y3+z4*z3);
        if (a>0)
        {
                time=-(b)/a;
        } 
        else
        {
                time=+0.0;
        }   
        if(time <= 0.0)
	    time = +0.0;
	    dis = sqrt((x3+x4*time)*(x3+x4*time) +(y3+y4*time)*(y3+y4*time) +(z3+z4*time)*(z3+z4*time));
        printf("Case #%d: %.8lf %.8lf\n",i,dis,time);
    }
}
