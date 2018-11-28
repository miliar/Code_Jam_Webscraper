#include <iostream>
#include <cstdio>

using namespace std;
int C, TC, R;
int map[200][200];
int change[200][200];
int result;
int bcount;

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-out0.txt", "w", stdout);
    cin >> C;
    int i, j, k, x1, y1, x2, y2;
    for (TC = 1; TC <= C; TC++) {
        for (i = 0; i < 200; i++)
            for (j = 0; j < 200; j++)
                map[i][j] = change[i][j] = 0;
        cin >> R;
        for (k = 0; k < R; k++) {
            cin >> x1 >> y1 >> x2 >> y2;
            for (i = x1; i <= x2; i++)
                for (j = y1; j <= y2; j++) map[i][j] = 1;
        }
        bcount = 0;
        for (i = 0; i < 200; i++)
            for (j = 0; j < 200; j++)
                bcount += map[i][j];
        result = 0;
        while (bcount) {
            for (i = 0; i < 200; i++)
                for (j = 0; j < 200; j++) {
                    change[i][j] = 0;
                    if (map[i][j] == 1
                            && map[i - 1][j] == 0
                            && map[i][j - 1] == 0) change[i][j] = -1;
                    if (map[i][j] == 0
                            && map[i - 1][j] == 1
                            && map[i][j - 1] == 1) change[i][j] = 1;
                    bcount += change[i][j];
                }
            for (i = 0; i < 200; i++)
                for (j = 0; j < 200; j++)
                    map[i][j] += change[i][j];
            result++;
        }
        cout << "Case #" << TC << ": " << result << endl;
    }
    return 0;
}
