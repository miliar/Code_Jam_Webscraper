#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        cout << "Case #" << c << ": ";
        
        vector< string > board(4);
        int empty = 0, xwon = 0, owon = 0;
        
        for (int i = 0; i < 4; i++) {
            cin >> board[i];
            for (int j = 0; j < 4; j++) {
                if (board[i][j] == '.') {
                    empty++;
                }
            }
        }
        
        int xd1flag = 1, od1flag = 1, xd2flag = 1, od2flag = 1;
        for (int i = 0; i < 4; i++) {
            if (board[i][i] == 'O' || board[i][i] == '.') {
                xd1flag *= 0;
            }
            if (board[i][i] == 'X' || board[i][i] == '.') {
                od1flag *= 0;
            }
            if (board[i][3 - i] == 'O' || board[i][3 - i] == '.') {
                xd2flag *= 0;
            }
            if (board[i][3 - i] == 'X' || board[i][3 - i] == '.') {
                od2flag *= 0;
            }
        }
        if (xd1flag == 1 || xd2flag == 1) {
            xwon++;
            goto finish;
        }
        if (od1flag == 1 || od2flag == 1) {
            owon++;
            goto finish;
        }
        
        for (int i = 0; i < 4; i++) {
            int xrflag = 1, orflag = 1, xcflag = 1, ocflag = 1;
            for (int j = 0; j < 4; j++) {
                if (board[i][j] == 'O' || board[i][j] == '.') {
                    xrflag *= 0;
                }
                if (board[i][j] == 'X' || board[i][j] == '.') {
                    orflag *= 0;
                }
                if (board[j][i] == 'O' || board[j][i] == '.') {
                    xcflag *= 0;
                }
                if (board[j][i] == 'X' || board[j][i] == '.') {
                    ocflag *= 0;
                }
            }
            if (xrflag == 1 || xcflag == 1) {
                xwon++;
                goto finish;
            }
            if (orflag == 1 || ocflag == 1) {
                owon++;
                //~ cout << i << endl;
                goto finish;
            }
        }

finish:
        if (xwon > 0) {
            cout << "X won\n";
        } else if (owon > 0) {
            cout << "O won\n";
        } else if (empty > 0) {
            cout << "Game has not completed\n";
        } else {
            cout << "Draw\n";
        }
    }
    return 0;
}
