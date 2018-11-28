
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
using namespace std;
const double EPS = 1e-12;
const double pi = 3.14159265358979323846264338;
double f, R, t, r, g;
double aarea(double x1, double y1, double x2, double y2){
    return (x2 * y2 - x1 * y1 - (x1*x1 + y1*y1) * (atan(y2 / x2) - atan(y1 / x1))) / 2;
}
inline double sect(const double& t, const double& r){return sqrt(r*r-t*t);}
inline double dist(const double& x, const double& y){return sqrt(x*x+y*y);}
double compute(double xmin, double xmax, double ymin, double ymax, double rr){
    if (dist(xmax, ymax) <= rr + EPS) return (xmax - xmin) * (ymax - ymin);
    if (dist(xmin, ymin) > rr + EPS) return 0;
    if (dist(xmin, ymax) <= rr + EPS){
        if (dist(xmax, ymin) <= rr + EPS){
            double xx = sect(ymax, rr);
            double yy = sect(xmax, rr);
            return (xx - xmin) * (ymax - ymin) - (xmax - xx) * ymin + aarea(xx, ymax, xmax, yy);
        }
        else{
            double x1 = sect(ymax, rr);
            double x2 = sect(ymin, rr);
            return (x1 - xmin) * (ymax - ymin) - (x2 - x1) * ymin + aarea(x1, ymax, x2, ymin);
        }
    }
    else{
        if (dist(xmax, ymin) <= rr + EPS){
            double y1 = sect(xmin, rr);
            double y2 = sect(xmax, rr);
            return aarea(xmin, y1, xmax, y2) - ymin * (xmax - xmin);
        }
        else{
            double yy = sect(xmin, rr);
            double xx = sect(ymin, rr);
            return aarea(xmin, yy, xx, ymin) - ymin * (xx - xmin);
        }
    }
}
double calc(){
    g = g + r * 2;
    int k = (int)ceil((R + r) / g);
    //double gmax = (g + r * 2) * ceil((R + r) / (g + r * 2));
    //cout << gmax << endl;
    double cover = 0, xmin, xmax, ymin, ymax, x0, y0;
    for(int i = k; i > 0; -- i){
        x0 = g * i;
        //cout << x0 - g << " , " << x0 << endl;
        xmin = x0 - g + r + f;
        xmax = x0 - r - f;
        //cout << xmin << "      " << xmax << endl;
        for(int j = k; j > 0; -- j){
            y0 = g * j;//max; ; y0 -= g){
            ymin = y0 - g + r + f;
            ymax = y0 - r - f;
            //printf("(%lf,%lf,%lf,%lf,%lf)=%lf,  rate=%lf\n", xmin, xmax, ymin, ymax, R-t-f, compute(xmin, xmax, ymin, ymax, R - t - f),compute(xmin, xmax, ymin, ymax, R - t - f)/(xmax-xmin)/(ymax-ymin));
            cover += compute(xmin, xmax, ymin, ymax, R - t - f);
        }
    }
    return 1.0 - cover * 4 / pi / R / R;
}
int main(){
    //ifstream cin("C-small-attempt0.in");
    //freopen("out.txt", "w+", stdout);
    int ncase;
    cin >> ncase;
    for(int tcase = 1; tcase <= ncase; ++ tcase){
        cout << "Case #" << tcase << ": ";
        cin >> f >> R >> t >> r >> g;
        cout.setf(ios::fixed);
        cout << setprecision(6) << calc() << endl;
    }
    return 0;
}
