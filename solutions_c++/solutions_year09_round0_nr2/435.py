
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int dr[] = {-1, 0, 0, 1};
const int dc[] = {0, -1, 1, 0};

int getRoot(int at, vector <int> &parent) {
    return parent[at] == -1 ? at : parent[at] = getRoot(parent[at], parent);
}

int main() {
    int tst;
    cin >> tst;
    for (int cas = 0; cas < tst; ++cas) {
        int H, W;
        cin >> H >> W;
        vector <vector <int> > map(H, vector <int>(W));
        for (int r = 0; r < H; ++r)
            for (int c = 0; c < W; ++c)
                cin >> map[r][c];
        vector <int> parent(H * W, -1);
        for (int r = 0; r < H; ++r)
            for (int c = 0; c < W; ++c) {
                int br = -1;
                int bc = -1;
                int best = map[r][c];
                for (int dir = 0; dir < 4; ++dir) {
                    int nr = r + dr[dir];
                    int nc = c + dc[dir];
                    if (nr < 0 || nr >= H || nc < 0 || nc >= W || map[nr][nc] >= best)
                        continue;
                    br = nr;
                    bc = nc;
                    best = map[nr][nc];
                }
                if (br >= 0) {
                    int x = getRoot(r * W + c, parent);
                    int y = getRoot(br * W + bc, parent);
                    if (x != y)
                        parent[x] = y;
                }
            }
        vector <string> res(H, string(W, '?'));
        int cnt = 0;
        for (int r = 0; r < H; ++r)
            for (int c = 0; c < W; ++c)
                if (res[r][c] == '?') {
                    res[r][c] = (char)(cnt + 'a');
                    for (int r2 = 0; r2 < H; ++r2)
                        for (int c2 = 0; c2 < W; ++c2)
                            if (getRoot(r * W + c, parent) == getRoot(r2 * W + c2, parent)) {
                                res[r2][c2] = (char)(cnt + 'a');
                            }
                    ++cnt;
                }
        cout << "Case #" << cas + 1 << ":" << endl;
        for (int r = 0; r < H; ++r)
            for (int c = 0; c < W; ++c)
                printf("%c%c", res[r][c], c < W - 1 ? ' ' : '\n');
    }
    return 0;
}