#include <iostream>
using namespace std;

int tcase, n, ans;

void solve() {
     char c;
     int p, r1 = 1, r2 = 1, last1 = 0, last2 = 0;
     scanf("%d", &n);
     ans = 0;
     for (int i = 1; i <= n; ++i) {
         scanf(" %c%d", &c, &p);
         if (c == 'O') {
            if (ans - last1 < abs(p - r1)) ans += abs(p - r1) - (ans - last1);
            last1 = ++ans, r1 = p;
         }
         else {
              if (ans - last2 < abs(p - r2)) ans += abs(p - r2) - (ans - last2);
              last2 = ++ans, r2 = p;
         }
     }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tcase);
    for (int k = 1; k <= tcase; ++k) {
        solve();
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}
