#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>

#define MAX 110

typedef long long i64;

using namespace std;

struct Point {
    double x, y;

    Point() {}
    Point(double _x, double _y) : x(_x), y(_y) {}
} p[MAX];

double r[MAX];

double dis(const Point &a, const Point &b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

int randInt(int n) {
    i64 ret = (i64)rand();
    ret = (ret << 15) | ((i64)rand());
    ret = (ret << 15) | ((i64)rand());
    return (int)(ret % n);
}

double randDouble() {
    return ((double)rand()) / RAND_MAX;
}

Point randPoint(int w, int l) {
    return Point(randInt(w) + randDouble(), randInt(l) + randDouble());
}

bool check(int n, int &a, int &b) {
    int i, j;

    for (i = 0; i < n; ++i) {
        for (j = i + 1; j < n; ++j) {
            if (dis(p[i], p[j]) <= r[i] + r[j]) {
                a = i; b = j;
                return false;
            }
        }
    }

    return true;
}

void solve(int n, int w, int l) {
    int i, a, b;

    for (i = 0; i < n; ++i) p[i] = randPoint(w, l);
    while (!check(n, a, b)) {
        while (dis(p[a], p[b]) <= r[a] + r[b]) {
            p[a] = randPoint(w, l);
            p[b] = randPoint(w, l);
        }
    }
}

int main() {
    int t, ct = 0, n, l, w, i;

    srand((unsigned int)time(NULL));


    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d", &n, &w, &l);
        for (i = 0; i < n; ++i) scanf("%lf", &r[i]);
        solve(n, w, l);
        printf("Case #%d:", ++ct);
        for (i = 0; i < n; ++i) printf(" %.2lf %.2lf", p[i].x, p[i].y);
        printf("\n");
    }

    return 0;
}
