#include <iostream>
using namespace std;

void min4(int map[102][102], int &i, int &j) {
    int a = i - 1, b = j;
    if (map[i][j-1] < map[a][b]) {
        a = i;
        b = j - 1;
    }
    if (map[i][j+1] < map[a][b]) {
        a = i;
        b = j + 1;
    }
    if (map[i+1][j] < map[a][b]) {
        a = i + 1;
        b = j;
    }

    i = a;
    j = b;
}

void makePath(int map[102][102], char mapC[100][101], int i, int j, char &bassin) {
    int a = i, b = j;
    min4(map, a, b);
    if (map[a][b] < map[i][j]) {
        if (mapC[a-1][b-1] == '\0')
            makePath(map, mapC, a, b, bassin);
        mapC[i-1][j-1] = mapC[a-1][b-1];
    }
    else if (mapC[i-1][j-1] == '\0') {
        mapC[i-1][j-1] = bassin;
        ++bassin;
    }
}

int main() {
    int T, H, W, cases = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d %d", &H, &W);
        int map[102][102];
        for (int i = 0; i <= H + 1; ++i)
            map[i][0] = map[i][W+1] = 10000;
        for (int i = 0; i <= W+1; ++i)
            map[0][i] = map[H+1][i] = 10000;
        for (int i = 1; i <= H; ++i)
            for (int j = 1; j <= W; ++j)
                scanf("%d", &map[i][j]);

        char mapC[100][101];
        for (int i = 0; i < H; ++i)
            for (int j = 0; j <= W; ++j)
                mapC[i][j] = '\0';
        char bassin = 'a';
        for (int i = 1; i <= H; ++i)
            for (int j = 1; j <= W; ++j)
                makePath(map, mapC, i, j, bassin);

        printf("Case #%d:\n", ++cases);
        for (int i = 0; i < H; ++i) {
            printf("%c", mapC[i][0]);
            for (int j = 1; j < W; ++j)
                printf(" %c", mapC[i][j]);
            printf("\n");
        }
    }
}

