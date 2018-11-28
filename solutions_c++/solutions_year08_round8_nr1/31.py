// comment

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:30000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <cmath>

using namespace std;

class cnum {
public:
    double x, y;

    void operator += (const cnum & b) {
        x += b.x, y += b.y;
    }
    void operator *= (const double & k) {
        x *= k, y *= k;
    }
    void operator -= (const cnum & b) {
        x -= b.x, y -= b.y;
    }
    void operator *= (const cnum & b) {
        double x1 = x*b.x - y*b.y;
        double x2 = x*b.y + y*b.x;
        x = x1, y = x2;
    }
    void operator /= (const cnum & b) {
        double x1 = x*b.x + y*b.y;
        double x2 = -x*b.y + y*b.x;
        double m = b.x*b.x + b.y*b.y;
        x = x1 / m, y = x2 / m;
    }    
    cnum() { x = y = 0; }
    cnum(double xx, double yy) { x = xx, y = yy; }
};

cnum c;

void solve() {
    cnum p[3], q[3];
    for (int i = 0; i < 3; ++i) {
        scanf("%lf%lf", &p[i].x, &p[i].y);
    }
    for (int i = 0; i < 3; ++i) {
        scanf("%lf%lf", &q[i].x, &q[i].y);
    }

    if (fabs(p[0].x - q[0].y) + fabs(p[0].y - q[0].y) < 1e-7) {
        c = p[0];
        return;
    }

    cnum r = q[2];
    r -= q[1];
    cnum temp = p[2];
    temp -= p[1];
    r /= temp;

    temp = p[1];
    temp *= r;
    temp *= -1;
    temp += q[1];
    r = cnum(1 - r.x, -r.y);
    temp /= r;

    c = temp;
}

void writeanswer() {
    printf("%0.6lf %0.6lf", c.x, c.y);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        solve();
        printf("Case #%d: ", testid + 1);
        writeanswer();
        printf("\n");
    }
    
    return 0;
}
