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

typedef long long ll;

int R, C, board[600][600], bb[600][600], sumBb[600][600];
char buf[1 << 16];
vector<int> ans;
bool qual[600][600];

void markUsed(int x, int y, int s) {
    for (int i = max(0, x - s + 1); i < x + s; ++i)
        for (int j = max(0, y - s + 1); j < y + s; ++j)
            qual[i][j] = false;
    for (int i = x; i < x + s; ++i)
        for (int j = y; j < y + s; ++j)
            board[i][j] = 2;
}

void cutOff(int s) {
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (qual[i][j]) {
                ans.push_back(s);
                markUsed(i, j, s);
            }
}

int min(int a, int b, int c) { return min(min(a, b), c); }

int square[600][600], leftExpand[600][600], upExpand[600][600];
int ss[600][600];

bool cuts() {
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) {
            bb[i][j] = i + 1 < R && j + 1 < C && board[i][j] < 2
                    && board[i][j] + board[i + 1][j] == 1
                    && board[i][j] + board[i][j + 1] == 1
                    && board[i][j] == board[i + 1][j + 1];
        }
    int L = 0;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) {
            square[i][j] = leftExpand[i][j] = upExpand[i][j] = 0;
            if (bb[i][j]) {
                leftExpand[i][j] = (j > 0 ? leftExpand[i][j - 1] : 0) + 1;
                upExpand[i][j] = (i > 0 ? upExpand[i - 1][j] : 0) + 1;
                square[i][j] = min((i > 0 && j > 0 ? square[i - 1][j - 1] : 0) + 1, leftExpand[i][j], upExpand[i][j]);
                if (square[i][j] > L)
                    L = square[i][j];
            }
        }
    if (L == 0)
        return false;
    for (int i = 0; i <= R; ++i)
        for (int j = 0; j <= C; ++j)
            ss[i][j] = 0;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            ss[i + 1][j + 1] = bb[i][j] + ss[i + 1][j] + ss[i][j + 1] - ss[i][j];
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            qual[i][j] = i + L <= R && j + L <= C && ss[i + L][j + L] + ss[i][j] - ss[i + L][j] - ss[i][j + L] == L * L;
    cutOff(L + 1);
    return true;
}

void solve() {
    cin >> R >> C;
    for (int i = 0; i < R; ++i) {
        cin >> buf;
        for (int j = 0; j < C; ++j) {
            int c = buf[j / 4];
            if (c < 'A')
                c -= '0';
            else
                c -= 'A' - 10;
            board[i][j] = c >> 3 - j % 4 & 1;
        }
    }
    ans.clear();
    while (cuts());
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (board[i][j] < 2)
                ans.push_back(1);
    vector<int> t = ans;
    sort(t.begin(), t.end());
    t.erase(unique(t.begin(), t.end()), t.end());
    printf("%d\n", t.size());
    for (vector<int>::reverse_iterator it = t.rbegin(); it != t.rend(); ++it) {
        int c = 0;
        for (int i = 0; i < ans.size(); ++i)
            if (ans[i] == *it)
                ++c;
        printf("%d %d\n", *it, c);
    }
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        else if (strcmp(file_name + len - 1, ".") == 0)
            file_name[len - 1] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc) {
        printf("Case #%d: ", cc + 1);
        solve();
    }
    return 0;
}
