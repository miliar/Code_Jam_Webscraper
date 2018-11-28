#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>


using namespace std;

const double PI=acos(-1);

const int ITERATIONS=1000000;

double integ(double R, double x)
{
    assert(x*x<=R*R);
    return 0.5*(x*sqrt(R*R-x*x)+R*R*asin(x/R) );
}

double Area(double x, double ox, double y, double oy, double R)
{
    if(x*x+y*y>=R*R) return 0.0;
    oy=sqrt(R*R-x*x)<?oy;
    ox=sqrt(R*R-y*y)<?ox;
    double cx=sqrt(R*R-oy*oy)<?ox;
    //if(cx>=ox) return (ox-x)*(oy-y);
    return (cx-x)*(oy-y)+(integ(R,ox)-integ(R,cx))-y*(ox-cx) ;
}
bool show=true;
double solveNof(double R, double t, double r, double g)
{
    if(g<=0.00) return 1.0;
    double bigA=Area(0,R,0,R,R);//PI*R*R/4;
    
    R-=t;
    if(R-r<=0) return 1.0;
    
    double y=r;
    double sum=0;
    show=true;
    while(y<R)
    {
        double x=r;
        while(x<R)
        {
            sum+=Area(x,x+g,y,y+g,R);
            x=x+g+2*r;
        }
        
        y=y+g+2*r;
    }
    //cout<<sum<<" / "<<bigA<<endl;
    //if(bigA<=sum) return 0;
    //assert(sum<=bigA);

    return 1-sum/bigA;
}

double solve(double f, double R, double t, double r, double g)
{
    return solveNof(R,t+f,r+f,g-2*f);
}

//=========================================================


int main()
{
    int N;
    cin>>N;
    for (int i=1;i<=N;i++)
    {
        double f, R, t, r,g;
        cin>>f>>R>>t>>r>>g;
       
        cout<<"Case #"<<i<<": "<<solve(f,R,t,r,g)<<endl;
    }
    
    
    

    return 0;
}
