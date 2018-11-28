#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t < T) {
        printf("Case #%d: ", ++t);
        int n;
        cin >> n;
        int ca = 0, cb = 0, pa = 1, pb = 1, ans = 0;
        for(int i = 0; i < n; i++){
        char c;
            int p;
            cin >> c >> p;
            if (c == 'O') {
                ca += max(abs(pa - p) - cb, 0) + 1;
                ans += max(abs(pa - p) - cb, 0) + 1;
                pa = p;
                cb = 0;
            } else {
                cb += max(abs(pb - p) - ca, 0) + 1;
                ans += max(abs(pb - p) - ca, 0) + 1;
                pb = p;
                ca = 0;
            }
        }
        cout << ans << endl;
    }
    return 0;
}

