#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define two(x)  (1<<x)
#define twol(x) ((long long)1<<x)
#define sqr(x)  ((x)*(x))

main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int task=1;task<=t;task++)
    {
        int n;
        cin>>n;
        double x=0,y=0,z=0,vx=0,vy=0,vz=0;
        for (int i=0;i<n;i++)
        {
            double curx,cury,curz,curvx,curvy,curvz;
            cin>>curx>>cury>>curz>>curvx>>curvy>>curvz;
            x+=curx;y+=cury;z+=curz;
            vx+=curvx;vy+=curvy;vz+=curvz;   
        }
        //cout<<x/n<<" "<<y/n<<" "<<z/n<<" "<<vx/n<<" "<<vy/n<<" "<<vz/n<<endl;
        double a,b,c;
        a=sqr(vx/n)+sqr(vy/n)+sqr(vz/n);
        b=2*vx*x/sqr(n)+2*vy*y/sqr(n)+2*vz*z/sqr(n);
        c=sqr(x/n)+sqr(y/n)+sqr(z/n);
        //cout<<b*b-4*a*c<<endl;
        //cout<<a+b+c<<" "<<sqr(vx/n+x/n)+sqr(vy/n+y/n)+sqr(vz/n+z/n)<<endl;
        //cout<<a<<" "<<b<<" "<<c<<endl;
        double t,dist;
        if (abs(a)<1e-5)
            t=0;
        else
        t=-b/(2*a);
        //cout<<t<<endl;
        if (t<1e-5)    t=0;
        dist=a*t*t+b*t+c;
        if (dist<1e-5)  dist=0;
        dist=sqrt(dist);
        printf("Case #%d: %7lf %7lf\n",task,dist,t);
    }    
}
