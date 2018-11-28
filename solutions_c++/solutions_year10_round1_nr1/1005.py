#include <iostream>
#include <vector>

using namespace std;

struct sth {
    int row;
    int col;
    int dia1;
    int dia2;
};

int main()
{
    int numCase;
    cin >> numCase;

    // input
    for (int m = 0; m < numCase; m++) {
        int size, win;
        cin >> size >> win;
        vector<char> *map = new vector<char>[size];
        for (int j = 0; j < size; j++) {
            char tmp[size+1];
            cin >> tmp;
            for (int k = 0; k < size; k++) {
                if (tmp[size-1-k] != '.') {
                    map[size-1-j].push_back(tmp[size-1-k]);
                }
            }
            for (int k = map[size-1-j].size(); k < size; k++) {
                map[size-1-j].push_back('.');
            }
        }
/*
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                cout << map[j][size-1-i];
            }
            cout << "\n";
        }
*/
        struct sth **winArray = new sth*[size];
        for (int i = 0; i < size; i++) {
            winArray[i] = new sth[size];
        }

        bool blueChecked = false;
        bool realBlueWin = false, realRedWin = false;
        char checkChar = 'B';

        checkWin:
        // check blue first
        bool blueWin = false;
        if (map[0][0] == checkChar) {
            winArray[0][0].row = 1;
            winArray[0][0].col = 1;
            winArray[0][0].dia1 = 1;
            winArray[0][0].dia2 = 1;
        } else {
            winArray[0][0].row = 0;
            winArray[0][0].col = 0;
            winArray[0][0].dia1 = 0;
            winArray[0][0].dia2 = 0;
        }

        // bottom row
        for (int i = 1; i < size; i++) {
            if (map[i][0] == checkChar) {
                winArray[i][0].row = winArray[i-1][0].row+1;
                winArray[i][0].col = 1;
                winArray[i][0].dia1 = 1;
                winArray[i][0].dia2 = 1;
                if (winArray[i][0].row >= win || winArray[i][0].col >= win || winArray[i][0].dia1 >= win || winArray[i][0].dia2 >= win) {
                    blueWin = true;
                    break;
                }
            } else {
                winArray[i][0].row = 0;
                winArray[i][0].col = 0;
                winArray[i][0].dia1 = 0;
                winArray[i][0].dia2 = 0;
            }
        }

        // first col
        for (int i = 1; i < size; i++) {
            if (map[0][i] == checkChar) {
                winArray[0][i].row = 1;
                winArray[0][i].col = winArray[0][i-1].col+1;
                //cout << winArray[0][i].col<<endl;
                winArray[0][i].dia1 = 1;
                winArray[0][i].dia2 = 1;
                if (winArray[0][i].row >= win || winArray[0][i].col >= win || winArray[0][i].dia1 >= win || winArray[0][i].dia2 >= win) {
                    blueWin = true;
                    break;
                }
            } else {
                winArray[0][i].row = 0;
                winArray[0][i].col = 0;
                winArray[0][i].dia1 = 0;
                winArray[0][i].dia2 = 0;
            }
        }

        if (!blueWin){
            // Others
            for (int j = 1; j < size; j++) {
                for (int i = 1; i < size; i++) {
                    if (map[i][j] == checkChar) {
                        winArray[i][j].row = winArray[i-1][j].row+1;
                        winArray[i][j].col = winArray[i][j-1].col+1;
                        winArray[i][j].dia1 = winArray[i-1][j-1].dia1+1;
                        winArray[i][j].dia2 = (i==size-1) ? 1 : (winArray[i+1][j-1].dia2+1);
                        if (winArray[i][j].row >= win || winArray[i][j].col >= win || winArray[i][j].dia1 >= win || winArray[i][j].dia2 >= win) {
                            blueWin = true;
                            break;
                        }
                    } else {
                        winArray[i][j].row = 0;
                        winArray[i][j].col = 0;
                        winArray[i][j].dia1 = 0;
                        winArray[i][j].dia2 = 0;
                    }
                }
                if (blueWin) {
                    break;
                }
            }
        }

        // first col again
        for (int i = 1; i < size; i++) {
            if (map[0][i] == checkChar) {
                winArray[0][i].dia2 = winArray[1][i-1].dia2+1;
                //cout << winArray[0][i].dia2 << endl;
                if (winArray[0][i].row >= win || winArray[0][i].col >= win || winArray[0][i].dia1 >= win || winArray[0][i].dia2 >= win) {
                    blueWin = true;
                    break;
                }
            } else {
                winArray[0][i].row = 0;
                winArray[0][i].col = 0;
                winArray[0][i].dia1 = 0;
                winArray[0][i].dia2 = 0;
            }
        }

        if (!blueChecked) {
            blueChecked = true;
            checkChar = 'R';
            realBlueWin = blueWin;
            goto checkWin;
        } else {
            realRedWin = blueWin;
        }

        if (realBlueWin && realRedWin) {
            cout << "Case #" << m+1 << ": Both\n";
        } else if (realBlueWin && !realRedWin) {
            cout << "Case #" << m+1 << ": Blue\n";
        } else if (realRedWin && !realBlueWin) {
            cout << "Case #" << m+1 << ": Red\n";
        } else {
            cout << "Case #" << m+1 << ": Neither\n";
        }
    }

    return 0;
}
