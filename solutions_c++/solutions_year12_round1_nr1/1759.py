#include <iostream>
#include <cstdio>
using namespace std;
class Node {
    public :
        int b, n;
        double g;
};
const int ww = 1000000;
int t, n, m, l, l1, rr, pre, now;
//Node f[1000000];
double f[2][ww];
double a[1000000], ans;


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int nn = 1; nn <= t; nn++) {
        cin >> n >> m;
        for (int i = n; i >= 1; i--) {
            scanf("%lf", &a[i]);
        }
        ans = m + 2; pre = 0; now = 1; f[0][0] = m - n + 1; l =0;
        for (int i = 1; i <= n; i++) {
            l1 = 0;
            if (f[pre][i - 1] + 2 <= ans) {l = i - 1; l1 = 1;}
            for (int j = 0; j <= l; j++) {
                f[now][j] = a[i] * (f[pre][j]) + (1 - a[i]) * (f[pre][j]+ m + 1);
                //cout << i << ' ' << j << ' ' << f[now][j] << endl;
            }
            l += l1;
            if (l == i) {f[now][i] = f[pre][i - 1] + 2;}
            //cout << i << ' ' << l << ' ' << f[now][l] << endl;}
            now  = 1 - now; pre = 1 - pre;
        }
        for (int j = 0; j <= l; j++) if (f[pre][j] < ans) ans = f[pre][j];
        /*l = -1; rr = 0; f[0].g = m - n + 1; f[0].b = 1; f[0].n = 0;
        while (l != rr) {
            l++; if (l > ww) l -= ww;
            int j = f[l].n + 1;
            if (j > n) continue;
            if (f[l].b == 1) {
                rr++;
                if (rr > ww) rr -=ww;
                f[rr] = f[l];
                f[rr].g += 2;
                f[rr].n++;
                cout << f[rr].b << ' '<< f[rr].g << ' ' << f[rr].n << endl;
                if (f[rr].g > ans) rr--;
                if (f[rr].n == n && f[rr].g < ans) ans = f[rr].g;
            }
            rr++;
            if (rr > ww) rr -=ww;
            f[rr] = f[l];
            f[rr].b = 0;
            f[rr].g = a[j] * (1 + f[l].g) + (1 - a[j]) * (1 + f[l].g + m + 1);
            f[rr].n++;
            cout << f[rr].b << ' '<< f[rr].g << ' ' << f[rr].n << endl;
            if (f[rr].n == n && f[rr].g < ans) ans = f[rr].g;
        }*/
                cout << "Case #" << nn << ": ";
        printf("%.6lf\n", ans);
    }
}
