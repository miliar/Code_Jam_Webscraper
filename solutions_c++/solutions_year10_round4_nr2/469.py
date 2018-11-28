#include <iostream>
#include <cstdio>

using namespace std;
int T, P;
int cost[3000];
int miss[3000];
const int pw[13] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096};
int f[3000][20];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-out.txt","w",stdout);
    cin >> T;
    int TC, k, i, a, b, flag, min;
    for (TC = 1; TC <= T; TC++) {
        cin >> P;
        for (i = 0; i < pw[P]; i++) {
            cin >> miss[i];
            if (miss[i] > P) miss[i] = P;
        }
        for (k = P; k >= 1; k--) {
            for (i = pw[k - 1]; i < pw[k]; i++) cin >> cost[i];
        }
        for (i = pw[P] - 1; i >= pw[P - 1]; i--) {
            for (k = 0; k <= P; k++) {
                a = (i - pw[P - 1])*2;
                b = a + 1;
                if (k + 1 <= miss[a] && k + 1 <= miss[b]) f[i][k] = 0;
                else if (k <= miss[a] && k <= miss[b]) f[i][k] = cost[i];
                else f[i][k] = -1;

            }
        }
        for (i = pw[P - 1] - 1; i > 0; i--) {
            for (k = 0; k <= P; k++) {
                a = i * 2;
                b = a + 1;
                flag = 0;
                min = 1000000000;
                if (f[a][k + 1] >= 0 && f[b][k + 1] >= 0) {
                    flag = 1;
                    if (f[a][k + 1] + f[b][k + 1] < min)
                        min = f[a][k + 1] + f[b][k + 1];
                }
                if (f[a][k] >= 0 && f[b][k] >= 0) {
                    flag = 1;
                    if (f[a][k] + f[b][k] + cost[i] < min)
                        min = f[a][k] + f[b][k] + cost[i];
                }
                if (!flag) f[i][k] = -1;
                else f[i][k] = min;
            }
        }
        cout << "Case #" << TC << ": ";
        cout << f[1][0] << endl;
    }
    return 0;
}
