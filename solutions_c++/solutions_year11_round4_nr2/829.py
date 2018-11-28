#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define MAXR 10

int R, C, D;
int mass[MAXR][MAXR];

bool ok(int r, int c, int k, bool inc) {
    int cc[] = { 0, 0 };

    int r_r = r+k-(inc ? 0 : 1);
    int c_r = c+k-(inc ? 0 : 1);

    if (r_r >= R || c_r >= C) return false;
    if (r-k < 0 || c-k < 0) return false;

    for (int i = r-k; i <= r_r; ++i)
        for (int j = c-k; j <= c_r; ++j) {
            if (i == r-k && (j == c-k || j == c_r)) continue;
            if (i == r_r && (j == c-k || j == c_r)) continue;
            
            cc[0] += mass[i][j] * (2*(i-r)+!inc);
            cc[1] += mass[i][j] * (2*(j-c)+!inc);
        }
    
    if (cc[0] == 0 && cc[1] == 0)
        return true;

    return false;
}

int m(int r, int c) {
    int best = -1;

    for (int k = 1; k <= min(R, C); ++k) {
        if (ok(r, c, k, true)) best = max(best, 2*k+1);
        if (ok(r, c, k, false)) best = max(best, 2*k);
    }

    return best;
}

int solve(vector<string> const& sheet) {
    int best = -1;
    int best_r = -1, best_c = -1;

    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            mass[i][j] = D + (sheet[i][j] - '0');

    for (int c_r = 1; c_r < R; ++c_r)
        for (int c_c = 1; c_c < C; ++c_c) {
            int v = m(c_r, c_c);
            if (v > best) {
                best = v;
                best_r = c_r; best_c = c_c;
            }
        }

    //    printf("%d %d: %d\n", best_r, best_c, best);

    return best;
}

int main() {
    char buf[0x1000];
    int T; scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d%d%d", &R, &C, &D);
        vector<string> sheet;
        for (int i = 0; i < R; ++i) {
            scanf("%s", buf);
            sheet.push_back(string(buf));
        }

        printf("Case #%d: ", tc);

        int sol = solve(sheet);
        if (sol == -1 || sol < 3) printf("IMPOSSIBLE"); else printf("%d", sol);

        putchar('\n');
    }

    return 0;
}
