#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int map[100][100], destx[100][100], desty[100][100];
bool flagged[100][100];
char alp[100][100];
int dx[4] = {-1, 0, 0, 1}, dy[4] = {0, -1, 1, 0};
int n, m, nowcase, Tn;

void read() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++) scanf("%d", &map[i][j]);
    memset(destx, 0xff, sizeof(destx));
    memset(desty, 0xff, sizeof(desty));
    memset(flagged, 0, sizeof(flagged));
}

inline bool valid(int x, int y) {
    return x >= 0 && y >= 0 && x < n && y < m;
}

void dfs(int x, int y) {
    if (destx[x][y] >= 0) return;

    int min = 100000, nx, ny;
    for (int dir = 0; dir < 4; dir ++) {
        nx = x + dx[dir];
        ny = y + dy[dir];
         //   printf("%d %d ^ %d %d", x, y, nx, ny);
        if (valid(nx, ny) && map[nx][ny] < map[x][y] && map[nx][ny] < min) min = map[nx][ny];
    }
    //printf("%d %d %d", x, y, min);
    if (min == 100000) {
        destx[x][y] = x;
        desty[x][y] = y;
        return;
    }
    //printf("%d %d [] %d", x, y, min);
    for (int dir = 0; dir < 4; dir ++) {
        nx = x + dx[dir];
        ny = y + dy[dir];
        if (valid(nx, ny) && map[nx][ny] == min) {
            //printf("%d %d ^ %d %d", x, y, nx, ny);
            dfs(nx, ny);
            destx[x][y] = destx[nx][ny];
            desty[x][y] = desty[nx][ny];
            break;
        }
    }
}

void work() {
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            dfs(i, j);

   // for (int i = 0; i < n; i ++)
    //    for (int j = 0; j < m; j ++)
            //printf("%d %d : %d %d\n", i, j, destx[i][j], desty[i][j]);

    char base = 'a';
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m;j ++)
            if (!flagged[i][j]) {
                alp[i][j] = base;
                flagged[i][j] = 1;
                for (int l = 0; l < n; l ++)
                    for (int k = 0; k < m; k ++)
                        if (destx[i][j] == destx[l][k] && desty[i][j] == desty[l][k]) {
                            alp[l][k] = alp[i][j];
                            flagged[l][k] = 1;
                        }
                base ++;
            }

    printf("Case #%d:\n", nowcase);
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m - 1; j ++) printf("%c ", alp[i][j]);
        printf("%c\n", alp[i][m - 1]);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &Tn);
    for (nowcase = 1; nowcase <= Tn; nowcase ++) {
        read();
        work();
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
