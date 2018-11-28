#include <cstdio>
#include <string>

using namespace std;

const int max_n = 50 + 10;

int t, n, m;
char board[max_n][max_n];

void solve();
string get_result();
void shift_down();
bool can_win(char);

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        char buf[64];
        scanf("%s", buf);
        for (int j = 0; j < n; ++j)
            board[j][n - i - 1] = buf[j];
    }
    printf("Case #%d: %s\n", ++t, get_result().c_str());
}

string get_result() {
    shift_down();
    /*for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j)
            putchar(board[i][j]);
        putchar('\n');
    }*/
    bool f1 = can_win('R'), f2 = can_win('B');
    if (f1 && f2)
        return "Both";
    if (f1)
        return "Red";
    if (f2)
        return "Blue";
    return "Neither";
}

void shift_down() {
    for (int j = 0; j < n; ++j) {
        int k = n - 1;
        for (int i = n - 1; i >= 0; --i)
            if (board[i][j] != '.')
                board[k--][j] = board[i][j];
        for (; k >= 0; --k)
            board[k][j] = '.';
    }
}

bool can_win(char c) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (board[i][j] != c)
                continue;
            int x, y;
            for (x = i; x < n && board[x][j] == c; ++x);
            if (x - i >= m)
                return true;
            for (y = j; y < n && board[i][y] == c; ++y);
            if (y - j >= m)
                return true;
            for (x = 1; i + x < n && j + x < n && board[i + x][j + x] == c; ++x);
            if (x >= m)
                return true;
            for (y = 1; i + y < n && j - y >= 0 && board[i + y][j - y] == c; ++y);
            if (y >= m)
                return true;
        }
    }
    return false;
}
