#include <cmath>
#include <iostream>
#include <string>
using namespace std;
#define MAXN 101

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int id = 1; id <= t; id++) {
        int n, a[MAXN][2], ans = 0;
        cin >> n;
        for(int i = 0; i < n; i++) {
            char c;
            cin >> c >> a[i][0];
            a[i][1] = c == 'O' ? 0 : 1;
        }
        int cur[] = {1, 1}, time[] = {0, 0};
        for(int i = 0; i < n; i++) {
            int time_passed = ans - time[a[i][1]];
            int need_moves = abs(a[i][0] - cur[a[i][1]]);
            if(need_moves > time_passed) ans += need_moves - time_passed;
            ans++;
            cur[a[i][1]] = a[i][0];
            time[a[i][1]] = ans;
        }
        printf("Case #%d: %d\n", id, ans);
    }
    return 0;
}
