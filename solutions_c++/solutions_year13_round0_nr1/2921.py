#include <vector>
#include <list>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <assert.h>

using namespace std;

struct Node {
    
};

char board[4][4];

int main() {
    int T;
    cin >> T;
    for (int index = 1; index <= T; ++index) {
        for (int i = 0; i < 4; ++i) {
            cin >> board[i];
        }
        bool oWin = false, xWin = false;
        int dotCount = 0, oCount = 0, xCount = 0;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (board[i][j] == '.') {
                    ++dotCount;
                }
            }
        }
        for (int i = 0; i < 4; ++i) {
            oCount = 0, xCount = 0;
            for (int j = 0; j < 4; ++j) {
                switch (board[i][j]) {
                    case 'X':
                        ++xCount;
                        break;
                    case 'O':
                        ++oCount;
                        break;
                    case 'T':
                        ++xCount;
                        ++oCount;
                        break;
                    default:
                        break;
                }
            }
            if (oCount == 4)
                oWin = true;
            if (xCount == 4)
                xWin = true;
        }
        for (int j = 0; j < 4; ++j) {
            oCount = 0, xCount = 0;
            for (int i = 0; i < 4; ++i) {
                switch (board[i][j]) {
                    case 'X':
                        ++xCount;
                        break;
                    case 'O':
                        ++oCount;
                        break;
                    case 'T':
                        ++xCount;
                        ++oCount;
                        break;
                    default:
                        break;
                }
            }
            if (oCount == 4)
                oWin = true;
            if (xCount == 4)
                xWin = true;
        }
        oCount = 0, xCount = 0;
        for (int i = 0; i < 4; ++i) {
            switch (board[i][i]) {
                case 'X':
                    ++xCount;
                    break;
                case 'O':
                    ++oCount;
                    break;
                case 'T':
                    ++xCount;
                    ++oCount;
                    break;
                default:
                break;
            }
        }
        if (oCount == 4)
            oWin = true;
        if (xCount == 4)
            xWin = true;
        oCount = 0, xCount = 0;
        for (int i = 0; i < 4; ++i) {
            switch (board[i][3 - i]) {
                case 'X':
                    ++xCount;
                    break;
                case 'O':
                    ++oCount;
                    break;
                case 'T':
                    ++xCount;
                    ++oCount;
                    break;
                default:
                    break;
            }
        }
        if (oCount == 4)
            oWin = true;
        if (xCount == 4)
            xWin = true;
        if (xWin)
            cout<<"Case #"<<index<<": X won"<<endl;
        else if (oWin)
            cout<<"Case #"<<index<<": O won"<<endl;
        else if (dotCount == 0)
            cout<<"Case #"<<index<<": Draw"<<endl;
        else
            cout<<"Case #"<<index<<": Game has not completed"<<endl;
        
    }
    return 0;
}