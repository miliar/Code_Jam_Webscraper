//#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#include <set>
#include <map>
using namespace std;

map<string, int> s;
bool us[105];
int cs;

inline void input() {
    s.clear();
    char buf[105];
    scanf("%d\n", &cs);
    for (int i = 0; i < cs; ++i) {
        gets(buf);
        s.insert(make_pair(string(buf), i));
    }
}

inline void solve(int t) {
    int q;
    scanf("%d\n", &q);
    int ans = 0;
    for (int i = 0; i < cs; ++i)
        us[i] = 0;
    int p = cs;
    char buf[105];
    for (int i = 0; i < q; ++i) {
        gets(buf);
        string str(buf);
        int idx = s.find(str)->second;
        if (us[idx])
            continue;
        us[idx] = 1;
        --p;
        if (!p) {
            ++ans;
            for (int i = 0; i < cs; ++i)
                us[i] = 0;
            us[idx] = 1;
            p = cs - 1;
        }
    }
    printf("Case #%d: %d\n", t, ans);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
    scanf("%d\n", &t);
    for (int i = 1; i <= t; ++i) {
        input();
        solve(i);
    }
	return 0;
}
