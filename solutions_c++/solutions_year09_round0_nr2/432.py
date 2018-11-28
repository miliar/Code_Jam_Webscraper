#include <iostream>
using namespace std;

const int maxh = 110;
const int maxw = 110;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int T;
int w, h;

int now_b;

int a[maxh][maxw];
int b[maxh][maxw];

bool ok(const int &x, const int &y) {
    return x >= 0 && x < h && y >= 0 && y < w;
}

int basin(int x, int y) {
    if (b[x][y] != -1)
        return b[x][y];
        
    int lower[4];
    int cnt_lower = 0;
    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (ok(nx, ny) && a[nx][ny] < a[x][y]) {
            if (cnt_lower == 0 || a[nx][ny] == a[x + dx[lower[0]]][y + dy[lower[0]]]) {
                lower[cnt_lower++] = i;   
            } else if (a[nx][ny] < a[x + dx[lower[0]]][y + dy[lower[0]]]) {
                lower[0] = i;
                cnt_lower = 1;
            }
        }
    }
    if (cnt_lower == 0)
        return b[x][y] = now_b++;
    return b[x][y] = basin(x + dx[lower[0]], y + dy[lower[0]]);
}

int main() {
    scanf("%d", &T);
    for (int ca = 0; ca < T; ++ca) {
        printf("Case #%d:\n", ca + 1);
        
        scanf("%d%d", &h, &w);
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                scanf("%d", &a[i][j]);
            }
        }
        memset(b, -1, sizeof(b));
        now_b = 0;
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                printf("%c", basin(i, j) + 'a');
                if (j < w - 1)
                    printf(" ");
            }
            printf("\n");
        }
    }
    return 0;
}
