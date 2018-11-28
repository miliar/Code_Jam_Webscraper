#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>

#define FOR(i,a,n) for(int i=a;i<n;i++)
#define REP(i,n) FOR(i,0,n)
#define DBGV(_v) { REP(_i, _v.sz) { cout << _v[_i] << "\t";} cout << endl;}
#define sz size()


using namespace std;

int search(vector<string> board, char move) {
    //REP(i, 4) {
        //cout << board[i] << endl;
    //}
    //cout << endl;
    REP(i, 4) {
        bool valid = true;
        REP(j, 4) {
            if (!(board[i][j] == move || board[i][j] == 'T')) {
                valid = false;
                break;
            }
        }
        if (valid == true) return move;
    }

    REP(i, 4) {
        bool valid = true;
        REP(j, 4) {
            if (!(board[j][i] == move || board[j][i] == 'T')) {
                valid = false;
                break;
            }
        }
        if (valid == true) return move;
    }

    REP(i, 1) {
        bool valid = true;
        REP(j, 4) {
            if (!(board[j][j] == move || board[j][j] == 'T')) {
                valid = false;
                break;
            }
        }
        if (valid == true) return move;
    }

    REP(i, 1) {
        bool valid = true;
        REP(j, 4) {
            if (!(board[j][3-j] == move || board[j][3-j] == 'T')) {
                valid = false;
                break;
            }
        }
        if (valid == true) return move;
    }

    REP(i, 4) {
        REP(j, 4) {
            if (board[i][j] == '.') {
                return -1;
            }
        }
    }

    return 0;

}

int main() {
    int kase = 0;
    cin >> kase;
    for(int kase_cnt = 1; kase_cnt <= kase; kase_cnt++) {
        vector<string> board;
        string s;
        REP(i, 4) {
            cin >> s;
            board.push_back(s);
        }
        int res1 = search(board, 'X');
        int res2 = search(board, 'O');
        cout << "Case #" << kase_cnt << ": ";
        if (res1 == 'X') {
            cout << "X won";
        }
        else if (res2 == 'O') {
            cout << "O won";
        }
        else if (res1 == -1 && res2 == -1) {
            cout << "Game has not completed";
        }
        else if (res1 == 0 && res2 == 0) {
            cout << "Draw";
        }
        cout << endl;
    }
}
