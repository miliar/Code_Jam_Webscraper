#include <iostream>

using namespace std;

void testLine(char *plateau, bool & winX, bool &winO, int inc) {
    bool O(true), X(true);
    for (int i = 0; i < 4*inc; i+=inc) {
        if (plateau[i] != 'O' && plateau[i] != 'T') {
            O = false;
        }
        if (plateau[i] != 'X' && plateau[i] != 'T') {
            X = false;
        }
    }

    winO |= O;
    winX |= X;
}

int main()
{
    int n;
    cin >> n;

    char plateau[16];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 16; j++) {
            cin >> plateau[j];
        }

        bool winX (false), winO(false);

        for (int j = 0; j < 4; j++) {
            testLine(plateau + j*4, winX, winO, 1);
            testLine(plateau + j, winX, winO, 4);
        }
        testLine(plateau, winX, winO, 5);
        testLine(plateau+3, winX, winO, 3);

        if (winO) {
            cout << "Case #" << (i+1) << ": O won" << endl;
        } else if (winX) {
            cout << "Case #" << (i+1) << ": X won" << endl;
        } else {
            bool incomplete = false;
            for (int j = 0; j < 16; j++) {
                if (plateau[j] == '.') {
                    incomplete = true;
                    break;
                }
            }
            if (incomplete) {
                cout << "Case #" << (i+1) << ": Game has not completed" << endl;
            } else {
                cout << "Case #" << (i+1) << ": Draw" << endl;
            }
        }
    }

    return 0;
}

