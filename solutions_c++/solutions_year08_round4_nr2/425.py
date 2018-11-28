#include <iostream>

using namespace std;

void go(int m, int n, int a) {
    if (a > m*n) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    int ax = 0, ay = 0;
    for (int bx = 0; bx <= m; bx++) for (int by = 0; by <= n; by++)
    for (int cx = 0; cx <= m; cx++) for (int cy = 0; cy <= n; cy++) {
        int area = (ax-cx) * (by-cy) - (bx-cx) * (ay-cy);
        if (area < 0) area = -area;
        if (area == a) {
            cout << ax << " " << ay << " " << bx << " " << by << " " << cx << " " << cy << endl;
            return;
        }
    }
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        int m, n, a; cin >> m >> n >> a;
        cout << "Case #" << t << ": ";
        go(m, n, a);
    }
    return 0;
}

