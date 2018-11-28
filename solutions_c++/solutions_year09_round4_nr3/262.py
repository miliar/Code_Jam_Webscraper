#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

int N, K, p[100][30];
bool pred[100][100];

int lU[100], rU[100];
bool mark[100];

bool FindMatch(int l) {
    for (int r = 0; r < N; ++r)
        if (pred[l][r] && !mark[r]) {
            mark[r] = true;
            if (rU[r] == -1 || FindMatch(rU[r])) {
                lU[l] = r;
                rU[r] = l;
                return true;
            }
        }
    return false;
}

bool Compare(int* a, int* b) {
    for (int i = 0; i < K; ++i, ++a, ++b)
        if (*a >= *b)
            return false;
    return true;
}

int solve() {
    cin >> N >> K;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < K; ++j)
            cin >> p[i][j];
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            pred[i][j] = Compare(p[i], p[j]);
    int ans = N;
    fill(lU, lU + N, -1);
    fill(rU, rU + N, -1);
    for (int i = 0; i < N; ++i) {
        fill(mark, mark + N, false);
        if (FindMatch(i)) --ans;
    }
    return ans;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        freopen((string(argv[1]) + ".in").c_str(), "r", stdin);
        freopen((string(argv[1]) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
