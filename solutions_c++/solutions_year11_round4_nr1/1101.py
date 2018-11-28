#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <queue>
#include <map>
#include <cmath>
#define EXP 1e-8
#define M 1000005


using namespace std;

int base[M];
int add[M];

typedef pair<int, int> PII;
PII pii[1005];

int dblcmp(double n) {
    return fabs(n) < EXP ? 0 : n > 0 ? +1 : -1;
}

int main()
{
    //freopen("test.in", "r", stdin);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    int index = 1;
    scanf ("%d", &T);
    while (T --) {
        int X, S, R, N;
        double t;
        scanf ("%d%d%d%lf%d", &X, &S, &R, &t, &N);

        for (int i = 0; i < X; i ++) {
            base[i] = S;
            add[i] = 0;
        }

        for (int i = 0; i < N; i ++) {
            int a, b, c;
            scanf ("%d%d%d", &a, &b, &c);
            pii[i] = PII(c, b - a);
        }
        sort(pii, pii + N);

        int i = X - 1;
        for (int j = N - 1; j >= 0; j --) {
            int len = pii[j].second;
            while (len --) {
                add[i --] = pii[j].first;
            }
        }

        double ans = 0.0;
        i = 0;
        for (; i < X; i ++) {
            double tmp = 1.0 / (R + add[i]);
            if (dblcmp(t - tmp) > 0) {
                t -= tmp;
                ans += tmp;
            } else {
                double ss = 1.0 - t * (R + add[i]);
                ans += t;
                ans += ss / (base[i] + add[i]);
                t = 0;
                break;
            }
        }

        for (i ++; i < X; i ++) {
            ans += 1.0 / (base[i] + add[i]);
        }

        printf ("Case #%d: %.6f\n", index++, ans);
    }
    return 0;
}
