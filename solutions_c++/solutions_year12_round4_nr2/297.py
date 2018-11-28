#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAXN = 1010;
double w, l;
double a[MAXN];
int b[MAXN];

double ans[MAXN][2], temp[MAXN][2];
int n, tot;

void getPos(double &x, double &y) {
    x = rand() % 100000000;
    y = rand() % 100000000;
    x = (w/100000000)*x;
    y = (l/100000000)*y;
}

double distance(double x1, double y1, double x2, double y2) {
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
}

bool search(int p) {
    if (p == n)
        return true;
    int num = 10000;
    while (num > 0) {
        --num;
        double x,y;
        getPos(x, y);
        temp[p][0] = x;
        temp[p][1] = y;
        bool ok = true;
        for (int i = 0; i < p; ++i)
            if (distance(x, y, temp[i][0], temp[i][1]) < (a[b[p]]+a[b[i]])*(a[b[p]]+a[b[i]])) {
                ok = false;
                break;
            }
        if (ok && search(p+1))
            return true;
    }
    return false;
}

int cmp(int x, int y) {
    return (a[x] > a[y]);
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("ou.txt", "w", stdout);
    scanf("%d", &tot);
    int num = 0;
    while (num < tot) {
        ++num;
        scanf("%d%lf%lf", &n, &w, &l);
        for (int i = 0; i < n; ++i) {
            scanf("%lf", &a[i]);
            b[i] = i;
        }
        sort(b, b+n, cmp);
        search(0);
        for (int i = 0; i < n; ++i) {
           ans[b[i]][0] = temp[i][0];
           ans[b[i]][1] = temp[i][1];
        }
        printf("Case #%d:", num);
        for (int i = 0; i < n; ++i)
            printf(" %lf %lf", ans[i][0], ans[i][1]);
        printf("\n");
    }
}
