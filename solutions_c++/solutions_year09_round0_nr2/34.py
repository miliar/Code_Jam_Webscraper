#include <iostream>

using namespace std;

const int dy[] = { 1, 0, 0, -1 };
const int dx[] = { 0, 1, -1, 0 };
const int INF = 1000000;

int rows, cols;
int a[100][100];
char sink[100][100];
int next;

char go(int i, int j) {
    if (sink[i][j] != '?') return sink[i][j];

    int best = INF;
    int r = -1, c = -1;
    for (int d = 0; d < 4; d++) {
        int ii = i + dy[d], jj = j + dx[d];
        if (ii < 0 || ii >= rows || jj < 0 || jj >= cols) continue;
        if (a[ii][jj] < a[i][j] && a[ii][jj] <= best) {
            best = a[ii][jj];
            r = ii; c = jj;
        }
    }
    if (r < 0) return (sink[i][j] = next++);
    return sink[i][j] = go(r, c);
}

int main() {
    int t; cin >> t;
    for (int c = 1; c <= t; c++) {
        cin >> rows >> cols;
        for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++) cin >> a[i][j];
        memset(sink, '?', sizeof(sink));
        next = 'a';

        cout << "Case #" << c << ":" << endl;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (j > 0) cout << ' ';
                cout << go(i, j);
            }
            cout << endl;
        }
    }
    return 0;
}

