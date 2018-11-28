#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int x = 1; x <= T; x++) {

        char ch[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> ch[i][j];
            }
        }

        int Xcount;
        int Ocount;
        bool T;

        bool inGame = false;
        bool X = false;
        bool O = false;

        //0
        Xcount = 0;
        Ocount = 0;
        for (int i = 0; i < 4; i++) {
            T = false;
            for (int j = 0; j < 4; j++) {
                switch (ch[i][j]) {
                    case '.':
                        inGame = true;
                        break;
                    case 'X':
                        Xcount++;
                        break;
                    case 'O':
                        Ocount++;
                        break;
                    case 'T':
                        Xcount++;
                        Ocount++;
                        break;
                }
            }
            if (Xcount == 4) {
                X = true;
            }
            if (Ocount == 4) {
                O = true;
            }
            Xcount = 0;
            Ocount = 0;
        }
        //270
        Xcount = 0;
        Ocount = 0;
        for (int j = 0; j < 4; j++) {
            T = false;
            for (int i = 0; i < 4; i++) {
                switch (ch[i][j]) {
                    case '.':
                        inGame = true;
                        break;
                    case 'X':
                        Xcount++;
                        break;
                    case 'O':
                        Ocount++;
                        break;
                    case 'T':
                        Xcount++;
                        Ocount++;
                        break;
                }
            }
            if (Xcount == 4) {
                X = true;
            }
            if (Ocount == 4) {
                O = true;
            }
            Xcount = 0;
            Ocount = 0;
        }
        //315
        Xcount = 0;
        Ocount = 0;
        T = false;
        for (int i = 0; i < 4; i++) {
            switch (ch[i][i]) {
                case '.':
                    inGame = true;
                    break;
                case 'X':
                    Xcount++;
                    break;
                case 'O':
                    Ocount++;
                    break;
                case 'T':
                    Xcount++;
                    Ocount++;
                    break;
            }
        }
        if (Xcount == 4) {
            X = true;
        }
        if (Ocount == 4) {
            O = true;
        }

        //45
        Xcount = 0;
        Ocount = 0;
        T = false;
        for (int i = 0; i < 4; i++) {
            switch (ch[i][3 - i]) {
                case '.':
                    inGame = true;
                    break;
                case 'X':
                    Xcount++;
                    break;
                case 'O':
                    Ocount++;
                    break;
                case 'T':
                    Xcount++;
                    Ocount++;
                    break;
            }
        }
        if (Xcount == 4) {
            X = true;
        }
        if (Ocount == 4) {
            O = true;
        }

        string res = "Draw";
        if (X) {
            res = "X won";
        } else if (O) {
            res = "O won";
        } else if (inGame) {
            res = "Game has not completed";
        }

        cout << "Case #" << x << ": " << res << endl;
    }
}