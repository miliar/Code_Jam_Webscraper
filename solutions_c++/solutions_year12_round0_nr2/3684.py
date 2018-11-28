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

int n, s, p, mx = 0, cs = 0, cmx = 0;
int sum[101];

void rec(int depth) {
    if(depth == n) {
        if(cs == s) {
            mx = max(mx, cmx);
        }
        return;
    }
    for(int a = 0; a <= 10; a++) {
        for(int b = 0; b <= 10; b++) {
            int c = sum[depth] - a - b;
            if(0 <= c && c <= 10) {
                int mx_apart = max(max(abs(a - b), abs(b - c)), abs(a - c));
                int mx_score = max(max(a, b), c);
                if(mx_apart <= 2) {
                    cs += (mx_apart == 2);
                    cmx += (mx_score >= p);
                    rec(depth + 1);
                    cmx -= (mx_score >= p);
                    cs -= (mx_apart == 2);
                }
            }
        }
    }
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        mx = 0;
        cin >> n >> s >> p;
        for(int i = 0; i < n; i++) {
            cin >> sum[i];
        }
        rec(0);
        cout << "Case #" << t + 1 << ": " << mx << endl;
    }
    return 0;
}
