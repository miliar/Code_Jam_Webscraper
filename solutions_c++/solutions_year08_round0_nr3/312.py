#include <vector>
#include <stack>
#include <map>
#include <iostream>
#include <fstream>
#include <strstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

template <typename T>
inline T sqr(T x) { return x*x; }

double sq1_x(double x, double r)
{
    if(x > r)
        return 0;
    double y = sqrt(sqr(r) - sqr(x));
    return (asin(x/r)*sqr(r) - x*y)/2;
}

double sq1_y(double y, double r)
{
    if(y > r)
        return 0;
    double x = sqrt(sqr(r) - sqr(y));
    return (acos(y/r)*sqr(r) - x*y)/2;
}
//////////////////////////////////////////////////////////////////////////
double sec_sq_xx(double x1, double x2, double r)
{
    double y1 = sqrt(sqr(r)-sqr(x1));
    double y2 = sqrt(sqr(r)-sqr(x2));
    return abs(sq1_x(x1, r) - sq1_x(x2, r)) - abs(y1-y2)*min(x1, x2);
}

double sec_sq_xy(double x1, double y2, double r)
{
    double y1 = sqrt(sqr(r)-sqr(x1));
    double x2 = sqrt(sqr(r)-sqr(y2));
    return abs(sq1_x(x1, r) - sq1_y(y2, r)) - abs(y1-y2)*min(x1, x2);
}

double sec_sq_yx(double y1, double x2, double r)
{
    double x1 = sqrt(sqr(r)-sqr(y1));
    double y2 = sqrt(sqr(r)-sqr(x2));
    return abs(sq1_y(y1, r) - sq1_x(x2, r)) - abs(y1-y2)*min(x1, x2);
}

double sec_sq_yy(double y1, double y2, double r)
{
    double x1 = sqrt(sqr(r)-sqr(y1));
    double x2 = sqrt(sqr(r)-sqr(y2));
    return abs(sq1_y(y1, r) - sq1_y(y2, r)) - abs(y1-y2)*min(x1, x2);
}
////////////////////////////////////////////////////////////////////////

double getWinSq(double x1, double y1, double x2, double y2, double r)
{
    if(sqr(x1) + sqr(y1) >= sqr(r))    // ---
    { /*cout<<' ';*/ return 0; }

    if(sqr(x2) + sqr(y2) <= sqr(r))    // 0 1 2 3
    { /*cout<<'0'; */return (x2-x1)*(y2-y1); }

    if(sqr(x1)+ sqr(y2) >= sqr(r)) {
        if(sqr(x2)+ sqr(y1) >= sqr(r))   // 0
        { /*cout<<'`';*/ return sec_sq_xy(x1, y1, r); } 
        else                             // 0, 2
        { /*cout<<'~';*/ return sec_sq_xx(x1, x2, r) + (x2-x1)*(sqrt(sqr(r)-sqr(x2)) - y1); }
    }
    else {
        if(sqr(x2)+ sqr(y1) >= sqr(r))                              // 0 1
        { /*cout<<'|'; */ return sec_sq_yy(y1, y2, r) + (y2-y1)*(sqrt(sqr(r)-sqr(y2)) - x1); }
        else {  // 0 1 2
            double _x2 = sqrt(sqr(r) - sqr(y2));
            double _y2 = sqrt(sqr(r) - sqr(x2));
            /*cout<<'/';*/
            return sec_sq_xy(x2, y2, r) + (y2-y1)*(_x2-x1) + (x2-_x2)*(_y2-y1); 

        }
    }
    return 0;
}

double Solve(double f, double R, double t, double r, double g)
{
    if(2*f >= g)
        return 1;

    double win_sz = g + 2*r;
    double rad = R - t - f;

    double win_count = rad/win_sz;

    double sq = 0;

    //cout<<endl;
    for(double yw_pos = 0; yw_pos <= rad; yw_pos += win_sz) {
        for(double xw_pos = 0; xw_pos <= rad; xw_pos += win_sz) {
            sq += getWinSq(xw_pos + r + f, yw_pos + r + f, xw_pos + r + g - f, yw_pos + r + g - f, rad);
        }
        //cout<<endl;
    }

    return 1-sq/(R*R*acos(-1.0)/4);
    
}

int main(int argc, char* argv[])
{
    string in_file("C-sample.in");
    if(argc > 1)
        in_file = argv[1];
    ifstream in(in_file.c_str());

    int N;
    in>>N;
    for(size_t i = 0; i<N; ++i) {
        double f, R, t, r, g;
        in>>f>>R>>t>>r>>g;
        cout<<"Case #"<<i+1<<": ";
        cout.precision(6);
        cout<<fixed<<Solve(f, R, t, r, g)<<endl;
    }

    int a;
    //cin>>a;
    return 0;
}

