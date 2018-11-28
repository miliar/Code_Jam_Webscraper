#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <stack>
#include <queue>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int n = 1; n <= T; n++) {
        char board[4][4] = { {'.', '.', '.', '.'},
                            {'.', '.', '.', '.'},
                            {'.', '.', '.', '.'},
                            {'.', '.', '.', '.'} };
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> board[i][j];
            }
        }
        bool containsdots = false;
        char rowwins[4]={0,0,0,0};
        char colwins[4]={0,0,0,0};
        for (int i = 0; i < 4; i++) {
            // check if any rows/cols win
            char curr = board[i][0];
            char curc = board[0][i];
            bool rdonet = false;
            bool cdonet = false;
            bool rwins = true;
            bool cwins = true;
            if (curr == '.') {
                containsdots = true;
                rwins = false;
            }
            if (curc == '.') {
                containsdots = true;
                cwins = false;
            }
            for (int j = 1; j < 4; j++) {
                if (rwins) {
                    if (curr == 'T') {
                        rdonet = true;
                        if (board[i][j] == 'T') {
                            rwins = false;
                        } else {
                            curr = board[i][j];
                        }
                    } else if (board[i][j] == '.') {
                        containsdots = true;
                        rwins = false;
                    } else if (board[i][j] == 'T') {
                        if (!rdonet) {
                            rdonet = true;
                        } else {
                            rwins = false;
                        }
                    } else if (board[i][j] != curr) {
                        rwins = false;
                    }
                }
                if (cwins) {
                    if (curc == 'T') {
                        cdonet = true;
                        if (board[j][i] == 'T') {
                            cwins = false;
                        } else {
                            curc = board[j][i];
                        }
                    } else if (board[j][i] == '.') {
                        containsdots = true;
                        cwins = false;
                    } else if (board[j][i] == 'T') {
                        if (!cdonet) {
                            cdonet = true;
                        } else {
                            cwins = false;
                        }
                    } else if (board[j][i] != curc) {
                        cwins = false;
                    }
                }
                if (!rwins && !cwins) {
                    break;
                }
            }
            rowwins[i] = rwins ? curr : 0;
            colwins[i] = cwins ? curc : 0;
        }
        char diags[2] = {0, 0};
        bool fi = true;
        bool si = true;
        bool ft = false;
        bool st = false;
        char finitial = board[0][0];
        char sinitial = board[0][3];
        for (int i = 1; i < 4; i++) {
            if (fi) {
                if (finitial == '.') {
                    containsdots = true;
                    fi = false;
                } else if (finitial == 'T') {
                    ft = true;
                    if (board[i][i] == 'T') {
                        fi = false;
                    } else if (board[i][i] == '.') {
                        containsdots = true;
                        fi = false;
                    } else {
                        finitial = board[i][i];
                    }
                } else {
                    if (board[i][i] == 'T') {
                        if (!ft) {
                            ft = true;
                        } else {
                            fi = false;
                        }
                    } else if (board[i][i] != finitial) {
                        fi = false;
                    }
                }
            }
            if (si) {
                if (sinitial == '.') {
                    containsdots = true;
                    si = false;
                } else if (sinitial == 'T') {
                    st = true;
                    if (board[i][3 - i] == 'T') {
                        si = false;
                    } else if (board[i][3 - i] == '.') {
                        containsdots = true;
                        si = false;
                    } else {
                        sinitial = board[i][3 - i];
                    }
                } else {
                    if (board[i][3 - i] == 'T') {
                        if (!st) {
                            st = true;
                        } else {
                            si = false;
                        }
                    } else if (board[i][3 - i] != sinitial) {
                        si = false;
                    }
                }
            }
            if (!fi && !si) {
                break;
            }
        }
        char winner = 0;
        diags[0] = fi ? finitial : 0;
        diags[1] = si ? sinitial : 0;
        for (int i = 0; i < 4; i++) {
            if (rowwins[i] != 0) {
                winner = rowwins[i];
                break;
            }
            if (colwins[i] != 0) {
                winner = colwins[i];
                break;
            }
        }
        if (winner == 0) {
            if (diags[0] != 0) {
                winner = diags[0];
            } else if (diags[1] != 0) {
                winner = diags[1];
            }
        }
        string output;
        if (winner == 0 && !containsdots) {
            output = "Draw";
        } else if (winner == 0 && containsdots) {
            output = "Game has not completed";
        } else {
            output = "";
            output += winner;
            output += " won";
        }
        cout << "Case #" << n << ": " << output << "\n";
    }
    return 0;
}
