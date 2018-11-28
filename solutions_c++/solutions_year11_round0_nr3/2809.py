#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;

int naive_calc(vi& v) {
    int n = v.size();

    int ans = -1;
    for (int i = 0; i < (1<<n); i++) {
        int xsum = 0, ysum = 0;
        int x = 0, y = 0;

        For(j, n) {
            if (i & (1<<j)) {
                x ^= v[j];
                xsum += v[j];
            }
            else {
                y ^= v[j];
                ysum += v[j];
            }
        }

        if (x == y && xsum > 0 && ysum > 0) {
            //printf("x:%d xsum:%d ysum:%d\n", x, xsum, ysum);
            ans = max(ans, max(xsum, ysum));
        }
    }
    return ans;
}

int main() {
    int ncases;
    scanf("%d", &ncases);
    For(cc, ncases) {
        int n;
        scanf("%d", &n);
        vi v(n);
        For(i, n) scanf("%d", &v[i]);

        printf("Case #%d: ", cc+1);
        int ans = naive_calc(v);
        if (ans == -1)
            puts("NO");
        else
            printf("%d\n", ans);
    }
}


