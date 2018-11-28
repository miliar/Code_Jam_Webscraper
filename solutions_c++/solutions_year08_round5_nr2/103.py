#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <cassert>
#include <set>
using namespace std;

struct Pos
{
    int x, y, bx, by, yx, yy;
    Pos(int x, int y, int bx, int by, int yx, int yy)
        : x(x), y(y), bx(bx), by(by), yx(yx), yy(yy) {}

    bool operator<(Pos rhs) const {
        if (x != rhs.x) return x < rhs.x;
        if (y != rhs.y) return y < rhs.y;
        if (bx != rhs.bx) return bx < rhs.bx;
        if (by != rhs.by) return by < rhs.by;
        if (yx != rhs.yx) return yx < rhs.yx;
        return yy < rhs.yy;
    }
};

const int DX[4] = { 1, 0, -1, 0 };
const int DY[4] = { 0, 1, 0, -1 };

void portalPositions(const vector<string>& field, int H, int W, int ix, int iy,
                     vector<pair<int, int> >& out)
{
    for (int d = 0; d < 4; ++d) {
        int dx = DX[d];
        int dy = DY[d];
        int x = ix;
        int y = iy;
        while (field[y][x] != '#') {
            x += dx * 2;
            y += dy * 2;
        }
        x -= dx;
        y -= dy;
        out.push_back(make_pair(x, y));
    }
    return;
}

void portalOut(const vector<string>& field, int px, int py, int& ox, int& oy)
{
    for (int d = 0; d < 4; ++d) {
        int dx = DX[d];
        int dy = DY[d];
        if (field[py + dy][px + dx] == '#') {
            ox = px - dx;
            oy = py - dy;
            return;
        }
    }
    assert(false);
    return;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cs = 0; cs < cases; ++cs) {
        int H, W;
        cin >> H >> W;

        int AH = (H + 2) * 2 - 1;
        int AW = (W + 2) * 2 - 1;
        vector<string> field(AH, string(AW, '.'));
        for (int x = 0; x < AW; ++x) {
            field[0][x] = '#';
            field[AH-1][x] = '#';
        }
        for (int y = 0; y < AH; ++y) {
            field[y][0] = '#';
            field[y][AW-1] = '#';
        }

        int sx = -1, sy = -1;
        int gx = -1, gy = -1;

        for (int py = 0; py < H; ++py) {
            string line;
            cin >> line;
            int y = py * 2 + 2;
            for (int px = 0; px < W; ++px) {
                int x = px * 2 + 2;
                field[y][x] = line[px];
                if (line[px] == 'O') {
                    sx = x;
                    sy = y;
                    field[y][x] = '.';
                }
                if (line[px] == 'X') {
                    gx = x;
                    gy = y;
                    field[y][x] = '.';
                }
            }
        }

        cout << "Case #" << cs + 1 << ": ";

        priority_queue<pair<int, Pos> > pq;
        set<Pos> visited;
        bool done = false;
        pq.push(make_pair(0, Pos(sx, sy, -1, -1, -1, -1)));

        while (!pq.empty()) {
            pair<int, Pos> pr = pq.top(); pq.pop();
            int negScore = pr.first;
            Pos pos = pr.second;

            if (pos.x == gx && pos.y == gy) {
                cout << -negScore << '\n';
                done = true;
                break;
            }

            if (visited.find(pos) != visited.end())
                continue;
            visited.insert(pos);

            vector<pair<int, int> > portpos;
            portalPositions(field, H, W, pos.x, pos.y, portpos);

            for (int p = 0; p < 4; ++p) {
                int px = portpos[p].first;
                int py = portpos[p].second;

                if (pos.yx != px || pos.yy != py) {
                    Pos npos(pos);
                    npos.bx = px;
                    npos.by = py;
                    pq.push(make_pair(negScore, npos));
                }
                if (pos.bx != px || pos.by != py) {
                    Pos npos(pos);
                    npos.yx = px;
                    npos.yy = py;
                    pq.push(make_pair(negScore, npos));
                }
            }

            for (int d = 0; d < 4; ++d) {
                int x = pos.x;
                int y = pos.y;
                int dx = DX[d] * 2;
                int dy = DY[d] * 2;
                if (field[y + dy][x + dx] != '#') {
                    Pos npos(pos);
                    npos.x += dx;
                    npos.y += dy;
                    pq.push(make_pair(negScore - 1, npos));
                }
            }

            if (pos.bx != -1 && pos.yx != -1) {
                int x = pos.x;
                int y = pos.y;
                for (int d = 0; d < 4; ++d) {
                    int dx = DX[d];
                    int dy = DY[d];

                    if (x + dx == pos.bx && y + dy == pos.by) {
                        int nx, ny;
                        portalOut(field, pos.yx, pos.yy, nx, ny);
                        Pos npos(pos);
                        npos.x = nx;
                        npos.y = ny;
                        pq.push(make_pair(negScore - 1, npos));
                    }
                    if (x + dx == pos.yx && y + dy == pos.yy) {
                        int nx, ny;
                        portalOut(field, pos.bx, pos.by, nx, ny);
                        Pos npos(pos);
                        npos.x = nx;
                        npos.y = ny;
                        pq.push(make_pair(negScore - 1, npos));
                    }
                }
            }
        }

        if (!done) {
            cout << "THE CAKE IS A LIE\n";
        }
    }

    return 0;
}
