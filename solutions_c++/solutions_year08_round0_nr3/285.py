#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <memory.h>

using namespace std;

#define LL                  long long
#define pb                  push_back
#define mp                  make_pair
typedef vector <int>        vi;
typedef vector <string>     vs;

const double eps = 1e-9;
const double pi  = acos(-1);

double f,R,t,r,g;
double rr,rr2,s;
double res;
char sres[100];

double cal(double x, double y, double u, double v)
{
    double alph = acos( (x*u+y*v) / (sqrt(x*x+y*y)*sqrt(u*u+v*v)) );
    return 0.5*rr2*(alph - sin(alph));
}

void process()
{
    double x,y,u,v,g1,g2;
    
    rr=R-t-f, s=g-f-f, rr2 = rr*rr;
    if (s<=0) { res = 1.0; return; }
    
    res = 0;
    for (y=r+f; y<rr; y+=g+r+r) for (x=r+f; x*x+y*y<rr2; x+=g+r+r)
    {
        u = x+s; v = y+s;
        if (u*u+v*v<=rr2) 
        { 
            res += s*s; 
            continue; 
        }

        if (x*x+v*v<=rr2)
        {
            if (u*u+y*y<=rr2)
            {
                g1 = sqrt(rr2-u*u); g2 = sqrt(rr2-v*v);
                res += s*s - 0.5*(u-g2)*(v-g1) + cal(u,g1,g2,v);
            } else
            {
                g1 = sqrt(rr2-y*y); g2 = sqrt(rr2-v*v);
                res += 0.5*(g1-x+g2-x)*s + cal(g1,y,g2,v);
            }
        } else
        {
            if (u*u+y*y<=rr2)
            {
                g1 = sqrt(rr2-x*x); g2 = sqrt(rr2-u*u);
                res += 0.5*(g1-y+g2-y)*s + cal(x,g1,u,g2);
            } else
            {
                g1 = sqrt(rr2-y*y); g2 = sqrt(rr2-x*x);
                res += 0.5*(g1-x)*(g2-y) + cal(g1,y,x,g2);
            }
        }
    }

    res = 1 - 4*res/(pi*R*R);
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int i,j,numTest;
    char buf[201];
    
    cin >> numTest; 
    for (i=0; i<numTest; i++)
    {
        cin >> f >> R >> t >> r >> g;
        process();
        sprintf(sres,"%.8lf",res);
        cout << "Case #" << (i+1) << ": " << sres << endl;
    }
    return 0;
}
