#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>

#define MAX 1010
#define INF 1000000000

typedef long long i64;

using namespace std;

int h[MAX], p[MAX];

struct Point {
    double x, y;

    Point() {}
    Point(double _x, double _y) : x(_x), y(_y) {}

    Point operator -(const Point &p) const {
        return Point(x - p.x, y - p.y);
    }

    double xMul(const Point &p) const {
        return x * p.y - y * p.x;
    }
};

int randInt(int n) {
    i64 ret = (i64)rand();
    ret = (ret << 15) | ((i64)rand());
    ret = (ret << 15) | ((i64)rand());
    return (int)(ret % n);
}

bool _check(int x, int y, int k) {
    Point a(x, h[x]), b(y, h[y]), p(k, h[k]);
    return (a - p).xMul(b - p) < 0;
}

int check(int n, int &x) {
    int i, j;

    for (i = 0; i < n - 1; ++i) {
        for (j = i + 1; j < p[i]; ++j) {
            if (!_check(i, p[i], j)) {
                x = i;
                return 1;
            }
        }
        for (j = p[i] + 1; j < n; ++j) {
            if (!_check(i, p[i], j)) {
                x = i;
                return 2;
            }
        }
    }

    return 0;
}

bool solve(int n) {
    int i, x, tag, cnt = 0;

    for (i = 0; i < n; ++i) h[i] = rand() % 10 + 1;
    while (tag = check(n, x)) {
        if (tag == 1) h[x] += rand() % 10 + 1;
        else h[p[x]] += rand() % 10 + 1;

        if (h[x] > INF || h[p[x]] > INF) return false;
        if (++cnt >= 1000000) return false;

       // for (i = 0; i < n; ++i) printf("%d ", h[i]);
       // printf("\n");
        //getchar();
    }

    return true;
}

int main() {
    int t, ct = 0, n, i;

    srand((unsigned int)time(NULL));

    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n - 1; ++i) {
            scanf("%d", &p[i]);
            --p[i];
        }
        printf("Case #%d:", ++ct);
        if (!solve(n)) printf(" Impossible\n");
        else {
            for (i = 0; i < n; ++i) printf(" %d", h[i]);
            printf("\n");
        }
    }

    return 0;
}
