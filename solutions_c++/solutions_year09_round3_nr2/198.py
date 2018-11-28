#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <float.h>

using namespace std;

// prewritten code

#define sz(x) (int)(x).size()
#define all(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define pb push_back

#define GDB 1
#define DBG(x) if(GDB){cerr << #x <<" = "<< x << endl;}
#define DBGA(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cerr<<x[i]<<' '; cerr<<endl;}
#define DBGV(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cerr<<x[i]<<' '; cerr<<endl;}

// real code
string problem_name="b";
void init(){
    freopen( (problem_name+".in").c_str(),"rt",stdin);
    freopen( (problem_name+".out").c_str(),"wt",stdout);
}
double f(double x,double y,double z){
    return sqrt(x*x+y*y+z*z);
}
double solve(double x,double y,double z,double vx,double vy,double vz){
    double l=0.,r=10000000000.;
    double ml,mr;
    int i;
    for(i=0;i<100000;i++){
        ml=(l+r)/3;
        mr=2*(l+r)/3;
        if(f(x+ml*vx,y+ml*vy,z+ml*vz)<=f(x+mr*vx,y+mr*vy,z+mr*vz)) r=mr; else l=ml;
    }
    return (l+r)/2;
}
int main(){
    init();
    int T,tt;
    int n,i;
    double d;
    double t;
    double x,y,z,vx,vy,vz;
    int tx,ty,tz,tvx,tvy,tvz;
    scanf("%d",&T);
    for(tt=1;tt<=T;tt++){
        x=y=z=vx=vy=vz=0.;
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d %d %d %d %d %d",&tx,&ty,&tz,&tvx,&tvy,&tvz);
            x=x+tx+0.;
            y=y+ty+0.;
            z=z+tz+0.;
            vx=vx+tvx+0.;
            vy=vy+tvy+0.;
            vz=vz+tvz+0.;
        }
        x=(x/(n+0.));
        y=(y/(n+0.));
        z=(z/(n+0.));
        vx=(vx/(n+0.));
        vy=(vy/(n+0.));
        vz=(vz/(n+0.));
        t=solve(x,y,z,vx,vy,vz);
        d=sqrt((x+vx*t)*(x+vx*t)+(y+vy*t)*(y+vy*t)+(z+vz*t)*(z+vz*t));
        printf("Case #%d: %.8lf %.8lf\n",tt,d,t);
    }
    return 0;
}
