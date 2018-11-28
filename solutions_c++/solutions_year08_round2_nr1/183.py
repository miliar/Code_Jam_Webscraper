#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long s64;
typedef unsigned long long u64;

s64 cnt[3][3];
s64 cnt1[3][3];

s64 ncr(int n, int r) {
    if (r == 0) return 1;
    if (r == 1) return n;
    if (r == 2) return (s64)n * (n-1) / 2;
    if (r == 3) return (s64)n * (n-1) * (n-2) / 6;
    assert(false);
    return 0;
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        memset(cnt, 0, sizeof(cnt));
        memset(cnt1, 0, sizeof(cnt1));

        int n; cin >> n;
        s64 A, B, C, D, x0, y0, M; cin >> A >> B >> C >> D >> x0 >> y0 >> M;
        s64 X = x0, Y = y0;
        cnt[X % 3][Y % 3]++;
        for (int i = 1; i < n; i++) {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            cnt[X % 3][Y % 3]++;
        }

        s64 sum = 0;
        for (int i = 0; i < 9; i++) for (int j = i; j < 9; j++) for (int k = j; k < 9; k++) {
            int a = i / 3, b = i % 3;
            int c = j / 3, d = j % 3;
            int e = k / 3, f = k % 3;
            if ((a + c + e) % 3 != 0 || (b + d + f) % 3 != 0) continue;
            cnt[a][b]--; cnt[c][d]--; cnt[e][f]--;
            cnt1[a][b]++; cnt1[c][d]++; cnt1[e][f]++;
            if (cnt[a][b] >= 0 && cnt[c][d] >= 0 && cnt[e][f] >= 0) {
                s64 test = ncr(cnt[a][b]+cnt1[a][b], cnt1[a][b]);
                if (c != a || d != b) test *= ncr(cnt[c][d]+cnt1[c][d], cnt1[c][d]);
                if (e != c || f != d) test *= ncr(cnt[e][f]+cnt1[e][f], cnt1[e][f]);
                sum += test;
            }
            cnt1[a][b]--; cnt1[c][d]--; cnt1[e][f]--;
            cnt[a][b]++; cnt[c][d]++; cnt[e][f]++;
        }
        cout << "Case #" << t << ": " << sum << endl;
    }

    return 0;
}

