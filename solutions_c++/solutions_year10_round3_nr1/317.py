/*
=====contest=========
Point operator +-*
xmul
equal,zero
distance(Point to Point;Point to Line)
intersect_point(Line and Line)
midpoint
online(Point on segment)
vertical(Point and Line)
midperpendicular
symmetric_point(Point to Line)
incircle(Trangle)
*/
#include <iostream>
#include <cmath>
using namespace std;

const double EPS = 1e-8;

class Point{
    public:
        double x,y;
        Point(double,double);
};
Point::Point(double x = 0.0,double y = 0.0){
    Point::x = x;
    Point::y = y;
}

class Line{     // ax + by + c = 0
    public:
        double a,b,c;
        Line(Point,Point);
        Line(double,double,double);
};
Line::Line(Point p1,Point p2){
    Line::a = p2.y - p1.y;
    Line::b = p1.x - p2.x;
    Line::c = -a * p1.x - b * p1.y;
}
Line::Line(double a = 0.0,double b = 0.0,double c = 0.0){
    Line::a = a;
    Line::b = b;
    Line::c = c;
}

class Circle{
    public:
        Point c;
        double r;
        Circle(Point,double);
};
Circle::Circle(Point c = Point(),double r = 0.0){
    Circle::c = c;
    Circle::r = r;
}

class Triangle{
    public:
        Point p[3];
        Triangle(Point,Point,Point);
        Point get_p(int);
};
Triangle::Triangle(Point p1,Point p2,Point p3){
    Triangle::p[0] = p1;
    Triangle::p[1] = p2;
    Triangle::p[2] = p3;
}


Point operator+(Point a,Point b){
    return Point(a.x+b.x,a.y+b.y);
}
Point operator-(Point a,Point b){
    return Point(a.x-b.x,a.y-b.y);
}
double operator*(Point a,Point b){
    return a.x * b.x + a.y * b.y;
}

double xmul(Point a,Point b){
    return a.x * b.y - a.y * b.x;
}
double xmul(double x1,double y1,double x2,double y2){
    return x1 * y2 - y1 * x2;
}
bool eq(double a,double b){
    return fabs(a - b) < EPS;
}
bool zero(double a){
    return eq(a,0.0);
}
inline bool gt(double a,double b){
    return a > b-EPS;
}
inline bool gteq(double a,double b){
    return gt(a,b) || eq(a,b);
}
inline bool st(double a,double b){
    return !gteq(a,b);
}
inline bool steq(double a,double b){
    return !gt(a,b);
}
inline double dis(Point p1,Point p2){
    return sqrt((p1.x-p2.x) * (p1.x-p2.x) + (p1.y-p2.y) * (p1.y-p2.y));
}
inline double dis(Point p,Line l){
    return fabs(p.x * l.a + p.y * l.b + l.c) / sqrt(l.a*l.a + l.b*l.b);
}
Point intersect_point(Line l1,Line l2){
    Point res(0.0, 0.0);
    double det;
    det = xmul(l1.a,l1.b,l2.a,l2.b);
    if(zero(det)) return res;
    res.x = xmul(-l1.c,l1.b,-l2.c,l2.b) / det;
    res.y = xmul(l1.a,-l1.c,l2.a,-l2.c) / det;
    return res;
}
inline Point midpoint(Point p1,Point p2){
    return Point((p1.x+p2.x) * 0.5,(p1.y+p2.y) * 0.5);
}
bool online(Point p,Point p1,Point p2){
    return zero(xmul(p-p1,p-p2))
        && min(p1.x,p2.x) <= p.x && p.x <= max(p1.x,p2.x)
        && min(p1.y,p2.y) <= p.y && p.y <= max(p1.y,p2.y);
}
int intersect(Point p1,Point p2,Point p3,Point p4,Point& p){        //-1 for not cross and not parallel, 0 for coincide, 1 for parallel, 2 for intersect
    double d1,d2,d3,d4;
    d1 = xmul(p4-p3,p1-p3);
    d2 = xmul(p4-p3,p2-p3);
    d3 = xmul(p2-p1,p3-p1);
    d4 = xmul(p2-p1,p4-p1);
    if(zero(d1) && zero(d2) && zero(d3) && zero(d4)
    && online(p1,p3,p4) || online(p2,p3,p4)) return 0;      //for segment, erase this line for Line
    if(d1*d2 < 0 && d3*d4 < 0){
        p = intersect_point(Line(p1,p2),Line(p3,p4));
        return 2;
    }
    if(online(p1,p3,p4)){
        p = p1;
        return 2;
    }
    if(online(p2,p3,p4)){
        p = p2;
        return 2;
    }
    if(online(p3,p1,p2)){
        p = p3;
        return 2;
    }
    if(online(p4,p1,p2)){
        p = p4;
        return 2;
    }
    if(zero(xmul(p2-p1,p4-p3))) return 1;
    p = intersect_point(Line(p1,p2),Line(p3,p4));       //for Line
    return -1;
}
Line vertical(Point p,Line l){
    Line res;
    res.a = l.b;
    res.b = -l.a;
    res.c = -(p.x * res.a + p.y * res.b);
    return res;
}
Line midperpendicular(Point p1,Point p2){
    return vertical(midpoint(p1,p2),Line(p1,p2));
}
Point symmetric_point(Point p,Line l){
    Line tl(vertical(p,l));
    Point O(intersect_point(tl,l)),res;
    res.x = O.x * 2 - p.x;
    res.y = O.y * 2 - p.y;
    return res;
}
Circle incircle(Triangle t){
    Circle res;
    res.c = intersect_point(midperpendicular(t.p[0],t.p[1]),midperpendicular(t.p[1],t.p[2]));
    res.r = dis(t.p[0],res.c);
    return res;
}


Point a[10100];
Point p;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    cin >> T;
    for(int I = 1;I <= T;++I){
        int n;
        cin >> n;
        for(int i = 0;i < n;++i){
            a[2*i].x = 0;
            a[2*i+1].x = 1;
            cin >> a[2*i].y >> a[2*i+1].y;
        }
        int ans(0);
        for(int i1 = 0;i1 < n;++i1)
            for(int j1 = 0;j1 < i1;++j1){
                if(intersect(a[i1*2],a[i1*2+1],a[j1*2],a[j1*2+1],p) == 2)
                    ++ans;
            }
        cout << "Case #" << I << ": " << ans << endl;
    }
}
