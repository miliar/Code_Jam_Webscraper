// comment

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>

using namespace std;

const int nmax = 10001;
const int inf = (int)1e+9;

int n, m, a;

void solve() {
    int p = a % n;
    if (p > 0) p = n - p;
    a += p;
    int x1 = n;
    int y1 = 1;
    int x2 = p;
    int y2 = a / n;
    printf("0 0 %d %d %d %d", x1, y1, x2, y2);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);

    for (int testid = 0; testid < testcnt; ++testid) {
        scanf("%d%d%d", &n, &m, &a);
        printf("Case #%d: ", testid + 1);
        if (a > (long long)n * m) printf("IMPOSSIBLE"); else {
            solve();
        }
        printf("\n");
        cerr << testid << endl;
    }
    
    return 0;
}
