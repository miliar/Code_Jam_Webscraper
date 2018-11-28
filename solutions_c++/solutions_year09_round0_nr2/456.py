#include <iostream>
#include <cstring>

using namespace std;

const int h_max = 100 + 10, w_max = 100 + 10;

int h, w, altitude[h_max][w_max];
char label_n, label[h_max][w_max];

void solve();
char make_label(int, int);

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ":" << endl;
        solve();
    }
    return 0;
}

void solve() {
    cin >> h >> w;
    for (int i = 0; i < h; ++i)
        for (int j = 0; j < w; ++j)
            cin >> altitude[i][j];
    label_n = 'a';
    memset(label, '\0', sizeof(label));
    for (int i = 0; i < h; ++i)
        for (int j = 0; j < w; ++j)
            if (label[i][j] == '\0')
                make_label(i, j);
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w - 1; ++j)
            cout << label[i][j] << ' ';
        cout << label[i][w - 1] << endl;
    }
}

char make_label(int x, int y) {
    if (label[x][y] != '\0')
        return label[x][y];
    int _x = x, _y = y;
    if (x - 1 >= 0 && altitude[x - 1][y] < altitude[_x][_y])
        _x = x - 1, _y = y;
    if (y - 1 >= 0 && altitude[x][y - 1] < altitude[_x][_y])
        _x = x, _y = y - 1;
    if (y + 1 < w && altitude[x][y + 1] < altitude[_x][_y])
        _x = x, _y = y + 1;
    if (x + 1 < h && altitude[x + 1][y] < altitude[_x][_y])
        _x = x + 1, _y = y;
    if (_x == x && _y == y)
        return label[x][y] = label_n++;
    return label[x][y] = make_label(_x, _y);
}
