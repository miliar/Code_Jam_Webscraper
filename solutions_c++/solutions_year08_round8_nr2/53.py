// comment

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:30000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <utility>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

const int nmax = 400;
const int inf = (int)1e+9;

vector < vector < int > > q;
pair < int, int > a[nmax];
int col[nmax];
string color[nmax];
map < string, int > num;
int n, m;
int ans;
int use[10000];

bool myless(const int & x, const int & y) {
    return (a[x].first < a[y].first);
}

int bitcnt(int x) {
    int res = 0;
    while (x > 0) {
        res += (x & 1);
        x >>= 1;
    }
    return res;
}

void init() {
    q.clear();

    scanf("%d\n", &n);
    m = 0;
    num.clear();
    for (int i = 0; i < n; ++i) {
        cin >> color[i] >> a[i].first >> a[i].second;
        if (num.count(color[i]) == 0) num[color[i]] = m++;
    }
    for (int i = 0; i < n; ++i) col[i] = num[color[i]];
    q.resize(m);
    for (int i = 0; i < n; ++i) {
        q[col[i]].push_back(i);
    }
}

vector < int > h;
int dp[nmax];
int k;

void solve() {
    h.reserve(n);
    for (int c1 = 0; c1 < m; ++c1) {
        for (int c2 = c1; c2 < m; ++c2) {
            for (int c3 = c2; c3 < m; ++c3) {
                h.clear();
                h.insert(h.begin(), q[c1].begin(), q[c1].end());
                if (c1 != c2) h.insert(h.begin(), q[c2].begin(), q[c2].end());
                if (c2 != c3) h.insert(h.begin(), q[c3].begin(), q[c3].end());
                k = (int)h.size();
                sort(h.begin(), h.end(), myless);
                for (int i = 0; i < k; ++i) {
                    if (a[h[i]].first == 1) dp[i] = 1;
                    else {
                        dp[i] = inf;
                        int x = h[i], y;
                        for (int j = 0; j < i; ++j) if (dp[j] != inf) {
                            y = h[j];
                            if (a[y].second + 1 >= a[x].first) {
                                if (dp[j] + 1 < dp[i]) dp[i] = dp[j] + 1;
                            }
                        }
                    }
                }

                for (int i = 0; i < k; ++i) {
                    if (a[h[i]].second == 10000) {
                        if (ans > dp[i]) ans = dp[i];
                    }
                }
            }
        }
    }
}

void writeanswer() {
    if (ans == inf) printf("IMPOSSIBLE");
    else printf("%d", ans);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        cerr << testid << endl;
        init();
        ans = inf;
        solve();
        printf("Case #%d: ", testid + 1);
        writeanswer();
        printf("\n");
    }
    
    return 0;
}
