#include <iostream>
using namespace std;

int charToInt(const char& c) {
    switch (c) {
        case 'X': return 1;
        case 'O': return 5;
        case 'T': return 0;
        default: return 100;
    }
}

int main(char* argv[]) {
    ios_base::sync_with_stdio(false);

    int T;
    int tab[4][4];
    char a, b, c, d;
    char result = 0;
    bool isDot = false;

    cin >> T;
    for (int i = 0; i < T; i++) {
        result = 0;
        isDot = false;

        for (int j = 0; j < 4; j++) {
            cin >> a >> b >> c >> d;

            if (result == 0) {
                tab[j][0] = charToInt(a);
                tab[j][1] = charToInt(b);
                tab[j][2] = charToInt(c);
                tab[j][3] = charToInt(d);

                if (!isDot && (tab[j][0] == 100 || tab[j][1] == 100 || tab[j][2] == 100 || tab[j][3] == 100))
                    isDot = true;

                int sum = tab[j][0] + tab[j][1] + tab[j][2] + tab[j][3];

                if (sum == 3 || sum == 4)
                    result = 'X';
                else if (sum == 15 || sum == 20)
                    result = 'O';
            }
        }

        if (result == 0) {
            for (int j = 0; j < 4; j++) {
                int sum = tab[0][j] + tab[1][j] + tab[2][j] + tab[3][j];

                if (sum == 3 || sum == 4)
                    result = 'X';
                else if (sum == 15 || sum == 20)
                    result = 'O';
            }
        }

        if (result == 0) {
            int sum_1 = tab[0][0] + tab[1][1] + tab[2][2] + tab[3][3];
            
            if (sum_1 == 3 || sum_1 == 4)
                result = 'X';
            else if (sum_1 == 15 || sum_1 == 20)
                result = 'O';
        } 

        if (result == 0) {
            int sum_2 = tab[0][3] + tab[1][2] + tab[2][1] + tab[3][0];

            if (sum_2 == 3 || sum_2 == 4)
                result = 'X';
            else if (sum_2 == 15 || sum_2 == 20)
                result = 'O';
        }

        if (result == 'X')
            cout << "Case #" << i+1 << ": X won" << endl;
        else if (result == 'O') 
            cout << "Case #" << i+1 << ": O won" << endl;
        else if (result == 0 && !isDot)
            cout << "Case #" << i+1 << ": Draw" << endl;
        else 
            cout << "Case #" << i+1 << ": Game has not completed" << endl;
    }

    return 0;
}