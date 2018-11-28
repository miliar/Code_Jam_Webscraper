#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_H = 105;
const int MAX_W = 105;
const int MAX_ALT = 20000;

int map[MAX_H][MAX_W];
int sinkmap[MAX_H][MAX_W];
char cmap[MAX_ALT];
int current_sink;

int find_sinks(int i, int j) {
    if (sinkmap[i][j] == -1) {
        int m = min(map[i + 1][j], min(map[i][j + 1], min(map[i - 1][j], map[i][j - 1])));

        if (m < map[i][j]) {
            if (map[i - 1][j] == m) {
                sinkmap[i][j] = find_sinks(i - 1, j);
            } else if (map[i][j - 1] == m) {
                sinkmap[i][j] = find_sinks(i, j - 1);
            } else if (map[i][j + 1] == m) {
                sinkmap[i][j] = find_sinks(i, j + 1);
            } else if (map[i + 1][j] == m) {
                sinkmap[i][j] = find_sinks(i + 1, j);
            }
            return sinkmap[i][j];
        } else {
            sinkmap[i][j] = current_sink++;
            return sinkmap[i][j];
        }
    } else {
        return sinkmap[i][j];
    }
}

int main() {
    int t, h, w;
    char current;

    scanf("%d", &t);
    for (int c = 0; c < t; ++c) {

        scanf("%d%d", &h, &w);
        for (int i = 1; i <= h; ++i)
            for (int j = 1; j <= w; ++j)
                scanf("%d", &map[i][j]);

        current = 'a';
        current_sink = 0;
        for (int i = 0; i < MAX_ALT; ++i)
            cmap[i] = 0;
        for (int i = 0; i < MAX_H; ++i)
            for (int j = 0; j < MAX_W; ++j)
                sinkmap[i][j] = -1;

        for (int i = 0; i <= w + 1; ++i)
            map[0][i] = map[h + 1][i] = MAX_ALT;
        for (int i = 0; i <= h + 1; ++i)
            map[i][0] = map[i][w + 1] = MAX_ALT;

        printf("Case #%d:\n", c + 1);
        for (int i = 1; i <= h; ++i) {
            for (int j = 1; j <= w; ++j) {
                int sink = find_sinks(i, j);
                if (cmap[sink] == 0) {
                    cmap[sink] = current++;
                }
                printf("%c ", cmap[sink]);
            }
            printf("\n");
        }
    }
    return 0;
}
