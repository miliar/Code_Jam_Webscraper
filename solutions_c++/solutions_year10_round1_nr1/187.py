#include <iostream>
#include <vector>
using namespace std;

typedef vector<char> Vc;
typedef vector<Vc> Mc;

const int diri[4] = { 0, 1, 1, 1 };
const int dirj[4] = { 1, 1, 0, -1 };

int N, K;
Mc m;

int llarg(int x, int y, int dx, int dy) {
    char c = m[x][y];
    int p = 1;
    while (x + p*dx >= 0 and x + p*dx < N and
           y + p*dy >= 0 and y + p*dy < N and
           m[x + p*dx][y + p*dy] == c) ++p;
    return p;
}

int main() {
    int tcas;
    cin >> tcas;
    for (int cas = 1; cas <= tcas; ++cas) {
        cin >> N >> K;
        m = Mc(N, Vc(N));
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                cin >> m[i][j];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                int t = -1;
                for (int k = j; t == -1 and k < N; ++k)
                    if (m[i][N - k - 1] != '.') t = k;
                if (t != -1) swap(m[i][N - j - 1], m[i][N - t - 1]);
            }
        }
        /*for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) cerr << m[i][j];
            cerr << endl;
        }
        cerr << endl;*/
        int maxb = 0, maxr = 0;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j) {
                if (m[i][j] == 'B') {
                    for (int k = 0; k < 4; ++k)
                        maxb = max(maxb, llarg(i, j, diri[k], dirj[k]));
                }
                else if (m[i][j] == 'R') {
                    for (int k = 0; k < 4; ++k)
                        maxr = max(maxr, llarg(i, j, diri[k], dirj[k]));
                }
            }
        cout << "Case #" << cas << ": ";
        if (maxb >= K and maxr >= K) cout << "Both" << endl;
        else if (maxb >= K) cout << "Blue" << endl;
        else if (maxr >= K) cout << "Red" << endl;
        else cout << "Neither" << endl;
    }
}
