// greedy

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <set>

using namespace std;

const int smax = 101;
const int qmax = 1001;

int s, q, ans;
set < string > server;
set < string > cur;
string r;
char str[10000];

void init() {
    ans = 0;
    server.clear();
    scanf("%d\n", &s);
    for (int i = 0; i < s; ++i) {
        fgets(str, 10000, stdin);
        r = "";
        for (int j = 0; str[j] != '\0'; ++j) {
            r += str[j];
        }
        server.insert(r);
    }
}

void solve() {
    scanf("%d\n", &q);
    cur.clear();
    for (int i = 0; i < q; ++i) {
        fgets(str, 10000, stdin);
        r = "";
        for (int j = 0; str[j] != '\0'; ++j) {
            r += str[j];
        }

        cur.insert(r);
        if ((int)cur.size() == s) {
            ans++;
            cur.clear();
            cur.insert(r);
        }
    }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int test_cnt;
    scanf("%d", &test_cnt);
    for (int test_id = 0; test_id < test_cnt; ++test_id) {
        init();
        solve();
        printf("Case #%d: %d\n", test_id + 1, ans);
    }

    return 0;
}
