#include <iostream>
#include <cmath>

using namespace std;

int x,n,i;
double svx,svy,svz,sx,sy,sz,t;

int main()
{
    freopen("gcj2.in","r",stdin);
    freopen("gcj2.out","w",stdout);
    cin>>x;
    for (int ii=1;ii<=x;ii++)
    {
        cin>>n;
        cout<<"Case #"<<ii<<": ";
        int p1,p2,p3,p4,p5,p6;
        sx=sy=sz=svx=svy=svz=0;
        for (i=1;i<=n;i++)
        {
            cin>>p1>>p2>>p3>>p4>>p5>>p6;
            sx+=p1;sy+=p2;sz+=p3;svx+=p4;svy+=p5;svz+=p6;
        }
        if (abs(svx*svx+svy*svy+svz*svz)<=10e-6)
        {
           printf("%.8lf %.8lf\n",sqrt(sx*sx+sy*sy+sz*sz)/n,0.0);
        }
        else
                                        
                                        if ((sx*svx+sy*svy+sz*svz)/(svx*svx+svy*svy+svz*svz)>=0)
                                           printf("%.8lf %.8lf\n",sqrt(sx*sx+sy*sy+sz*sz)/n,0.0);
                                        else
                                        {
                                            t=-(sx*svx+sy*svy+sz*svz)/(svx*svx+svy*svy+svz*svz);
                                            
                                            double a,b,c;
                                            a=svx*svx+svy*svy+svz*svz;
                                            b=2*(sx*svx+sy*svy+sz*svz);
                                            c=sx*sx+sy*sy+sz*sz;
                                                       double temp=(a*t*t);
                                                       temp+=(b*t);
                                                       temp+=(c);
                                            printf("%.8lf %.8lf\n",sqrt(temp)/n,t);
                                        }
        
    }
    return 0;
}
            
