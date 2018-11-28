#include <iostream>
#include <string>
using namespace std;

string a[205], b[205];
int t2, n, m;

int calc(int l, int r, int s)
{
    int ret = 1;
    for (int i = l; i <= r; ++i) if (s < a[i].size()) {
        int t = s + 1;
        while (a[i][t] != '/' && t < a[i].size()) ++t;
        b[i] = a[i].substr(s + 1, t - s - 1);
    }
    for (int i = l, j = l - 1; i <= r; ++i)
        if (s < a[i].size() && (b[i] != b[i + 1] || i == r)) {
            int t = s + 1;
            while (a[i][t] != '/' && t < a[i].size()) ++t;
            ret += calc(j + 1, i, t);
            j = i;
        }
    return ret;
}

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);

    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> n >> m;
        for (int i = 1; i <= n + m; ++i)
            cin >> a[i];
        sort(&a[1], &a[1] + n);
        int ret = calc(1, n, 0);
        sort(&a[1], &a[1] + n + m);
        printf("Case #%d: %d\n", t1, calc(1, n + m, 0) - ret);
    }
    
    return 0;
}
