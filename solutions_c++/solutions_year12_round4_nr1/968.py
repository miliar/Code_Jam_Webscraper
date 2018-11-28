#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAX_N = 10005;

int n;
int a[MAX_N];
int b[MAX_N];
int d;

set< pair<int, int> > S;
set< pair<int, int> > S2;

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int tests; scanf("%d", &tests);
    for (int testId = 1; testId <= tests; ++testId) {
        printf("Case #%d: ", testId);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d%d", &a[i], &b[i]);
        scanf("%d", &d);
        S.clear();
        S2.clear();
        S.insert(make_pair(2 * a[0], a[0]));
        S2.insert(make_pair(a[0], 2 * a[0]));
        for (int i = 1; i < n; ++i) {
            pair<int, int> top;
            while (!S.empty()) {
                top = *(S.begin());
                if (top.first >= a[i]) break;
                S.erase(S.begin());
                S2.erase(S2.find(make_pair(top.second, top.first)));
            }
            if (S.empty()) continue;
            top = *(S2.begin());
            int swing = min(b[i], a[i] - top.first);
            S.insert(make_pair(a[i] + swing, a[i]));
            S2.insert(make_pair(a[i], a[i] + swing));
        }
        bool ok = false;
        while (!S.empty()) {
            if ((*(S.begin())).first >= d) ok = true;
            S.erase(S.begin());
        }
        if (ok) printf("YES\n");
        else printf("NO\n");
    } 
    return 0;
}