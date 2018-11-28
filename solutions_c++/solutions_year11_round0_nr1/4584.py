#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>

using namespace std;

int o[111];
int b[111];

int main()
{
    int t, n, k, cnt = 0;
    char c;

    freopen("A-large.in", "r", stdin);
    freopen("data.out", "w", stdout);

    cin >> t;

    while (t--) {
        cin >> n;
        o[0] = b[0] = 1;
        for (int i = 1; i <= n; i++) {
            cin >> c >> k;
            if (c == 'O')
                o[i] = k;
            else b[i] = k;
        }
        int time = 0, preTime = 0, tt, preO = 0, preB = 0;
        for (int i = 1; i <= n; i++) {
            if (o[i]) {
                tt = (int)abs((float)o[i] - o[preO]) + 1;
                if (o[i - 1]) {
                    preTime += tt;
                    time += tt;
                }
                else {
                    if (preTime < tt) preTime = tt - preTime;
                    else preTime = 1;
                    time += preTime;
                }
                preO = i;
            }
            else {
                tt = (int)abs((float)b[i] - b[preB]) + 1;
                if (b[i - 1]) {
                    preTime += tt;
                    time += tt;
                }
                else {
                    if (preTime < tt) preTime = tt - preTime;
                    else preTime = 1;
                    time += preTime;
                }
                preB = i;
            }
        }
        cout << "Case #" << ++cnt << ": " << time << endl;
        memset(o, 0, sizeof(o));
        memset(b, 0, sizeof(b));
    }
}
