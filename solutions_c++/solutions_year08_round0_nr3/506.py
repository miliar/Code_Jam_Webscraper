#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int > > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

double inside(double x, double y, double r) {
    return x*x + y*y < r*r;
}

double poly_area(vector<pair<double,double> > p) {
    double area = 0;

    for(int i = 1; i+1<p.size(); i++){
        double x1 = p[i].first - p[0].first;
        double y1 = p[i].second - p[0].second;
        double x2 = p[i+1].first - p[0].first;
        double y2 = p[i+1].second - p[0].second;
        double cross = x1*y2 - x2*y1;
        area += cross;
    }
    return abs(area/2.0);
}

double eps = 1e-12;

bool intersect(pair<double,double> p0, pair<double,double> p1, double r, pair<double,double>& pt)
{

    double root_x, root_y;
    if (p1.second == p0.second) {
        root_y = p0.second;
        if (r*r < root_y*root_y) return false;
        root_x = sqrt(r*r - root_y*root_y);
        if (root_x > eps + min(p0.first,p1.first) && root_x + eps < max(p0.first,p1.first)) {
            pt.first = root_x;
            pt.second = root_y;
            return true;
        }
    } else if (p1.first == p0.first) {
        root_x = p0.first;
        if (r*r < root_x*root_x) return false;
        root_y = sqrt(r*r - root_x*root_x);
        if (root_y > eps + min(p0.second,p1.second) && root_y + eps < max(p0.second,p1.second)) {
            pt.first = root_x;
            pt.second = root_y;
            return true;
        }
    }

    return false;
}

double circle(pair<double,double> p0, pair<double,double> p1, double r) 
{
    vector<pair<double,double> > tri;
    tri.push_back(make_pair(0,0));
    tri.push_back(p0);
    tri.push_back(p1);

    double angle[2];
    angle[0] = atan(p1.second/p1.first);
    angle[1] = atan(p0.second/p0.first);
    if (angle[0] < angle[1]) {
        swap(angle[0],angle[1]);
    }
    double ang = angle[0]-angle[1];
    return r*r*ang/2 - poly_area(tri);
}

string print(double a, double b) {
    ostringstream oss;
    oss << "(" << a << ", " << b << ")";
    return oss.str();
}

double pi = 2*acos(0);
int main()
{
    int n;
    scanf("%d\n", &n);
    for (int tr=0; tr<n; tr++) {
        double f, R, t, r, g;
        scanf("%lf %lf %lf %lf %lf\n", &f, &R, &t, &r, &g);

        vector<pair<double,double> > outside;

        double total_area = pi*(R)*(R)/4;
        double rect_area=0;
        for (double x=r; x<=R+1; x+=g+2*r) {
            for (double y=r; y<=R+1; y+=g+2*r) {
                if (inside(x+f,y+f,R-t-f) 
                        && inside(x-f+g,y+f,R-t-f)
                        && inside(x+f,  y-f+g,R-t-f)
                        && inside(x-f+g,y-f+g,R-t-f)) {
                    if (g > 2*f) {
                        rect_area += (g-2*f)*(g-2*f);
                    }
                } else {
                    outside.push_back(make_pair(x,y));
                }
            }
        }

        double slice_area=0;
        for (int i=0; i<outside.size(); i++) {
            pair<double,double> pii = outside[i];
            pair<double,double> pt[4];
            bool pint[4];
            pint[0] = intersect(make_pair(pii.first+f,   pii.second+f),      make_pair(pii.first-f+g,    pii.second+f), R-t-f,       pt[0]);
            pint[1] = intersect(make_pair(pii.first-f+g, pii.second+f),      make_pair(pii.first-f+g,    pii.second-f+g), R-t-f,     pt[1]);
            pint[2] = intersect(make_pair(pii.first-f+g, pii.second-f+g),    make_pair(pii.first+f,      pii.second-f+g), R-t-f,     pt[2]);
            pint[3] = intersect(make_pair(pii.first+f,   pii.second-f+g),    make_pair(pii.first+f,      pii.second+f), R-t-f,       pt[3]);


            vector<pair<double,double> > poly;
            if (pint[0] && pint[3]) {
                poly.push_back(make_pair(pii.first+f,pii.second+f));
                poly.push_back(pt[0]);
                poly.push_back(pt[3]);
                slice_area += circle(pt[0],pt[3],R-t-f);
            } else if (pint[0] && pint[2]) {
                poly.push_back(make_pair(pii.first+f,pii.second+f));
                poly.push_back(pt[0]);
                poly.push_back(pt[2]);
                poly.push_back(make_pair(pii.first+f,pii.second-f+g));
                slice_area += circle(pt[0],pt[2],R-t-f);
            } else if (pint[1] && pint[3]) {
                poly.push_back(make_pair(pii.first+f,pii.second+f));
                poly.push_back(make_pair(pii.first-f+g,pii.second+f));
                poly.push_back(pt[1]);
                poly.push_back(pt[3]);
                slice_area += circle(pt[1],pt[3],R-t-f);
            } else if (pint[1] && pint[2]) {
                poly.push_back(make_pair(pii.first+f,pii.second+f));
                poly.push_back(make_pair(pii.first-f+g,pii.second+f));
                poly.push_back(pt[1]);
                poly.push_back(pt[2]);
                poly.push_back(make_pair(pii.first+f,pii.second-f+g));
                slice_area += circle(pt[1],pt[2],R-t-f);
            }


            slice_area += poly_area(poly);
        }


        
        printf("Case #%d: %lf\n", tr+1, 1.-(slice_area + rect_area)/total_area);

    }
    return 0;
}

