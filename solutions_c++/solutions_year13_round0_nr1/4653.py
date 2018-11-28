#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <climits>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int t;
char board[8][8];

bool O(char c) {
    return c == 'O' || c == 'T';
}

bool X(char c) {
    return c == 'X' || c == 'T';
}

void solve() {
    for (int i = 0; i < 4; ++i)
        scanf("%s", board[i]);
    bool win_o = false, win_x = false;
    for (int i = 0; i < 4; ++i)
        if (O(board[i][0]) && O(board[i][1]) && O(board[i][2]) && O(board[i][3]))
            win_o = true;
    for (int i = 0; i < 4; ++i)
        if (X(board[i][0]) && X(board[i][1]) && X(board[i][2]) && X(board[i][3]))
            win_x = true;
    for (int i = 0; i < 4; ++i)
        if (O(board[0][i]) && O(board[1][i]) && O(board[2][i]) && O(board[3][i]))
            win_o = true;
    for (int i = 0; i < 4; ++i)
        if (X(board[0][i]) && X(board[1][i]) && X(board[2][i]) && X(board[3][i]))
            win_x = true;
    if (O(board[0][0]) && O(board[1][1]) && O(board[2][2]) && O(board[3][3]))
        win_o = true;
    if (X(board[0][0]) && X(board[1][1]) && X(board[2][2]) && X(board[3][3]))
        win_x = true;
    if (O(board[3 - 0][0]) && O(board[3 - 1][1]) && O(board[3 - 2][2]) && O(board[3 - 3][3]))
        win_o = true;
    if (X(board[3 - 0][0]) && X(board[3 - 1][1]) && X(board[3 - 2][2]) && X(board[3 - 3][3]))
        win_x = true;
    if (win_x && win_o) {
        puts("Fuck...");
        while (1);
    }
    if (win_x)
        printf("Case #%d: X won\n", ++t);
    else if (win_o)
        printf("Case #%d: O won\n", ++t);
    else {
        bool e = false;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                if (board[i][j] == '.')
                    e = true;
        if (e)
            printf("Case #%d: Game has not completed\n", ++t);
        else
            printf("Case #%d: Draw\n", ++t);
    }
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        solve();
    }
    return 0;
}
