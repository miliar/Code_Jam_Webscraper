#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

int x[128];
int y[128];
int r[128];
int n;

#define EPS (1e-9)

typedef double real;
inline bool eq(real q, real w) { return fabs(q-w)<EPS; }
inline bool more(real q, real w) { return q-w>EPS; }
inline bool les(real q, real w) { return w-q>EPS; }
inline bool moreeq(real q, real w) { return q-w>-EPS; }
inline bool lesseq(real q, real w) { return w-q>-EPS; }
inline real mul( real x1, real y1, real x2, real y2) { return x1*y2-y1*x2;}

#define SQR2(x,y) (SQR(x)+SQR(y))

#define SQR(x) ((x)*(x))

class Point {
public:
    real x,y;
    Point() {x=y=0; }
    Point(real q,real w) {x=q; y=w; }                                
    friend Point operator+ (Point a,Point b) {return *new Point(a.x+b.x,a.y+b.y);}
    friend Point operator- (Point a,Point b) {return *new Point(a.x-b.x,a.y-b.y);}   
    friend ostream& operator << (ostream& str,Point q) {
        str << '(' << q.x << ',' << q.y << ')' << endl;
        return str;
    }
    friend inline real mul(Point q,Point w) { return q.x*w.y-q.y*w.x; }
};

class Circle {
public:
    real x,y,r;    
    Circle() {x=y=r=0;}
    Circle( real _x, real _y, real _r) {x=_x;y=_y;r=_r;}
    int detect( Point p) {
        static real tmp;
        tmp=SQR2(x-p.x,y-p.y)-SQR(r);
        return eq(tmp,0)?0:tmp>0?1:-1;
    }
    friend ostream& operator << (ostream& str,Circle& q) {
        str << '(' << q.x << ',' << q.y << ' ' << q.r << ')' << endl;
        return str;
    }
};

#define SQRT(x) (((x)<1e-9)?0:sqrt(x))
#define PI		3.14159265358979323846

class Vector {
public:
    real x,y;
    Vector() {x=y=0; }
    Vector( real q, real w) {x=q; y=w; }
    Vector( real x1, real y1, real x2, real y2) {x=x2-x1; y=y2-y1;}
    Vector( Point p1, Point p2) {x=p2.x-p1.x; y=p2.y-p1.y;}    
    friend Vector& operator+ ( Vector a, Vector b) {return *new Vector(a.x+b.x,a.y+b.y);}
    friend Vector& operator- ( Vector a, Vector b) {return *new Vector(a.x-b.x,a.y-b.y);}
    friend Vector& operator* ( Vector a, real p) {return *new Vector(p*a.x,p*a.y);}     
    friend inline real operator* ( Vector a, Vector b) { return a.x*b.x+a.y*b.y; }     
    inline real len()  {return SQRT(x*x+y*y);}    
    inline real len2()  {return x*x+y*y;}    
    real angle( Vector b)  {
        static real q,w,e;
        q=x*b.y-y*b.x;
        w=x*b.x+y*b.y;
        e=fabs(atan(q/w));
        if (eq(w,0) && q>0) return PI/2;
        if (eq(w,0) && q<0) return -PI/2;                
        if (w>0) return e;
        if (q>-EPS) return e+PI;
        return e-PI;
    }
    friend ostream& operator << (ostream& str,Vector& q) {
        str << '(' << q.x << ',' << q.y << ')' << endl;
        return str;
    }
    friend inline real mul( Vector q, Vector w) { return q.x*w.y-q.y*w.x; } 
};
inline real dist( Point p, Point p1, Point p2) {
    return fabs(mul(Vector(p,p1),Vector(p,p2))/Vector(p1,p2).len());
}
inline real dist( Point p1,Point p2) {
    return SQRT(SQR(p1.x-p2.x)+SQR(p1.y-p2.y));
}
inline real dist(real x1,real y1,real x2,real y2) {
    return SQRT(SQR(x1-x2)+SQR(y1-y2));
}

vector<Point>& intersect(Circle q,Circle w) {
    static real l,hp,o1h;
    vector<Point> &res =*new vector<Point> ();        
    l=dist(q.x,q.y,w.x,w.y);
    if (l>q.r+w.r) return res;
    if (l<fabs(q.r-w.r)) return res;    
    o1h=(q.r*q.r+l*l-w.r*w.r)/(2*l);
    hp=SQRT(q.r*q.r-o1h*o1h);
    Vector vo1h=Vector(q.x,q.y,w.x,w.y)*(o1h/l);
    Vector n(w.y-q.y,q.x-w.x);
    Point h(q.x+vo1h.x,q.y+vo1h.y);
    Vector vhp=n*(hp/n.len());
    res.push_back(Point(h.x+vhp.x,h.y+vhp.y));
    res.push_back(Point(h.x-vhp.x,h.y-vhp.y));    
    return res;
}

bool can (double R)
{
    vector <Point> p;
    REP (i, n)
        p.pb (Point (x[i]+0.0, y[i]+0.0));
    REP (i, n)
        REP (j, i)
        if (R > r[i] && R > r[j])
        {
            double d1 = R - r[i];
            double d2 = R - r[j];
            vector <Point> u = intersect (Circle (x[i], y[i], d1), Circle (x[j], y[j], d2));
            REP (k, SZ (u))
                p.pb (u[k]);      
        }
    vector <ll> mm;
    REP (i, SZ (p))
    {
        ll mask = 0;
        REP (j, n)
            if (lesseq (dist (p[i], Point (x[j], y[j])) + r[j], R))
                mask |= 1LL<<j;
        mm.pb (mask);                
    }
    UNIQUE (mm);
    REP (i, SZ (mm))
        REP (j, i+1)
            if ((mm[i] | mm[j]) == (1LL<<n)-1)
                return true;
    return false;
}

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    FOR (ntest, 1, test+1)
    {
        cin >> n;
        REP (i, n)
            cin >> x[i] >> y[i] >> r[i];            
        double b1 = 0;
        double b2 = 1e5;
        while (b2 - b1 > 1e-7)
        {
            double r = (b1 + b2) / 2;
            if (!can (r))
                b1 = r;
            else
                b2 = r;
        }
        printf ("Case #%d: %.7lf\n", ntest, (b1+b2)/2);
    }
	return 0;
}
