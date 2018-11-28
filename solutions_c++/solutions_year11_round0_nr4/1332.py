#include <cmath>
#include <iostream>
#include <string>
using namespace std;
#define MAXN 1010

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int id = 1; id <= t; id++) {
        int n, a[MAXN];
        bool were[MAXN];
        int ans = 0;
        cin >> n;
        for(int i = 1; i <= n; i++) {
            cin >> a[i];
            were[i] = false;
        }
        for(int i = 1; i <= n; i++) {
            int t = a[i], cnt = 1;
            if(were[t]) continue;
            were[t] = true;
            while(t != i) {
                t = a[t];
                were[t] = true;
                cnt++;
            }
            if(cnt == 1) continue;
            ans += cnt;
        }
        printf("Case #%d: %lf\n", id, double(ans));
    }
    return 0;
}
