#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "vector"
#include "queue"
#include "stack"
#include "cmath"
#include "string"
#include "cctype"
#include "map"
#include "iomanip"
#include "set"
#include "utility"
using namespace std;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
const int inf = 1 << 29;
const double dinf = 1e30;
const ll linf = 1LL << 55;


const int N = 4;
char board[N << 1][N << 1];

bool checkRow(int row, char ch) {
    for (int j = 0; j < N; j++) {
        if (board[row][j] != ch && board[row][j] != 'T') return false;
    }
    return true;
}

bool checkCol(int col, char ch) {
    for (int i = 0; i < N; i++) {
        if (board[i][col] != ch && board[i][col] != 'T') return false;
    }
    return true;
}

bool checkDia(char ch) {
    bool flag = true;
    for (int i = 0; i < N; i++) {
        if (board[i][i] != ch && board[i][i] != 'T') flag = false;
    }
    if (flag) return true;
    for (int i = 0; i < N; i++) {
        if (board[i][N - 1 - i] != ch && board[i][N - 1 - i] != 'T') return false;
    }
    return true;
}

bool check(char ch) {
    for (int i = 0; i < N; i++) {
        if (checkCol(i, ch) || checkRow(i, ch)) return true;
    }
    if (checkDia(ch)) return true;
    return false;
}

void solve() {
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cnt += (board[i][j] != '.');
        }
    }
    if (check('O')) {
        puts("O won");
    } else if (check('X')) {
        puts("X won");
    } else if (cnt == 16) {
        puts("Draw");
    } else {
        puts("Game has not completed");
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        for (int i = 0; i < N; i++) cin >> board[i];
        printf("Case #%d: ", Case++);
        solve();
    }
    return 0;
}
