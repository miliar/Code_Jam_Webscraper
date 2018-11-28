#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    int T, i;
    scanf("%d", &T);
    for (i = 1; i <= T; ++i) {
        char c[4][5], ans, a[2] = {'O', 'X'};
        for (int j = 0; j < 4; ++j)
            scanf("%s", c[j]);
        int state = 0, j, k;
        for (int l = 0; l < 2; ++l) {
            ans = a[l];
            for (j = 0; j < 4; ++j)
            {
                for (k = 0; k < 4; ++k)
                {
                    if (c[j][k] != ans && c[j][k] != 'T') break;
                }
                if (k == 4) state = 1;
                for (k = 0; k < 4; ++k)
                    if (c[k][j] != ans && c[k][j] != 'T') break;
                if (k == 4) state = 1;
            }
            for (k = 0; k < 4; ++k)
                if (c[k][k] != ans && c[k][k] != 'T') break;
            if (k == 4) state = 1;
            for (k = 0; k < 4; ++k)
                if (c[k][3-k] != ans && c[k][3-k] != 'T') break;
            if (k == 4) state = 1;
            if (state) break;
        }
        if (state == 0) {
            for (j = 0; j < 4; ++j)
                for (k = 0; k<4; ++k)
                    if (c[j][k] == '.')
                        state = 2;
        }
        cout << "Case #"<<i<<": ";
        if (state == 1) {
            cout << ans << " won\n";
        } else if (state == 2) {
            cout << "Game has not completed\n";
        } else {
            cout << "Draw\n";
        }
    }
    return 0;
}
