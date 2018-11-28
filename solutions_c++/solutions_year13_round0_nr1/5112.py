#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define fi first
#define se second
char board[50][50];

bool check(char ch) {
    bool flag1=true,flag2=true;
    for (int i = 0; i < 4; i++) {
         flag1=true,flag2=true;
        for (int j = 0; j < 4; j++) {
            if (board[j][i] != ch && board[j][i] != 'T') flag1=false;
        }
        for (int j = 0; j < 4; j++) {
            if (board[i][j] != ch && board[i][j] != 'T') flag2=false;
        }
        if (flag1 || flag2) return true;
    }
    bool flag = true;
    for (int i = 0; i < 4; i++) {
        if (board[i][i] != ch && board[i][i] != 'T') flag = false;
    }
    if (flag) return true;
    for (int i = 0; i < 4; i++) {
        if (board[i][3 - i] != ch && board[i][3 - i] != 'T') return false;
    }
    return true;    
}

int main() {
      freopen("A.in", "r", stdin);
      freopen("A.txt", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        for (int i = 0; i < 4; i++) cin >> board[i];
        printf("Case #%d: ", Case++);
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (board[i][j] != '.') cnt+=1;
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
    return 0;
}

