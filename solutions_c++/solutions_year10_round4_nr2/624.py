#include <cmath>
#include <cstdio>
#include <map>
#include <vector>

#define MAXP 20
#define MAXN 10000

using namespace std;

int test, tests;
int p;
int n;
int res;
int m[MAXN];
bool f[MAXP][MAXN];
bool u[MAXN];

int count(int t) {
    int z = m[t];
    int k = 0;
    int r = p - 1;
    t = t >> 1;
    while (r >= 0 && z > 0) {
        if (!f[r][t])
            z--;
        k++;
        r--;
        t = t >> 1;
    }
    return k;
}

void fill(int t) {
    int z = m[t];
    int r = p - 1;
    t = t >> 1;
    while (r >= 0 && z > 0) {
        if (!f[r][t])
            z--;
        r--;
        t = t >> 1;
    }
    while (r >= 0) {
        if (!f[r][t]) {
            f[r][t] = true;
            res++;
        }
        r--;
        t = t >> 1;
    }
}

void solve() {
    scanf("%d", &p);
    n = 1 << p;
    for (int i = 0; i < n; i++)
        scanf("%d", &m[i]);
    
    int step = 1 << (p - 1);
    int tmp = 0;
    while (step > 0) {
        for (int i = 0; i < step; i++)
            scanf("%d", &tmp);
        step = step >> 1;
    }       

    for (int r = 0; r <= p; r++)
        for (int t = 0; t < n; t++)
            f[r][t] = false;
    for (int i = 0; i < n; i++)
        u[i] = false;


    res = 0;
    for (int step = 0; step < n; step++) {
        int zi = -1;
        int zc = -1;
        for (int i = 0; i < n; i++) {
            if (u[i])
                continue;
            int tmp = count(i);
            if (zi == -1 || tmp < zc) {
                zi = i;
                zc = tmp;
            }
        }

        fill(zi);
        u[zi] = true;
    }
    printf("Case #%d: %d\n", test, res);
}

int main() {
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("data.out", "wt", stdout);

    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
        solve();

    return 0;
}
