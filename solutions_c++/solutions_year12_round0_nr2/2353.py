#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, s, p, p1, ans = 0;
        cin >> n >> s >> p;
        if (p <= 0) {ans = n; for (int i = 0; i < n; i++) cin >> p;} else
        if (p > 10) {ans = 0; for (int i = 0; i < n; i++) cin >> p;} else
        {
        p1 = 2*max(0, p-2)+p;
        p = 2*max(0, p-1)+p;
        for (int i = 0; i < n; i++) {
            int v;
            cin >> v;
            if (p<=v) {ans++; continue;}
            if (s && (p1<=v)) {ans++; s--; continue;}
        }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
