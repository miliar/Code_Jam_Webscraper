#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>
#include <sstream>
#include <iomanip>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
using namespace std;

const double PI = acos(-1.0);

struct Point {
    long double x, y;
    
    Point() {}
    Point(long double x, long double y) : x(x), y(y) {}
    
    Point operator + (Point a) {return Point(x + a.x, y + a.y); }
    Point operator - (Point a) {return Point(x - a.x, y - a.y); }
    
    long double len() {
        return sqrt(x*x + y*y);
    }
} lower[111], upper[111];

long double ab(long double x) {
    if (x < 0) return -x;
    else return x;
}

bool operator < (Point a, Point b) {
    if (ab(a.x - b.x) < 1e-6) return a.y < b.y;
    else return a.x < b.x;
}

struct Line {
    Point A, B;
    long double a, b, c;
    
    Line(Point A, Point B) : A(A), B(B) {
        a = B.y - A.y;
        b = A.x - B.x;
        c = - (a * A.x + b * A.y);
    }
};

int w, l, u, g;

void inp() {
    scanf("%d %d %d %d", &w, &l, &u, &g);
    FOR(i,1,l) cin >> lower[i].x >> lower[i].y;
    FOR(i,1,u) cin >> upper[i].x >> upper[i].y;
    sort(lower+1, lower+l+1);
    sort(upper+1, upper+u+1);
}

vector< Point > now;

long double area() {
    now.PB(now[0]);
    long double res = 0.0;
    REP(i,now.size() - 1)
        res += now[i].x * now[i+1].y - now[i].y * now[i+1].x;
    return ab(res) / 2.0;
}

Point intersect(Line P, long double X) {
    return Point(X, -(P.c + P.a * X) / P.b);
}

vector<Point> tmp2;

long double getArea(long double X) {
    now.clear();
    FOR(i,1,l) {
        if (ab(lower[i].x - X) < 1e-6) {
            now.PB(lower[i]);
            break;
        }
        else if (lower[i].x < X && X < lower[i+1].x) {
            now.PB(lower[i]);
            now.PB(intersect(Line(lower[i], lower[i+1]), X));
            break;
        }
        else now.PB(lower[i]);
    }
    tmp2.clear();
    FOR(i,1,u) {
        if (ab(upper[i].x - X) < 1e-6) {
            tmp2.PB(upper[i]);
            break;
        }
        else if (upper[i].x < X && X < upper[i+1].x) {
            tmp2.PB(upper[i]);
            tmp2.PB(intersect(Line(upper[i], upper[i+1]), X));
            break;
        }
        else tmp2.PB(upper[i]);
    }
    FORD(i,tmp2.size()-1,0)
        now.PB(tmp2[i]);
    return area();
}

void cut(long double S) {
    long double L = 1e-6, R = w - 1e-6;
    while (L + 1e-8 < R) {
        long double mid = (L + R) / 2.0;
        if (getArea(mid) < S) {
            L = mid;
        }
        else R = mid;
    }
    cout << (L + R) / 2.0 << endl;
}

void solve() {
    now.clear();
    FOR(i,1,l) now.PB(lower[i]);
    FORD(i,u,1) now.PB(upper[i]);
    
    long double S = area();
    
    FOR(i,1,g-1) {
        cut(S / g * i);
    }
}


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test; scanf("%d", &test);
    cout << (fixed) << setprecision(8);
    FOR(t,1,test) {
        printf("Case #%d:\n", t);
        inp();
        solve();
    }
    return 0;
}
