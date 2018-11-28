#include <iostream>
using namespace std;

int main () {
    char table[4][4];
    int n, instance = 1;
    ios::sync_with_stdio(false);

    cin >> n;
    while (n--) {
        bool completed = true;
        int x = 0, o = 0;
        bool xw = false, ow = false;
        
        cin >> ws;
        for (int i = 0; i < 4; i++) {
            x = o = 0;
            for (int j = 0; j < 4; j++) {
                cin >> table[i][j];
                switch (table[i][j]) {
                    case '.': completed = false; break;
                    case 'X': x++; break;
                    case 'O': o++; break;
                    case 'T': x++; o++; break;
                }
            }
            if (x == 4) xw = true;
            else if (o == 4) ow = true;
            cin >> ws;
        }
        if (xw) { cout << "Case #" << instance++ << ": X won\n"; continue; }
        if (ow) { cout << "Case #" << instance++ << ": O won\n"; continue; }
        
        for (int j = 0; j < 4; j++) {
            x = o = 0;
            for (int i = 0; i < 4; i++) {
                switch (table[i][j]) {
                    case '.': completed = false; break;
                    case 'X': x++; break;
                    case 'O': o++; break;
                    case 'T': x++; o++; break;
                }
            }
            
            if (x == 4) xw = true;
            else if (o == 4) ow = true;
        }
        if (xw) { cout << "Case #" << instance++ << ": X won\n"; continue; }
        if (ow) { cout << "Case #" << instance++ << ": O won\n"; continue; }
        
        x = 0; o = 0;
        for (int i = 0; i < 4; i++) {
            switch (table[i][i]) {
                case '.': completed = false; break;
                case 'X': x++; break;
                case 'O': o++; break;
                case 'T': x++; o++; break;
            }
            if (x == 4) xw = true;
            else if (o == 4) ow = true;
        }
        if (xw) { cout << "Case #" << instance++ << ": X won\n"; continue; }
        if (ow) { cout << "Case #" << instance++ << ": O won\n"; continue; }
        
        
        x = 0; o = 0;
        for (int i = 0; i < 4; i++) {
            switch (table[i][3-i]) {
                case '.': completed = false; break;
                case 'X': x++; break;
                case 'O': o++; break;
                case 'T': x++; o++; break;
            }
            if (x == 4) xw = true;
            else if (o == 4) ow = true;
        }
        if (xw) { cout << "Case #" << instance++ << ": X won\n"; continue; }
        if (ow) { cout << "Case #" << instance++ << ": O won\n"; continue; }
                      
        cout << "Case #" << instance++ << ": ";
        
        if (completed) cout << "Draw\n";
        else cout << "Game has not completed\n";
    }
    return 0;
    
}
