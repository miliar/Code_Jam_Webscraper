#include <iostream>
#include <algorithm>
using namespace std;

const int INF = 1000000000;

int N;
int mat[1000][1000];

int main() {
    int tcas;
    cin >> tcas;
    for (int cas = 1; cas <= tcas; ++cas) {
        cin >> N;
        for (int d = -N + 1; d <= N - 1; ++d) {
            for (int i = N - 1; i >= 0; --i)
                for (int j = 0; j < N; ++j)
                    if (j + i - N + 1 == d) cin >> mat[i][j];
        }
//         for (int i = 0; i < N; ++i) {
//             for (int j = 0; j < N; ++j)
//                 cerr << ' ' << mat[i][j];
//             cerr << endl;
//         }
        int mini = INF;
        for (int da = -N + 1; da <= N - 1; ++da)
            for (int db = -N + 1; db <= N - 1; ++db) {
                bool ok = true;
                for (int i = 0; i < N; ++i)
                    for (int j = 0; j < N; ++j) {
                        int a = i - j;
                        int b = j + i - N + 1;
                        int ta = da - a;
                        int tb = db - b;
                        int xa = i + ta;
                        int ya = j - ta;
                        int xb = i + tb;
                        int yb = j + tb;
                        if (xa >= 0 and xa < N and ya >= 0 and ya < N) {
                            if (mat[i][j] != mat[xa][ya]) ok = false;
                        }
                        if (xb >= 0 and xb < N and yb >= 0 and yb < N) {
                            if (mat[i][j] != mat[xb][yb]) ok = false;
                        }
                    }
                if (ok) {
                    int m = N + abs(da) + abs(db);
                    if (m < mini) mini = m;
//                     cerr << da << ' ' << db << endl;
                }
            }
        cout << "Case #" << cas << ": " << mini*mini - N*N << endl;
    }
}
