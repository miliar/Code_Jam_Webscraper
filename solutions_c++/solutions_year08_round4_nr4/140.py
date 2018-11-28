// comment

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <string>
#include <vector>

using namespace std;

const int nmax = 50001;
const int inf = (int)1e+9;

char q[nmax];
string s;
int k, n, res;

void solve() {
    res = n = (int)s.length();
    vector < int > p(k);
    for (int i = 0; i < k; ++i) p[i] = i;
    do {
        for (int i = 0; i < n; ++i) {
            int j = i % k;
            q[i - j + p[j]] = s[i];
        }
        int cur = 1;
        for (int i = 1; i < n; ++i) {
            if (q[i] != q[i - 1]) cur++;
        }
        if (res > cur) res = cur;
    } while (next_permutation(p.begin(), p.end()));

    printf("%d", res);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);

    for (int testid = 0; testid < testcnt; ++testid) {
        cin >> k >> s;
        printf("Case #%d: ", testid + 1);

        solve();

        printf("\n");
        cerr << testid << endl;
    }
    
    return 0;
}
