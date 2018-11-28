// -*- encoding: utf-8-unix -*-
// USED ALGORITHM: 
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <complex>

using namespace std;
typedef complex<double> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<double> vd;
typedef vector<string> vs;
#define ALL(c) (c).begin(), (c).end()
//#define FOR(c, it) for (typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define REP(i, n) for (int i = 0; i < n; ++i)

bool check(const vector<vector<char> >& board, int N, int K, char c)
{
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            // right
            if (j + K <= N) {
                bool ok = true;
                for (int k = 0; k < K; ++k) {
                    if (board[i][j+k] != c) { ok = false; break; }
                }
                if (ok) { return true; }
            }
            // down
            if (i + K <= N) {
                bool ok = true;
                for (int k = 0; k < K; ++k) {
                    if (board[i+k][j] != c) { ok = false; break; }
                }
                if (ok) { return true; }
            }
            // rightdown
            if (i + K <= N && j + K <= N) {
                bool ok = true;
                for (int k = 0; k < K; ++k) {
                    if (board[i+k][j+k] != c) { ok = false; break; }
                }
                if (ok) { return true; }
            }
            // leftdown
            if (i + K <= N && j - K >= -1) {
                bool ok = true;
                for (int k = 0; k < K; ++k) {
                    if (board[i+k][j-k] != c) { ok = false; break; }
                }
                if (ok) { return true; }
            }
        }
    }
    return false;
}

int main(void)
{
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, K; cin >> N >> K;
        vector<vector<char> > board(N, vector<char>(N));
        REP (i, N) REP (j, N) {
            cin >> board[j][N-i-1];
        }

        REP (j, N) {
            for (int i = N - 1; i >= 0; --i) {
                if (board[i][j] != '.') { continue; }
                for (int k = i - 1; k >= 0; --k) {
                    if (board[k][j] == '.') { continue; }
                    swap(board[i][j], board[k][j]);
                    break;
                }
            }
        }

#if 0
        REP (i, N) {
            REP (j, N) {
                cout << board[i][j];
            }
            cout << endl;
        }
        cout << endl;
#endif

        bool blue = check(board, N, K, 'B');
        bool red = check(board, N, K, 'R');

        cout << "Case #" << t << ": ";
        if (blue && red) { cout << "Both" << endl; }
        else if (blue) { cout << "Blue" << endl; }
        else if (red) { cout << "Red" << endl; }
        else { cout << "Neither" << endl; }
    }

    return 0;
}

