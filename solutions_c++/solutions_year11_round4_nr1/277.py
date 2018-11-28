#include <iostream>
using namespace std;
const int maxn = 2 * (1000 + 10);
const double delta = 1e-8;

int zero(double s)
{
    if (s < -delta)
        return -1;
    return s > delta;
}

void swap(int &a, int &b)
{
    int t = a;
    a = b;
    b = t;
}

int main(void)
{
    int T;
    cin >> T;
    for (int loop = 1; loop <= T; loop++) {
        double x, s, r, t;
        int n;
        double b[maxn], e[maxn], w[maxn];

        cin >> x >> s >> r >> t >> n;
        for (int i = 0; i < n; i++)
            cin >> b[i] >> e[i] >> w[i];

        int st = 0, m = n;
        for (int i = 0; i < m; i++) {
            if (st < b[i]) {
                b[n] = st;
                e[n] = b[i];
                w[n++] = 0.0;
            }
            st = e[i];
        }
        if (e[m - 1] < x) {
            b[n] = e[m - 1];
            e[n] = x;
            w[n++] = 0.0;
        }

        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1; j++)
                if (w[j] > w[j + 1]) {
                    swap(b[j + 1], b[j]);
                    swap(e[j + 1], e[j]);
                    swap(w[j + 1], w[j]);
                }

//        for (int i = 0; i < n; i++)
 //           printf("%f %f %f\n", b[i], e[i], w[i]);

        double ans = 0.0;
        for (int i = 0; i < n; i++) {
            if (zero(t) >= 0) {
                double time = (e[i] - b[i]) / (w[i] + r);
                if (zero(t - time) >= 0) {
                    ans += time;
                    t -= time;
                } else {
                    double tx = (w[i] + r) * t;
                    time = t + (e[i] - b[i] - tx) / (w[i] + s);
                    t = 0.0;
                    ans += time;
                }
            } else
                ans += (e[i] - b[i]) / (w[i] + s);
        }

        printf("Case #%d: %.10f\n", loop, ans);
    }
    return 0;
}
