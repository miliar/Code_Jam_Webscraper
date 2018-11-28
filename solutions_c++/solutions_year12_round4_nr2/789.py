#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <ctime>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
const int maxn = 15;
int t, n, w, l, r[maxn], x[maxn], y[maxn];

long long sqr(long long x) {
    return x * x;
}

bool check(int sx, int sy, int r1, int tx, int ty, int r2) {
    long long d = sqr(sx - tx) + sqr(sy - ty);
    return d >= sqr(r1 + r2);
}

int ca;

void out() {
    printf("Case #%d: ", ++ca);
    for(int i = 1; i < n; i++) {
        printf("%d %d ", x[i], y[i]);
    }
    printf("%d %d\n", x[n], y[n]);
}

int main() {
    freopen("B.out", "w", stdout);
    srand(time(0));
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d%d", &n, &w, &l);
        for(int i = 1; i <= n; i++) {
            scanf("%d", r + i);
        }
        x[1] = y[1] = 0;
        for(int i = 2; i <= n; i++) {
            while(1) {
                int tx = (long long)rand() * rand() % (w + 1);
                int ty = (long long)rand() * rand() % (l + 1);
                bool ck = true;
                for(int j = 1; j < i; j++) {
                    if(!check(x[j], y[j], r[j], tx, ty, r[i])) {
                        ck = false;
                        break;
                    }
                }
                if(ck) {
                    x[i] = tx;
                    y[i] = ty;
                    break;
                }
            } 
        }
        out();
    }
    return 0;
}

