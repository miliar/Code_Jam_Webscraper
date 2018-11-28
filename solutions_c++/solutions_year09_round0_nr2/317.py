#include <cstdio>
#include <cstring>

using namespace std;

int dir[5][2] = {{-1,0}, {0,-1}, {0,1}, {1,0}, {0,0}};
int T, H, W;
int map[102][102];
int label[102][102];
char labelchar[50];
int labelnum = 0;

bool flow(int x, int y, int d) {
    return map[x][y] > map[x+dir[d][0]][y+dir[d][1]];
}

int flowdir(int x, int y) {
    if (x == 0 || x == H+1 || y == 0 || y == W+1) return 0;
    int min = 100000000;
    int mind = 0;
    for (int d = 0; d < 4; d++) {
        if (min > map[x+dir[d][0]][y+dir[d][1]]) {
            min = map[x+dir[d][0]][y+dir[d][1]];
            mind = d;
        }
    }
    if (flow(x,y,mind))
        return mind;
    else
        return 4;
}

void DFS(int x, int y, int l) {
    if (x == 0 || x == H+1 || y == 0 || y == W+1) return;
    if (label[x][y] != -1) return;
    label[x][y] = l;
    for (int d = 0; d < 4; d++) {
        int f = flowdir(x+dir[d][0], y+dir[d][1]);
        if (dir[f][0] + dir[d][0] == 0 && dir[f][1] + dir[d][1] == 0) {
            DFS(x+dir[d][0], y+dir[d][1], l);
        }
    }
}

void solve() {
    scanf("%d %d", &H, &W);
    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            scanf("%d", &map[i][j]);
        }
    }
    for (int i = 1; i <= H; i++) {
        map[i][0] = map[i][1];
        map[i][W+1] = map[i][W];
    }
    for (int i = 1; i <= W; i++) {
        map[0][i] = map[1][i];
        map[H+1][i] = map[H][i];
    }

    memset(label, -1, sizeof(label));
    labelnum = 0;
    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            bool sink = 1;
            for (int k = 0; k < 4; k++) {
                sink = sink && !flow(i, j, k);
            }
            if (sink) {
//printf("DFS %d %d %d\n", i, j, labelnum);
                DFS(i, j, labelnum++);
            }
        }
    }

    memset(labelchar, 0, sizeof(labelchar));
    char curr = 'a';
    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            if (labelchar[label[i][j]] == 0) {
                labelchar[label[i][j]] = curr++;
            }
            printf("%c", labelchar[label[i][j]]);
            if (j != W) printf(" ");
        }
        printf("\n");
    }
}

int main() {
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        printf("Case #%d:\n", i+1);
        solve();
    }

    return 0;
}
