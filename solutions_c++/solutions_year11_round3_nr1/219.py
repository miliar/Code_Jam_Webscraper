#include <vector>
#include <list>
#include <map>
#include <queue>
#include <iostream>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>
using namespace std;

inline int get(void) {
    int a;
    scanf("%d", &a);
    return a;
}

void solve() {
    int r = get();
    int c = get();
    char board[50+5][50+5];
    scanf("\n");
    for (int i = 0; i < r; i++) {
        fgets(board[i], 50+5, stdin);
    }
    for (int i = 0; i < r - 1; i++) {
        for (int j = 0; j < c - 1; j++) {
            if (board[i][j] == '#') {
                if (board[i+1][j] == '#' && board[i+1][j+1] == '#' &&
                        board[i][j+1] == '#') {
                    board[i][j] = '/';
                    board[i+1][j] = '\\';
                    board[i+1][j+1] = '/';
                    board[i][j+1] = '\\';
                }
            }
        }
    }
    for (int i = 0; i < r ; i++) {
        for (int j = 0; j < c ; j++) {
            if (board[i][j] == '#') {
                printf("Impossible\n");
                return;
            }
        }
    }
    for (int i = 0; i < r ; i++) {
        for (int j = 0; j < c ; j++) {
            printf("%c",board[i][j]);
        }
        printf("\n");
    }
}

int main(void) {
    int tests = get();
    for (int t = 1; t <= tests; t++) {
        printf("Case #%d:\n", t);
        solve();
    }
    return 0;
}
