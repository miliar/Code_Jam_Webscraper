#include<iostream>
#include<cmath>
#include<iomanip>

using namespace std;

const double pi = 2*acos(0);

double arc(double r, double t) {
    return r*r*(t - sin(t))/2;
}

double area(double x, double y, double a, double r) {
    if(x*x+y*y >= r*r) return 0;
    if((x+a)*(x+a) + (y+a)*(y+a) <= r*r) return a*a;
    
    //cout << x << ' ' << y << ' ' << a << ' ' << r <<  endl;
    
    if(x*x + (y+a)*(y+a) >= r*r) {
        if((x+a)*(x+a) + y*y >= r*r) {   // case 4
            double t1 = acos(x/r);
            double t2 = asin(y/r);
            double y1 = r*sin(t1)-y, y2 = r*cos(t2)-x;
            return arc(r, t1-t2) + y1*y2/2;
        }
        else {                         // case 1
            double t1 = acos(x/r);
            double t2 = acos((x+a)/r);
            double y1 = r*sin(t1) - y, y2 = r*sin(t2) - y;
            return arc(r, t1-t2) + (y1 + y2)*a/2;
        }
    }
    else {
        if((x+a)*(x+a) + y*y >= r*r) {   // case 3
            double t1 = asin((y+a)/r);
            double t2 = asin(y/r);
            double y1 = r*cos(t1)-x, y2 = r*cos(t2)-x;
            return arc(r, t1-t2) + (y1 + y2)*a/2;
        }
        else {                         // case 2
            double t1 = acos((x+a)/r);
            double t2 = asin((y+a)/r);
            double y1 = y+a-r*sin(t1), y2 = x+a-r*cos(t2);
            return arc(r, t2-t1) + a*a - y1*y2/2;
        }
    }
}


double pr(double f, double R, double t, double r, double g) {
    if(g - 2*f <= 0) return 1;
    if(R - t <= f) return 1;
    double A = pi*R*R/4, B=A;
    double d = 2*r + g;
    for(int i=0; i*d<R; i++) {
        for(int j=0; j*d<R; j++) {
            A -= area(i*d+r+f, j*d+r+f, g-2*f, R-t-f);
        }
    }
    
    
    return (A/B);
}

int main() {
    int n;
    cin >> n;
    for(int c=1; c<=n; c++) {
        double f, R, t, r, g;
        cin >> f >> R >> t >> r >> g;
        printf("Case #%d: %.7f\n", c, pr(f, R, t, r, g));
    }
}
