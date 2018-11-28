#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int p[1000010], pos, n;
int cT, cN, a, b, a1, a2, b1, b2, lowlim;
long long ans;

int main() {
    p[1] = 2;
    pos = 1;
    for (n = 2; n <= 1000000; ++n) {
        if (n == p[pos]) ++pos;
        p[n] = n + pos;
    }
    scanf("%d", &cN);
    for (cT = 1; cT <= cN; ++cT) {
        scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
        ans = 0;
        // a < b => b >= p[a]
        for (a = a1; a <= a2; ++a) {
            lowlim = b1;
            if (p[a] > lowlim) lowlim = p[a];
            if (b2 >= lowlim) ans += b2 - lowlim + 1;
        }
        // reverse
        for (b = b1; b <= b2; ++b) {
            lowlim = a1;
            if (p[b] > lowlim) lowlim = p[b];
            if (a2 >= lowlim) ans += a2 - lowlim + 1;
        }
        cout << "Case #" << cT << ": " << ans << endl;
    }
}
