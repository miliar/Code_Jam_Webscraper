#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;

const int mv[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int R, C, N, h[100 * 100], f[100 * 100], id[100 * 100];

int fa(int i) {
    return f[i] == i ? i : (f[i] = fa(f[i]));
}

void Main() {
    cin >> R >> C;
    N = R * C;
    for (int i = 0; i < N; ++i)
        cin >> h[i];
    for (int i = 0; i < N; ++i) {
        int x0 = i / C, y0 = i % C, best = h[i], bp = i;
        for (int d = 0; d < 4; ++d) {
            int x = x0 + mv[d][0], y = y0 + mv[d][1];
            if (!(0 <= x && x < R && 0 <= y && y < C)) continue;
            int j = x * C + y;
            if (h[j] < best) {
                best = h[j];
                bp = j;
            }
        }
        f[i] = bp;
    }
    for (int i = 0; i < N; ++i)
        f[i] = fa(i);
    fill(id, id + N, -1);
    int used = 0;
    for (int i = 0; i < N; ++i)
        if (id[f[i]] == -1)
            id[f[i]] = used++;
    for (int x = 0, i = 0; x < R; ++x) {
        for (int y = 0; y < C; ++y, ++i) {
            if (y) cout.put(' ');
            cout.put('a' + id[f[i]]);
        }
        cout << endl;
    }
}

int main(int argc, char* argv[]) {
    freopen((string(argv[1]) + ".in").c_str(), "r", stdin);
    freopen((string(argv[1]) + ".out").c_str(), "w", stdout);

    int ccc, c = 0;
    for (cin >> ccc; ccc-- > 0;) {
        cout << "Case #" << ++c << ":" << endl;
        Main();
    }
    return 0;
}
