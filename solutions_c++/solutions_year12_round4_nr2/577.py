#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
class node{
    public:
        int x, y;
};

bool cmp (const node& a,const node &b) {
    return (a.x < b.x);
}

node r[10000];
int b[10000];
double q[10000][2];
int test, n, w, l;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    for (int t = 1; t <= test; t++) {
        cin >> n >> w >> l;
        int u = 0, s;
        if (w < l) { s = w; w = l; l = s; u = 1;}
        for (int i = 1; i <= n; i++) {
            scanf("%d", &r[i].x); r[i].y = i;
        }
        sort(r + 1, r + n + 1, cmp);
        int num = 1;
        b[n] = 1;
        int x = 0, y = 0, nowR = r[n].x;
        for (int i = n; i >= 1; i--) {
            q[r[i].y][0] = x, q[r[i].y][1] = y;
            if (i == 1) break;
            y += r[i].x + r[i - 1].x;
            if (y > l) {y = 0; x += nowR + r[i - 1].x; nowR = r[i - 1].x;}
        }
        /*q[r[n].y][0] = 0; q[r[n].y][1] = 0;
        int now = 0;
        //cout << "!!!!";
        double x = 0, y = r[n].x;
        memset(b, 0, sizeof(b));*/
        //cout << x << ' ' << y << ' ' << l - y << ' ' << r[1].x << endl;

        printf("Case #%d:", t);
        for (int i = 1; i <= n; i++) {
            printf(" %.1lf %.1lf", q[i][u], q[i][1 - u]);
        }
        //if (num != n) cout << "!!!!!!!!";
        cout << endl;
    }
}
      /*  for (int i = n - 1; i >= 1; i--) {
            if ((l >= y) && (l - y >= r[i].x)) {
                //cout << x << ' ' << y + r[i].x << endl;
                q[r[i].y][0] = x; q[r[i].y][1] = y + r[i].x;
                y += r[i].x * 2;
                b[i] = 1;
                num++;
            }
        }

			}
        //cout << "!!!!";
        x += r[n].x;
        while (1) {
            y = 0;
            now = 0;
            for (int i = n - 1; i >= 1; i--) {
                if ((b[i] == 0) && (w >= x) && (w - x >= r[i].x)) {
                    x += r[i].x;
                    q[r[i].y][0] = x; q[r[i].y][1] = y;
                    b[i] = 1; now = i;
                    num++;
                    break;
                }
            }
            if (now == 0) break;
            for (int i = n - 1; i >= 1; i--) {
                if ((b[i] == 0) && (l >= y) && (l - y >= r[i].y)) {
                    q[r[i].y][0] = x; q[r[i].y][1] = y + r[i].x;
                    b[i] = 1;
                    y += r[i].x * 2;
                    num++;
                }
            }
            x += r[now].x;
        }
*/
