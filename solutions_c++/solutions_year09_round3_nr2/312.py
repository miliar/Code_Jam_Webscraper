#include<stdio.h>
#include<iostream>
#include<queue>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<math.h>
#include<algorithm>
#define _clr(x) memset(x,-1,sizeof(x))
#define clr(x) memset(x,0,sizeof(x))
#define pb push_back
#define M 1001
using namespace std;
const double eps=1e-9;
int main()
{
    freopen("in.txt","r",stdin);
    //freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ca;
    scanf("%d",&ca);
    int cas=0;
    while(ca--)
    {
        int n;
        scanf("%d",&n);
        double x=0,y=0,z=0,A=0,B=0,C=0;
        for(int i=0;i<n;i++)
        {
            double rx,ry,rz,ra,rb,rc;
            scanf("%lf%lf%lf%lf%lf%lf",&rx,&ry,&rz,&ra,&rb,&rc);
            x+=rx;
            y+=ry;
            z+=rz;
            A+=ra;
            B+=rb;
            C+=rc;
        }
		x/=n;
		y/=n;
		z/=n;
		A/=n;
		B/=n;
		C/=n;
        double t;
		if((A*A+B*B+C*C)<eps)
		{
			t=0;
		}
		else
			t=-(A*x+B*y+C*z)/(A*A+B*B+C*C);
        if(t<eps)t=0;
        double xx=x+A*t;
        double yy=y+B*t;
        double zz=z+C*t;
        double d=sqrt((xx)*(xx)+(zz)*(zz)+(yy)*(yy));
        printf("Case #%d: %.8lf %.8lf\n",++cas,d,t);
    }
}
