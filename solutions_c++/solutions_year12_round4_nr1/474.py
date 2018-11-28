#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define printf_debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define printf_debug(fmt, args...)
#endif

typedef long long llong;

using namespace std;

#define MAXN 10010

llong d[MAXN], l[MAXN];
llong to[MAXN];
int n;
llong D;

void solve() {
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> d[i] >> l[i];
        to[i] = 0;
    }
    cin >> D;
    llong mx = 0;
    to[0] = d[0];
    for(int i = 0; i < n; i++) {
        mx = max(mx, d[i] + to[i]);
        for(int j = i + 1; j < n; j++) {
            if(d[i] + to[i] >= d[j]) {
                to[j] = max(to[j], min(l[j], abs(d[j] - d[i])));
            }
        }
    }
    if(mx >= D) {
        cout << " YES" << endl;
    } else {
        cout << " NO" << endl;
    }
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cout << "Case #" << t << ":";
        solve();
    }
    return 0;
}
