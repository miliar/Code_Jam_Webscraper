#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

const double eps=1e-8;

void solve(int qqq)
{
        int n;
        scanf("%d",&n);
        double x=0,y=0,z=0,A=0,B=0,C=0;
        for(int i=0;i<n;i++)
        {
            double a1,a2,a3,b1,b2,b3;
            scanf("%lf %lf %lf %lf %lf %lf",&a1,&a2,&a3,&b1,&b2,&b3);
            x+=a1; y+=a2; z+=a3;
            A+=b1; B+=b2; C+=b3;
        }
		x/=n;
y/=n;
z/=n;
A/=n;
B/=n;
C/=n;
        double t;
		if((A*A+B*B+C*C) < eps)
		{
			t=0;
		}
		else
         {   
             t=-(A*x+B*y+C*z)/(A*A+B*B+C*C);
             }
        if(t<0)t=0;
        double rx=x+A*t;
        double ry=y+B*t;
        double rz=z+C*t;
        double d=sqrt((rx)*(rx)+(rz)*(rz)+(ry)*(ry));
        printf("Case #%d: %.8lf %.8lf\n", qqq, d, t);
}

int main()
{
    freopen("B-large.in","r",stdin);
   freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int qqq = 1; qqq <= T; qqq++)
    {
        solve(qqq);
    }
} 
