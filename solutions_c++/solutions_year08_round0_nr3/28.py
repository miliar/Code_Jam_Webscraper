#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

using namespace std;

double PI = acos(-1);

double area(double x1, double y1, double x2, double y2, double r)
{
    if(x1*x1 + y1*y1 > r*r - 1e-8) return 0;
    if(x2*x2 + y2*y2 < r*r + 1e-8) return (x2 - x1)*(y2 - y1);
    
    bool b1 = (x1*x1 + y2*y2 < r*r + 1e-8);
    bool b2 = (x2*x2 + y1*y1 < r*r + 1e-8);
    
    if(b1 && b2)
    {
        double o1 = 0.5*PI - asin(x2/r), o2 = asin(y2/r);
        double A = 0.5*r*r*(o2-o1) - 0.5*(x1*tan(o2) - y1)*x1 - 0.5*(y1*tan(0.5*PI - o1) - x1)*y1;
        A += 0.5*(y2*tan(0.5*PI - o2) - x1)*(y2 - x1*tan(o2));
        A += 0.5*(x2*tan(o1) - y1)*(x2 - y1*tan(0.5*PI - o1));
        return A;
    }
    else if(b1 && !b2)
    {
        double o1 = asin(y1/r), o2 = asin(y2/r);
        double A = 0.5*r*r*(o2-o1) - 0.5*(x1*tan(o2) - y1)*x1 - 0.5*(y1*tan(0.5*PI - o1) - x1)*y1;
        A += 0.5*(y2*tan(0.5*PI - o2) - x1)*(y2 - x1*tan(o2));
        return A;
    }
    else if(!b1 && b2)
    {
        double o1 = 0.5*PI - asin(x2/r), o2 = 0.5*PI - asin(x1/r);
        double A = 0.5*r*r*(o2-o1) - 0.5*(x1*tan(o2) - y1)*x1 - 0.5*(y1*tan(0.5*PI - o1) - x1)*y1;
        A += 0.5*(x2*tan(o1) - y1)*(x2 - y1*tan(0.5*PI - o1));
        return A;
    }
    else
    {
        double o1 = asin(y1/r), o2 = 0.5*PI - asin(x1/r);
        double A = 0.5*r*r*(o2-o1) - 0.5*(x1*tan(o2) - y1)*x1 - 0.5*(y1*tan(0.5*PI-o1) - x1)*y1;
        return A;
    }
    
    return 0;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int N;
    cin>>N;
    
    for(int caso=0; caso<N; caso++)
    {
        double f, R, t, r, g;
        cin>>f>>R>>t>>r>>g;
       // 0.000001 1 0.000005 0.000001  0.002002

        double A = 0, T = acos(-1)*R*R/4;
               
        double x = r, y = r, D = g + 2*r;
        while(x < R - t)
        {
            y = r;
            while(y < R - t)
            {
                if(g > 2*f)
                {
                    A += area(x + f, y + f, x + g - f, y + g - f, R - t - f);
                }
                
                y += D;
            }
            x += D;
        }
        
        cout<<"Case #"<<caso + 1<<": ";
        printf("%.6lf\n", (T-A)/T);
    }
    return 0;
}

