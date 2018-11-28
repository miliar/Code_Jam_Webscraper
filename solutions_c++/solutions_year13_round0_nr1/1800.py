/*
	https://code.google.com/codejam/contest/2270488/dashboard#s=p0
*/
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int T;
    string inStr;

    int comparer[11] = {0, };
    
    // horizontal
    comparer[0] = 1 | 1 << 1 | 1 << 2 | 1 << 3;
    comparer[1] = comparer[0] << 4;
    comparer[2] = comparer[1] << 4;
    comparer[3] = comparer[2] << 4;
    
    // vertical
    comparer[4] = 1 | 1 << 4 | 1 << 8 | 1 << 12;
    comparer[5] = comparer[4] << 1;
    comparer[6] = comparer[5] << 1;
    comparer[7] = comparer[6] << 1;
    
    // diagonal
    comparer[8] = 1 | 1 << 5 | 1 << 10 | 1 << 15;
    comparer[9] = 1 << 3 | 1 << 6 | 1 << 9 | 1 << 12;
    
    comparer[10] = 0;
    for (int i = 0; i < 16; i++)
        comparer[10] |= (1 << i);
  
    cin >> T;
    getline (cin, inStr);   // ignoring a newline
    
    int* X = new int[T];
    int* O = new int[T];
    
    for (int i = 0; i < T; i++) {
        X[i] = O[i] = 0;
        
        for (int j = 0; j < 4; j++) {
            getline (cin, inStr);
            
            for (int k = 0; k < 4; k++) {
                char ch = inStr.at(k);
                
                if (ch == 'X') {
                    X[i] |= 1 << (j * 4 + k);
                } else if (ch == 'O') {
                    O[i] |= 1 << (j * 4 + k);
                } else if (ch == 'T') {
                    X[i] |= 1 << (j * 4 + k);
                    O[i] |= 1 << (j * 4 + k);
                }
            }
        }
        
        int result = 0; // 0: not completed 1: X wins 2: O wins 3: draw
        
        for (int j = 0; j < 10; j++) {
            if ((X[i] & comparer[j]) == comparer[j]) // X wins
                result = 1;
            else if ((O[i] & comparer[j]) == comparer[j]) // O wins
                result = 2;
                
            if (result)
                break;
        }
        
        if (!result && ((X[i] | O[i]) & comparer[10]) == comparer[10]) // draw
            result = 3;
        
        cout << "Case #" << (i + 1) << ": ";
        switch (result) {
            case 0:
                cout << "Game has not completed";
                break;
            case 1:
                cout << "X won";
                break;
            case 2:
                cout << "O won";
                break;
            case 3:
                cout << "Draw";
        }
        cout << endl;
        
        getline (cin, inStr); // ignoring a newline
    }

    return 0;
}
