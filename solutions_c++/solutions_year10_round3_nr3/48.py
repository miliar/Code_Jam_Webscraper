#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long ullong;

int main() {
    ifstream input("A-small.in");
    ofstream output("A-small.out");
    ullong t, n, m;
    input>>t;
    for (ullong i = 0; i < t; i++) {
        input>>m>>n;
        char board[m + 1][n + 1];
        
        cout<<i + 1<<endl;
        for (int g = 0; g < m; g++) {
            for (int h = 0; h < n/4; h++) {
                char c;
                input>>c;
                switch (c) {
                    case '0' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case '1' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '1';
                        break;
                    case '2' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case '3' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '1';
                        break;
                    case '4' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case '5' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '1';
                        break;
                    case '6' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case '7' :
                        board[g][h * 4] = '0';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '1';
                        break;
                    case '8' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case '9' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '1';
                        break;
                    case 'A' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case 'B' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '0';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '1';
                        break;
                    case 'C' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case 'D' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '0';
                        board[g][h * 4 + 3] = '1';
                        break;
                    case 'E' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '0';
                        break;
                    case 'F' :
                        board[g][h * 4] = '1';
                        board[g][h * 4 + 1] = '1';
                        board[g][h * 4 + 2] = '1';
                        board[g][h * 4 + 3] = '1';
                        break;
                }
            }
        }
        
        for (int j = 0; j < n + 1; j ++) {
            board[m][j] = 'x';
        }
        for (int j = 0; j < m + 1; j ++) {
            board[j][n] = 'x';
        }
        vector<int> boardsize;
        vector<int> amountofboards;
        int maximumboard = 2;
        while (maximumboard > 1) {
            maximumboard = 0;
            int cordx=-1;
            int cordy=-1;
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < n; k++) {
                    if (board[j][k] == 'x') continue;
                    bool searching = true;
                    int tsize = 1;
                    while (searching) {
                        tsize++;
                        for (int ti = 0; ti < tsize - 1; ti++) {
                            if (board[j + tsize - 1][k + ti] == board[j + tsize - 2][k + ti] || board[j + tsize - 1][k + ti] == 'x') {
                               searching = false;
                               break;
                            }
                            if (board[j + ti][k + tsize - 1] == board[j + ti][k + tsize - 2] || board[j + ti][k + tsize - 1] == 'x') {
                               searching = false;
                               break;
                            }
                        }
                        if (board[j+tsize -1][k+tsize-1] == board[j+tsize-2][k+tsize-1] || board[j+tsize -1][k+tsize-1] == 'x')
                            searching = false;
                    }
                    if ((tsize - 1) > maximumboard) {
                        maximumboard = tsize - 1;
                        cordx=j;
                        cordy=k;
                    }
                }
            }
            for (int j = cordx; j < cordx + maximumboard; j++) {
                for (int k = cordy; k < cordy + maximumboard; k++) {
                    board[j][k] = 'x';
                }
            }if (cordx != -1) {
            if (boardsize.size() != 0) {
                if (boardsize[boardsize.size() - 1] == maximumboard) {
                    amountofboards[boardsize.size() - 1]++;
                } else {
                    boardsize.push_back(maximumboard);
                    amountofboards.push_back(1);
                }
            } else {
                boardsize.push_back(maximumboard);
                amountofboards.push_back(1);
            }}
        }
        for (int j = 0; j < m; j++) {
            for(int k = 0; k < n; k++) {
                if (board[j][k] != 'x') {
                    if (boardsize[boardsize.size() - 1] == 1) {
                        amountofboards[boardsize.size() - 1]++;
                    } else {
                        boardsize.push_back(1);
                        amountofboards.push_back(1);
                    }
                }
            }
        }
        output<<"Case #"<<i + 1<<": "<<boardsize.size()<<endl;
        for (int j = 0; j < boardsize.size(); j++) {
            output<<boardsize[j]<<' '<<amountofboards[j]<<endl;
            }
    }
}
