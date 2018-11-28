#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
#define fi first
#define se second
#define rep(i, n) for (int i = 0, _##i = (n); i < _##i; ++i)
 
char board[4][4];
 
void ttt() {
    rep(i, 4) {
                char rowcomp = board[i][0];
        if (rowcomp == 'T') rowcomp = board[i][1];
                char colcomp = board[0][i];
        if (colcomp == 'T') colcomp = board[1][i];
                bool rowtest = 0; bool coltest = 0;
                for (int j = 0; j < 4; j++) {
                        if (rowcomp != board[i][j] && board[i][j] != 'T') rowtest = 1;
                        if (colcomp != board[j][i] && board[j][i] != 'T') coltest = 1;
                }
                if (rowtest == 0 && rowcomp != '.') {
                        cout << rowcomp << " won\n";
                        return;
                }
                if (coltest == 0 && colcomp != '.') {
                        cout << colcomp << " won\n";
                        return;
                }
        }
// check diagonals
    char d1 = board[0][0];
    bool t1 = 0;
    if (d1 == 'T') d1 = board[1][1];
    rep(i, 4) {
        if (board[i][i] != d1 && board[i][i] != 'T') t1 = 1;
    }
    if (t1 == 0 && d1 != '.') {
        cout << d1 << " won\n";
        return;
    }
    char d2 = board[3][0];
    bool t2 = 0;
    if (d2 == 'T') d2 = board[2][1];
    rep(i, 4) {
        if (board[3-i][i] != d2 && board[3-i][i] != 'T') t2 = 1;
    }
    if (t2 == 0 && d2 != '.') {
        cout << d2 << " won\n";
        return;
    }
        rep(i, 4) {
                rep(j, 4) {
                        if (board[i][j] == '.') {
                                cout << "Game has not completed\n";
                                return;
                        }
                }
        }
        cout << "Draw\n";
        return;
}
 
int main() {
freopen("ttt.out","w",stdout);
    int t;
        cin >> t;
        rep(i, t) {
                rep(j, 4) {
                        rep(k, 4) {
                                char temp;
                                cin >> temp;
                                board[j][k] = temp;
                        }
                }
                cout << "CASE #" << i+1 << ": ";
                ttt();
                rep(j, 4) {
                        rep(k, 4) {
                                board[j][k] = '.';
                        }
                }
        }
        return 0;
}