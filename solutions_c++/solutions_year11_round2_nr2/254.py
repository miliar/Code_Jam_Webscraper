#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const double eps = 1e-8;
int c, d;
int p[500], v[500];

int check(double t) {
    double l = -1e99;
    for(int i=0; i<c; ++i) {
        for(int j=0; j<v[i]; ++j) {
            l = max(l + d, (double)p[i] - t);
            if(l > p[i] + t) return 0;
        }
    }
    return 1;
}

void work() {
    scanf("%d%d", &c, &d);
    for(int i=0; i<c; ++i) {
        scanf("%d%d", &p[i], &v[i]);
    }
    double l = 0, h = 1e15, mid;
    int cnt = 0;
    while(l + eps < h) {
        ++cnt;
        if(cnt > 1000) break;
        mid = (l + h) / 2;
        if (check(mid)) h = mid;
        else l = mid + eps;
    }
    printf("%.10f\n", h);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; ++i) {
        printf("Case #%d: ", i+1);
        work();
    }
}
