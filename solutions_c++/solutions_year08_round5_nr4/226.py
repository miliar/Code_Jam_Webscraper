#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

int DX[2] = { 2, 1 };
int DY[2] = { 1, 2 };

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        int H, W, R;
        cin >> H >> W >> R;
        vector<vector<LL> > field(H + 2, vector<LL>(W + 2, 0LL));
        for (int i = 0; i < R; ++i) {
            int y, x;
            cin >> y >> x;
            --y; --x;
            field[y][x] = -1LL;
        }
        field[0][0] = 1LL;

        for (int y = 0; y < H; ++y)
            for (int x = 0; x < W; ++x)
                if (field[y][x] > 0LL) {
                    LL v = field[y][x];
                    for (int d = 0; d < 2; ++d) {
                        int dx = DX[d];
                        int dy = DY[d];
                        int nx = x + dx;
                        int ny = y + dy;
                        if (field[ny][nx] >= 0LL) {
                            field[ny][nx] += v;
                            field[ny][nx] %= 10007LL;
                        }
                    }
                }

        cout << "Case #" << cs + 1 << ": " << field[H-1][W-1] << '\n';
    }

    return 0;
}
