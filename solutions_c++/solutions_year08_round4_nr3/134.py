#include <cstdio>
#include <vector>
#include <cmath>

#define MAXN 1024
#define ITERATIONS 100
#define INF 2000000000
#define EPS 1e-7

using namespace std;

struct point {
    float x, y, z, d;
};

vector<point> p;

float calc(float c[]) {
    point tmp;
    tmp.x = c[0];
    tmp.y = c[1];
    tmp.z = c[2];
    float res = 0;
    for (unsigned i = 0; i < p.size(); i++) {
        res = max((abs(p[i].x - tmp.x) + abs(p[i].y - tmp.y) + abs(p[i].z - tmp.z)) / p[i].d, res);
    }
    return res;
}

float solve(int i, float c[]) {
    if (i == 3) {
        return calc(c);
    }
    float l = 0, r = 1000000, res = INF;
    for (int t = 0; t < ITERATIONS; t++) {
        float m1 = (2 * l + r) / 3;
        float m2 = (l + 2 * r) / 3 + EPS;
        c[i] = m1;
        float res1 = solve(i + 1, c);
        c[i] = m2;
        float res2 = solve(i + 1, c);
        if (res1 < res2) {
            r = m2;
        }
        else {
            l = m1;
        }
        res = min(res1, res2);
    }
    return res;
}

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ti++) {
        fprintf(stderr, "%d\n", ti);
        int n;
        scanf("%d", &n);
        p.resize(n);
        for (int i = 0; i < n; i++) {
            scanf("%f%f%f%f", &p[i].x, &p[i].y, &p[i].z, &p[i].d);
        }
        float c[3];
        printf("Case #%d: %f\n", ti + 1, solve(0, c));
    }
    return 0;
}
