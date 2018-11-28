#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

#define N 2000005
#define LL long long

bool a[N];

LL solve() {
    int l, r;
    int b[20];
    LL ret = 0;
    scanf("%d %d", &l, &r);
    fill(a + l, a + r + 1, false);
    for (int i = l; i <= r; ++i) {
        if (a[i]) continue;
        int bn = 0;
        for (int x = i; x; x /= 10)
            b[bn++] = x % 10;
        reverse(b, b + bn);
        for (int j = 0; j < bn; ++j)
            b[bn + j] = b[j];
        LL cnt = 0;
        for (int j = 0; j < bn; ++j) {
            int x = 0;
            for (int k = 0; k < bn; ++k)
                x = x * 10 + b[j + k];
            if (l <= x && x <= r && !a[x]) {
                a[x] = true;
                ++cnt;
            }
        }
        ret += cnt * (cnt - 1) / 2;
    }
    return ret;
}

int main() {
    int cas;
    scanf("%d", &cas);
    for (int i = 1; i <= cas; ++i)
        cout << "Case #" << i << ": " << solve() << endl;
    return 0;
}
