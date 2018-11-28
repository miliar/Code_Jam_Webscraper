#include <iostream>
#include <cstdio>

using namespace std;

int T, tc;
int n, pd, pg;
int d, wd, g, wg;
bool  broken;

int main() {
    freopen("E:\\A-small-attempt0.in", "r", stdin);
    freopen("E:\\A-small.out", "w", stdout);
    cin >> T;
    for (tc = 1; tc <= T; tc++) {
        cin >> n >> pd >> pg;
        broken = true;
        for (d = 1; d <= n; d++) {
            if ((pd * d) % 100 != 0) continue;
            else {
                wd = pd * d / 100;
                if ((wd != 0 && pg == 0)
                  || wd != d && pg == 100) broken = true;
                else broken = false;
            }
            if (!broken) break;
        }
        cout << "Case #" << tc << ": ";
        if (broken) cout << "Broken";
        else cout << "Possible";
        cout << endl;
    }
    return 0;
}
