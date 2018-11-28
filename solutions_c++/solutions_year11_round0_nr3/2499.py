#pragma comment(linker, "/STACK:25000000")
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> pi;
typedef unsigned long long ull;

#define x first
#define y second
#define mp make_pair

void solution(int tstNum) {  
    int n, c[1000] = {0};
    int ans[1 << 20] = {0};
    scanf("%d", &n);
    int tot = 0;
    int summ = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%d", &c[i]);        
        tot ^= c[i];
        summ += c[i];
    }
    set<int> q;

    for (int i = 0; i < n; ++i) {
        q.insert(c[i]);
        if (ans[c[i]] == 0 || ans[c[i]] > c[i]) {
            ans[c[i]] = c[i];
        }
    }

    for (int i = 0; i < n; ++i) {
        for (set<int>::iterator it = q.begin(); it != q.end(); ++it) {
            int curr = *it;
            int nxt = curr ^ c[i];
            if (ans[nxt] == 0 || ans[nxt] > ans[curr] + c[i]) {
                ans[nxt] = ans[curr] + c[i];
            }
        }
    }
    int res = -1;

    for (int i = 0; i < 1 << 20; ++i) {
        if (ans[i] && ((i ^ tot) == i)) {
            res = max(res, summ - ans[i]);
        }
    }

    if (res == -1) {
        printf("NO\n");
    } else {
        printf("%d\n", res);
    }
}

int main() {

    //freopen("in.in", "rt", stdin);
    //freopen("out.out", "wt", stdout);

    //freopen("C-small.in", "rt", stdin);
    //freopen("C-small.out", "wt", stdout);

    freopen("C-large.in", "rt", stdin);
    freopen("C-large.out", "wt", stdout);

    int t = 0;
    scanf("%d", &t);
    for (int tt = 0; tt < t; tt++) {
        printf("Case #%d: ", tt + 1);
        solution(tt);
    }

    return 0;
}