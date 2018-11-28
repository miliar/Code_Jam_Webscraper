#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int, pii> pip;
typedef pair<pii, int> ppi;
typedef pair<int64, int64> pii64;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "B"
#define RR 151

int c, d, n;
string comb[64];
char a[128][128];
string opp[64];
vector< vector<char> > op;
string s;
int cnt[128];

void solve () {
    memset(a, 0, sizeof a);
    for (int i = 0; i < c; ++i) {
        char x = comb[i][0];
        char y = comb[i][1];
        a[x][y] = a[y][x] = comb[i][2];
    }
    op.clear();
    op.resize(128);
    for (int i = 0; i < d; ++i) {
        char x = opp[i][0];
        char y = opp[i][1];
        op[x].push_back(y);
        op[y].push_back(x);
    }

    vector<char> ans;
    memset(cnt, 0, sizeof cnt);
    for (int i = 0; i < n; ++i) {
        char x = s[i];
        if (!ans.empty() && a[ans.back()][x]) {
            char y = ans.back();
            ans.pop_back();
            --cnt[y];
            ans.push_back(a[x][y]);
            ++cnt[a[x][y]];
            continue;
        }
        bool bad = false;
        for (int j = 0; j < sz(op[x]); ++j) {
            char y = op[x][j];
            if (cnt[y]) {
                ans.clear();
                memset(cnt, 0, sizeof cnt);
                bad = true;
                break;
            }
        }
        if (bad) continue;
        ans.push_back(x);
        ++cnt[x];
    }
    printf("[");
    for (int i = 0; i < sz(ans); ++i) {
        printf("%c", ans[i]);
        if (i + 1 < sz(ans)) printf(", ");
    }
    printf("]\n");
}

//#define SMALL
#define LARGE
//#define DEBUG

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt1.in", "r", stdin);
    freopen(TASK "-small-attempt1.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);

        printf("Case #%d: ", test);
        
        cin >> c;
        for (int i = 0; i < c; ++i)
            cin >> comb[i];
        cin >> d;
        for (int i = 0; i < d; ++i)
            cin >> opp[i];
        cin >> n >> s;

        solve();
        
        fprintf(stderr, "done.\n");
    }

    return 0;
}
