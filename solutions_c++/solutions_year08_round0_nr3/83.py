#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

const double PI =  3.1415926535897932384626433832795;

double area(double a, double b, double c)
{
    double s = (a+b+c)/2.0;

    return sqrt(s*(s-a)*(s-b)*(s-c));
}

double len(double x0, double y0, double x1, double y1)
{
    return sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0));
}


int
main(void)
{
    int N;
    double f, R, t, r, g;
    int i, j;
    int x, y;
    double xx0, xx1, yy0, yy1;
    double vy0, vy1, vx0, vx1;
    int in00, in01, in10, in11;
    double area_total, a, s;
    double area_m, theta;
    vector<double> area_miss;

    cin >> N;
    for(i=1;i<=N;i++) {
        cin >> f >> R >> t >> r >> g;

        if (2.0*f > g) {
            cout << "Case #" << i << ": " << 1.0 << endl;
            continue;
        }
        g = g - 2.0*f;
        t += f;
        r += f;
        
        area_total = R*R*PI;
        area_miss.clear();

        R = R - t;

        for(x=0;x<1000;x++) {
            for(y=0;y<1000;y++) {
                xx0 = (x+0)*(g+2*r)+r;
                xx1 = xx0 + g;
                yy0 = (y+0)*(g+2*r)+r;
                yy1 = yy0 + g;

                in00 = ((xx0*xx0+yy0*yy0) < R*R) ? 1 : 0;
                in01 = ((xx0*xx0+yy1*yy1) < R*R) ? 1 : 0;
                in10 = ((xx1*xx1+yy0*yy0) < R*R) ? 1 : 0;
                in11 = ((xx1*xx1+yy1*yy1) < R*R) ? 1 : 0;

                if (!in00) {
                    continue;
                }
                if (in11) {
                    a = g*g*4.0;
                    area_miss.push_back(a);
                } else if (in10 && in01) {
                    vx0 = xx1;
                    vy0 = sqrt(R*R-vx0*vx0);
                    vy1 = yy1;
                    vx1 = sqrt(R*R-vy1*vy1);
                    a = (g*g-(yy1-vy0)*(xx1-vx1)/2.0)*4.0;
                    area_miss.push_back(a);
                    s = area(R, R, len(vx0, vy0, vx1, vy1));
                    theta = asin(2.0*s/(R*R));
                    a = (R*R*PI*theta/(2.0*PI)-s)*4.0;
                    area_miss.push_back(a);
                } else if (!in10 && in01) {
                    vy0 = yy0;
                    vx0 = sqrt(R*R-vy0*vy0);
                    vy1 = yy1;
                    vx1 = sqrt(R*R-vy1*vy1);
                    a = ((vx0-xx0)+(vx1-xx0))*g/2.0*4.0;
                    area_miss.push_back(a);
                    s = area(R, R, len(vx0, vy0, vx1, vy1));
                    theta = asin(2.0*s/(R*R));
                    a = (R*R*PI*theta/(2.0*PI)-s)*4.0;
                    area_miss.push_back(a);
                } else if (in10 && !in01) {
                    vx0 = xx0;
                    vy0 = sqrt(R*R-vx0*vx0);
                    vx1 = xx1;
                    vy1 = sqrt(R*R-vx1*vx1);
                    a = ((vy0-yy0)+(vy1-yy0))*g/2.0*4.0;
                    area_miss.push_back(a);
                    s = area(R, R, len(vx0, vy0, vx1, vy1));
                    theta = asin(2.0*s/(R*R));
                    a = (R*R*PI*theta/(2.0*PI)-s)*4.0;
                    area_miss.push_back(a);
                } else if (!in10 && !in01) {
                    vy0 = yy0;
                    vx0 = sqrt(R*R-vy0*vy0);
                    vx1 = xx0;
                    vy1 = sqrt(R*R-vx1*vx1);
                    a = (vx0-xx0)*(vy1-yy0)/2.0*4.0;
                    area_miss.push_back(a);
                    s = area(R, R, len(vx0, vy0, vx1, vy1));
                    theta = asin(2.0*s/(R*R));
                    a = (R*R*PI*theta/(2.0*PI)-s)*4.0;
                    area_miss.push_back(a);
                }
            }
        }
        sort(area_miss.begin(), area_miss.end());
        area_m = 0;
        for(j=0;j<area_miss.size();j++) {
            area_m += area_miss[j];
        }
        cout << "Case #" << i << ": " << (area_total-area_m)/area_total << endl;
    }
    
    
    return 0;
}
