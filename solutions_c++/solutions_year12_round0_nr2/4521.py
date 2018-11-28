#include <cstdio>
#include <cstring>

int T, n, S, P;
int a[128];

void solve(int test) {
    int i;
    int sol = 0;
    for (i = 1; i <= n; ++i) {
        int v = a[i];
        //if (v == 0)
        //    continue;
        int rest = v % 3;
        int t = v / 3;
        if (rest == 0) {
            if (t >= P) {
                ++sol;
                continue;
            }
            if (S >= 1  && t - 1 >= 0 && t + 1 >= P) {
                ++sol;
                --S;
                continue;
            }
        }
        if (rest == 1) {
            if (t + 1 >= P) {
                ++sol;
                continue;
            }
        }
        if (rest == 2) {
            if (t + 1 >= P) {
                ++sol;
                continue;
            }
            if (S >= 1 && t + 2 >= P) {
                ++sol;
                --S;
                continue;
            }
        }
    }

    printf ("Case #%d: %d\n", test, sol);
}

int main() {
    freopen ("b.in", "r", stdin);
    freopen ("b.out", "w", stdout);
    scanf ("%d\n", &T);
    for (int test = 1; test <= T; ++test) {
        scanf ("%d %d %d ", &n, &S, &P);
        for (int i = 1; i <= n; ++i)
            scanf ("%d ", &a[i]);
        
        solve(test);
    }
}
