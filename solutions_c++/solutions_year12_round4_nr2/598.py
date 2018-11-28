#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>

using namespace std;

const int MAX_N = 1100;
typedef pair<int, int> PII;
int n, w, l, T;
bool used[MAX_N];
int x[MAX_N], y[MAX_N];
PII r[MAX_N];

bool gao(int x0, int y0, int cw, int ch) {
    int i;
    bool flag = false;
    for (i = 0; i < n; i++) {
        if (!used[i]) {
            flag = true;
            //int rr = r[i].first;
            if (cw >= r[i].first * 2 && ch >= r[i].first * 2) {
                //rr + x0 >= 0 && rr + y0 >= 0 && rr + x0 <= w && rr + y0 <= l) {
                break;
            }
        }
    }
    if (!flag) return false;
    if (i == n) return true;

    int rr = r[i].first;
    int rx = rr + x0, ry = rr + y0;
    if (rx < 0) rx = 0;
    if (ry < 0) ry = 0;
    int rw = rx - x0, rh = ry - y0;
    if (rx > w || ry > l)
        return true;

    x[r[i].second] = rx;
    y[r[i].second] = ry;
    used[i] = true;

    //printf("(%d %d)+(%d %d) %d@(%d,%d)\n", x0, y0, cw, ch, i, rx, ry);

    if (!gao(x0 + rw + rr, y0, cw - rw - rr, rh + rr))
        return false;
    if (!gao(x0 + rw + rr, y0 + rh + rr, cw - rw - rr, ch - rh - rr))
        return false;
    if (!gao(x0, y0 + rh + rr, rw + rr, ch - rh - rr))
        return false;

    return true;

}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d%d%d", &n, &w, &l);
        for (int i = 0; i < n; i++) {
            scanf("%d", &r[i].first);
            r[i].second = i;
        }
        memset(used, false, sizeof(used));
        sort(r, r + n, greater<PII>());
        gao(-r[0].first, -r[0].first, w + r[0].first * 2, l + r[0].first * 2);
        for (int i = 0; i < n; i++) {
            if (!used[i])
                printf("err = %d\n", r[i].second);
        }
        printf("Case #%d:", t);
        for (int i = 0; i < n; i++)
            printf(" %d %d", x[i], y[i]);
        printf("\n");
    }
}
