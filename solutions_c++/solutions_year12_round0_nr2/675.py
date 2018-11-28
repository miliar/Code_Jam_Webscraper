#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 1010

using namespace std;

struct Triple {
    int x, y, z;

    Triple() {}
    Triple(int _x, int _y, int _z) : x(_x), y(_y), z(_z) {}
};

Triple getTriple(int n, bool tag) {
    int x = n % 3;

    if (tag) {
        switch (x) {
            case 0: return Triple(n / 3 - 1, n / 3, n / 3 + 1);
            case 1: return Triple((n - 1) / 3 - 1, (n - 1) / 3 + 1, (n - 1) / 3 + 1);
            case 2: return Triple((n + 1) / 3 - 1, (n + 1) / 3 - 1, (n + 1) / 3 + 1);
            default: return Triple();
        }
    } else {
        switch (x) {
            case 0: return Triple(n / 3, n / 3, n / 3);
            case 1: return Triple((n - 1) / 3, (n - 1) / 3, (n - 1) / 3 + 1);
            case 2: return Triple((n + 1) / 3 - 1, (n + 1) / 3, (n + 1) / 3);
            default: return Triple();
        }
    }

    return Triple();
}

int a[MAX];

int main() {
    int t, ct = 0, ans, cnt, n, s, p, i;
    Triple cur;

    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d", &n, &s, &p);
        for (i = 0; i < n; ++i) scanf("%d", &a[i]);
        sort(a, a + n, greater<int>());
        ans = 0;
        for (cnt = i = 0; i < n; ++i) {
            cur = getTriple(a[i], false);
            if (cur.z >= p) ++ans;
            else {
                if (a[i] > 1 && cnt < s) {
                    cur = getTriple(a[i], true);
                    if (cur.z >= p) {
                        ++ans; ++cnt;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", ++ct, ans);
    }

    return 0;
}
