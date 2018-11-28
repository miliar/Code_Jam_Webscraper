#include <iostream>
#include <cstring>

using namespace std;

long long ans, money[1010];
int g[1010], round[1010], cN, tN, r, k, n, run, pos, loop;

int runOnce(int pos, long long &ans) {
    int tmp = pos, free = k;
    while (free >= g[pos]) {
        free -= g[pos];
        ans += g[pos];
        if (++pos == n) pos = 0;
        if (pos == tmp) break;
    }
    return pos;
}

int main() {
    cin >> cN;
    for (tN = 1; tN <= cN; ++tN) {
        cin >> r >> k >> n;
        for (int i = 0; i < n; ++i) cin >> g[i];
        ans = 0;
        memset(round, -1, sizeof(round));
        run = 0;
        pos = 0;
        while (run < r && round[pos] < 0) {
            round[pos] = run++;
            money[pos] = ans;
            pos = runOnce(pos, ans);
        }
        if (run < r) {
            loop = (r - run) / (run - round[pos]);
            run += loop * (run - round[pos]);
            ans += loop * (ans - money[pos]);
            while (run < r) {
                run++;
                pos = runOnce(pos, ans);
            }
        }
        cout << "Case #" << tN << ": " << ans << endl;
    }
}
