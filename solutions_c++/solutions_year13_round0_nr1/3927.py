#include <iostream>
#include <string>
#include <memory.h>
using namespace std;

const int N = 4;

string field[4];

string solve() {
#define CHECK() \
    if (cnt['X'] + cnt['T'] == N) \
        return "X won"; \
    if (cnt['O'] + cnt['T'] == N) \
        return "O won";

    for (int i = 0; i < N; ++i) {
        int cnt[256];
        memset(cnt, 0, sizeof(cnt));
        for (int j = 0; j < N; ++j)
            ++cnt[field[i][j]];
        CHECK();
    }

    for (int j = 0; j < N; ++j) {
        int cnt[256];
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < N; ++i)
            ++cnt[field[i][j]];
        CHECK();
    }

    int cnt[256];
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < N; ++i)
        ++cnt[field[i][i]];
    CHECK();

    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < N; ++i)
        ++cnt[field[i][N - 1 - i]];
    CHECK();

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            if (field[i][j] == '.')
                return "Game has not completed";
    return "Draw";
}

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        for (int i = 0; i < 4; ++i)
            cin >> field[i];
        cout << "Case #" << tt << ": " << solve() << '\n';
    }

    return 0;
}

