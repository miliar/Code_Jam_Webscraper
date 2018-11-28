#include <iostream>
using namespace std;

int H, W;
int map[100][100];
char result[100][100];
int filled;

int
walk(int x, int y, char ch)
{
    int rtn = 0;
    int xx, yy, xl, yl, hl;

    xx = x;
    yy = y;
    while (1) {
//printf("checking %d:%d\n", xx, yy);
        if (ch) {
            result[xx][yy] = ch;
            filled++;
        }

        xl = -1; yl = -1;
        hl = map[xx][yy];  // lowest height

        // check north
        if (yy >= 1 && map[xx][yy-1] < hl) {
            xl = xx; yl = yy - 1;
            hl = map[xl][yl];
        }
        // check west
        if (xx >= 1 && map[xx-1][yy] < hl) {
            xl = xx - 1; yl = yy;
            hl = map[xl][yl];
        }
        // check east
        if (xx < W-1 && map[xx+1][yy] < hl) {
            xl = xx + 1; yl = yy;
            hl = map[xl][yl];
        }
        // check south
        if (yy < H-1 && map[xx][yy+1] < hl) {
            xl = xx; yl = yy + 1;
            hl = map[xl][yl];
        }
//printf("  xl=%d yl=%d\n", xl, yl);

        if (xl < 0 && yl < 0) {
            // found sink
            return result[xx][yy];
        }

        xx = xl;
        yy = yl;
    }
}

void
solve(int cases)
{
    char current;
    int x,y;
    char ch;

    // read map
    cin >> H;
    cin >> W;
    for (y = 0; y < H; y++) {
        for (x = 0; x < W; x++) {
             cin >> map[x][y];
             result[x][y] = 0;
        }
    }

    // solve
    filled = 0;
    current = 'a';
    while (filled < W * H) {
        for (y = 0; y < H; y++) {
            for (x = 0; x < W; x++) {
                if (result[x][y]) continue;
                ch = walk(x, y, 0);
                if (ch) {
                    // found sink already marked
                    walk(x, y, ch);
                } else {
                    // found sink not marked
                    walk(x, y, current++);
                }
            }
        }
    }

    // output result
    cout << "Case #" << cases << ":" << endl;
    for (y = 0; y < H; y++) {
        for (x = 0; x < W; x++) {
            cout << result[x][y] << " ";
        }
        cout << endl;
    }
}

int
main()
{
    int N, i;

    cin >> N;
    for (i = 0; i < N; i++) {
        solve(i + 1);
    }

}
