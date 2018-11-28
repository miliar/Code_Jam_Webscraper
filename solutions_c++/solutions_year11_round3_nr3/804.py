#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;

int calc(int low, int high, vi& v) {
    for (int i = low; i <= high; i++) {
        bool ok = true;
        For(j, v.size()) {
            int x = v[j];
            if (x <= i) {
                if (i % x != 0) {
                    ok = false;
                    break;
                }
            }

            if (x >= i) {
                if (x % i != 0) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) return i;
    }
    return -1;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int n, low, high;
        scanf("%d %d %d", &n, &low, &high);

        vi v(n);
        For(i, n) scanf("%d", &v[i]);

        int ans = calc(low, high, v);
        printf("Case #%d: ", cc+1);
        if (ans == -1)
            puts("NO");
        else
            printf("%d\n", ans);
    }
}

