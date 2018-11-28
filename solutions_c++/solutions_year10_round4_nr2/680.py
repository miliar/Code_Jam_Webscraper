#include <iostream>
#include <set>
#include <string>

using namespace std;

const int MAX = 10;
int N, M[1 << MAX], P[1 << (MAX + 1)], S[1 << (MAX + 1)][MAX + 1];

void ReadData() {
    cin >> N;
    for (int i = 0, cnt = (1 << N); i != cnt; ++i)
        cin >> M[i];
    for (int i = 0, cnt = (1 << N) - 1; i != cnt; ++i)
        cin >> P[i];
}

int Work() {
    for (int i = 0, cnt = (1 << N); i != cnt; ++i) {
        for (int j = 0; j != N + 1; ++j) {
            S[i][j] = (j <= M[i] ? 0 : -1);
        }
    }
    for (int k = 0, s = (1 << N), t = (1 << N), u = 0; k < N; ++k, t /= 2, s += t) {
        for (int j = 0; j < t / 2; ++j, ++u) {
            int c = s + j;
            int a = s - t + 2 * j;
            int b = s - t + 2 * j + 1;
            for (int r = 0; r <= N; ++r) {
                S[c][r] = (S[a][r] != -1 && S[b][r] != -1 ) ? ( S[a][r] + S[b][r] + P[u] ) : -1;
                if (r != N && S[a][r + 1] != -1 && S[b][r + 1] != -1 && (S[c][r] == -1 || S[a][r + 1] + S[b][r + 1] < S[c][r]) )
                    S[c][r] = S[a][r + 1] + S[b][r + 1];
            }
        }
    }
    int res = -1;
    for (int i = 0; i != N + 1; ++i) {
        int v = S[(1 << (N + 1)) - 2][i];
        if (v != -1 && (res == -1 || v < res))
            res = v;
    }
    return res;
}

void Output(int t, int res) {
    cout << "Case #" << t << ": " << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        ReadData();
        Output(i, Work());
    }
    return 0;
}

