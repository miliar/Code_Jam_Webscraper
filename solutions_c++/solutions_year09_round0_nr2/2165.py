#include <iostream.h>

char bt(int x, int y, int map[][101], char res[][101], char &c) {
    if(res[x][y] >= 'a') return res[x][y];
    int nx = x, ny = y;
    if(x > 0 && map[x-1][y] < map[nx][ny]) {
        nx = x-1;
        ny = y;
    }
    if(y > 0 && map[x][y-1] < map[nx][ny]) {
        nx = x;
        ny = y-1;
    }
    if(map[x][y+1] < map[nx][ny]) {
        nx = x;
        ny = y+1;
    }
    if(map[x+1][y] < map[nx][ny]) {
        nx = x+1;
        ny = y;
    }
    if(x == nx && y == ny) {
        res[x][y] = c++;
    } else {
        res[x][y] = bt(nx, ny, map, res, c);
    }
/*
        cout << "x:" << x << " y:" << y << " c:" << c << "\n";
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                cout << res[i][j] << " ";
            }
            cout << "\n";
        }
*/
    return res[x][y];
}

int main() {
    int N;
    cin >> N;

    for(int n = 1; n <= N; n++) {
        int h, w;
        int map[101][101];
        char res[101][101];
        cin >> h >> w;
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                cin >> map[i][j];
                res[i][j] = '0';
            }
            map[i][w] = 99999;
        }
        for(int j = 0; j < w; j++) map[h][j] = 99999;

        char c = 'a';
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                bt(i, j, map, res, c);
            }
        }

        cout << "Case #" << n << ":\n";
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                cout << res[i][j] << " ";
            }
            cout << "\n";
        }
    }
}
