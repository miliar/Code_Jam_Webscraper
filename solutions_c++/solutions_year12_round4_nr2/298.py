#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#define X first
#define Y second
#define N 1001

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int rr[N], cx[N], cy[N], p[N];
PII r[N];

inline double dis(int x1, int y1, int x2, int y2)
{
    return sqrt(LL(x1 - x2) * (x1 - x2) + LL(y1 - y2) * (y1 - y2));
}

inline bool check(int x, int y, int a, int b)
{
    if (dis(x, y, cx[b], cy[b]) >= r[a].X + r[b].X) return true;
    return false;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        int n, w, l;
        scanf("%d%d%d", &n, &w, &l);
        for (int i = 0; i < n; i++) scanf("%d", &r[i].X), r[i].Y = i;
        sort(r, r + n);
        rr[n - 1] = r[n - 1].X;
        cx[n - 1] = cy[n - 1] = 0;
        bool flag;
        for (int i = n - 2; i >= 0; i--) {
            rr[n] = -r[i].X;
            for (int j = n; j > i; j--) {
                int x = rr[j] + r[i].X;
                if (x >= w) break;
                for (int k = n; k > i; k--) {
                    int y = rr[k] + r[i].X;
                    if (y >= l) break;
                    flag = true;
                    for (int kk = n - 1; kk > i; kk--)
                        if (!check(x, y, i, kk)) {
                            flag = false;
                            break;
                        }
                    if (flag) {
                        cx[i] = x, cy[i] = y;
                        rr[i] = rr[i + 1] + r[i].X * 2;
                        break;
                    }
                }
                if (flag) break;
            }
        }
        for (int i = 0; i < n; i++) p[r[i].Y] = i;
        printf("Case #%d:", cases);
        for (int i = 0; i < n; i++) printf(" %d %d", cx[p[i]], cy[p[i]]);
        printf("\n");
    }
    return 0;
}
