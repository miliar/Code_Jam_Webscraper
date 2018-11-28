#include <iostream>

using namespace std;

const int MAX_N = 50;

int main() {
    int TT;
    int KK;
    int NN;
    char board1[MAX_N+1][MAX_N+1];
    char board2[MAX_N+1][MAX_N+1];
    int counter1;
    int counter2;
    bool rwins = false;
    bool bwins = false;
    int rcount = 0;
    int bcount = 0;
    cin >> TT;
    for (int z = 1; z <= TT; z++) {
        cin >> NN >> KK;
        for (int i = 0; i < NN; i++) {
            cin >> board1[i];
        }
        for (int i = NN - 1; i >= 0; i--) {
            counter1 = NN-1;
            counter2 = 0;
            for (int j = NN - 1; j >= 0; j--) {
                if (board1[i][j] == '.') {
                    board2[counter2][NN-1-i] = board1[i][j];
                    counter2++;
                } else {
                    board2[counter1][NN-1-i] = board1[i][j];
                    counter1--;
                }
            }
            board2[i][NN] = '\0';
        }
//         for (int i = 0; i < NN; i++) {
//             cerr << board2[i] << endl;
//         }
        rwins = false;
        bwins = false;
        /* check horizontal */
        for (int i = 0; i < NN; i++) {
            rcount = 0;
            bcount = 0;
            for (int j = 0; j < NN; j++) {
                if (board2[i][j] == '.') {
                    rcount = 0;
                    bcount = 0;
                }
                if (board2[i][j] == 'R') {
                    rcount++;
                    bcount = 0;
                }
                if (board2[i][j] == 'B') {
                    bcount++;
                    rcount = 0;
                }
                if (bcount >= KK) {
                    bwins = true;
                }
                if (rcount >= KK) {
                    rwins = true;
                }
            }
        }
        /* check verical */
        for (int j = 0; j < NN; j++) {
            rcount = 0;
            bcount = 0;
            for (int i = 0; i < NN; i++) {
                if (board2[i][j] == '.') {
                    rcount = 0;
                    bcount = 0;
                }
                if (board2[i][j] == 'R') {
                    rcount++;
                    bcount = 0;
                }
                if (board2[i][j] == 'B') {
                    bcount++;
                    rcount = 0;
                }
                if (bcount >= KK) {
                    bwins = true;
                }
                if (rcount >= KK) {
                    rwins = true;
                }
            }
        }
        for (int i = 0; i < NN; i++) {
            /* check diagonal SW-NE from NW */
            rcount = 0;
            bcount = 0;
            for (int j = 0; j <= i; j++) {
                if (board2[i-j][j] == '.') {
                    rcount = 0;
                    bcount = 0;
                }
                if (board2[i-j][j] == 'R') {
                    rcount++;
                    bcount = 0;
                }
                if (board2[i-j][j] == 'B') {
                    bcount++;
                    rcount = 0;
                }
                if (bcount >= KK) {
                    bwins = true;
                }
                if (rcount >= KK) {
                    rwins = true;
                }
            }            
            /* check diagonal SW-NE from SE */
            rcount = 0;
            bcount = 0;
            for (int j = 0; j <= i; j++) {
                if (board2[NN-1-(i-j)][NN-1-(j)] == '.') {
                    rcount = 0;
                    bcount = 0;
                }
                if (board2[NN-1-(i-j)][NN-1-(j)] == 'R') {
                    rcount++;
                    bcount = 0;
                }
                if (board2[NN-1-(i-j)][NN-1-(j)] == 'B') {
                    bcount++;
                    rcount = 0;
                }
                if (bcount >= KK) {
                    bwins = true;
                }
                if (rcount >= KK) {
                    rwins = true;
                }
            }            
            /* check diagonal NW-SE from NE */
            rcount = 0;
            bcount = 0;
            for (int j = 0; j <= i; j++) {
                if (board2[i-j][NN-1-(j)] == '.') {
                    rcount = 0;
                    bcount = 0;
                }
                if (board2[i-j][NN-1-(j)] == 'R') {
                    rcount++;
                    bcount = 0;
                }
                if (board2[i-j][NN-1-(j)] == 'B') {
                    bcount++;
                    rcount = 0;
                }
                if (bcount >= KK) {
                    bwins = true;
                }
                if (rcount >= KK) {
                    rwins = true;
                }
            }            
            /* check diagonal NW-SE from SW */
            rcount = 0;
            bcount = 0;
            for (int j = 0; j <= i; j++) {
                if (board2[NN-1-(i-j)][j] == '.') {
                    rcount = 0;
                    bcount = 0;
                }
                if (board2[NN-1-(i-j)][j] == 'R') {
                    rcount++;
                    bcount = 0;
                }
                if (board2[NN-1-(i-j)][j] == 'B') {
                    bcount++;
                    rcount = 0;
                }
                if (bcount >= KK) {
                    bwins = true;
                }
                if (rcount >= KK) {
                    rwins = true;
                }
            }
        }
        
        if ((rwins) and (bwins)) {
            cout << "Case #" << z << ": " << "Both" << endl;
        }
        
        if ((rwins) and (not bwins)) {
            cout << "Case #" << z << ": " << "Red" << endl;
        }
        
        if ((bwins) and (not rwins)) {
            cout << "Case #" << z << ": " << "Blue" << endl;
        }
        
        if ((not rwins) and (not bwins)) {
            cout << "Case #" << z << ": " << "Neither" << endl;
        }
        
            
    }
    
}