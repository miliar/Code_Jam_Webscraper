#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 512;

typedef long long i64;

int H, W, D;

int weight[MAX][MAX];
int sumH[MAX][MAX], sumV[MAX][MAX];

int h_range(int y, int x1, int x2) {
    if (x1 > x2)
        swap(x1, x2);
    return sumH[y][x2] - (x1 > 0 ? sumH[y][x1-1] : 0);
}

int v_range(int x, int y1, int y2) {
    if (y1 > y2)
        swap(y1, y2);
    return sumV[y2][x] - (y1 > 0 ? sumV[y1-1][x] : 0);
}

void solve()
{
    scanf("%d %d %d", &H, &W, &D);
    for (int y = 0; y < H; y++) {
        for (int x = 0; x < W; x++) {
            int ch;
            do {
                ch = getchar();
            } while (!isdigit(ch));

            weight[y][x] = D + ch - '0';
        }
    }

    for (int y = 0; y < H; y++) {
        //        puts("");
        for (int x = 0; x < W; x++) {
            sumH[y][x] = (x > 0 ? sumH[y][x-1] : 0) + weight[y][x];
            sumV[y][x] = (y > 0 ? sumV[y-1][x] : 0) + weight[y][x];

            //            printf("%4d", weight[y][x]);
        }
    }


    for (int k = min(H, W); k >= 3; k--) {
        int k2 = k/2;
        for (int x = 0; x+k <= W; x++) {
            int x2 = x+k-1;
            for (int y = 0; y+k <= H; y++) {
                int y2 = y+k-1;
                int lev = k-1;

                {
                    i64 dx = lev * i64(v_range(x, y+1, y2-1) - v_range(x2, y+1, y2-1));
                    for (int i = 1; i < k2; i++)
                        dx += (lev-i-i) * i64(v_range(x+i, y, y2) - v_range(x2-i, y, y2));
                    if (dx != 0)
                        continue;
                }

                {
                    i64 dy = lev * i64(h_range(y, x+1, x2-1) - h_range(y2, x+1, x2-1));
                    for (int i = 1; i < k2; i++)
                        dy += (lev-i-i) * i64(h_range(y+i, x, x2) - h_range(y2-i, x, x2));
                    if (dy != 0)
                        continue;
                }

                printf("%d\n", k, x, y);
                return;
            }
        }
    }

    puts("IMPOSSIBLE");
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        printf("Case #%d: ", i+1);
        solve();
    }
}
