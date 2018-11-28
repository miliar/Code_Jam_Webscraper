#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    int tcases = 0;
    cin >> tcases;
    for (int i = 1; i <= tcases; ++i) {
        // initialization
        int r = 0, c = 0;
        cin >> r >> c;
        char a[52][52];
        for (int j = 1; j <= 50; ++j) {
            for (int k = 1; k <= 50; ++k) {
                a[j][k] = '.';
            }
        } 

        // read lines
        for (int j = 1; j <= r; ++j) {
            for (int k = 1; k <= c; ++k) {
                cin >> a[j][k];
            }
        } 
        
        // process
        bool fail = false;
        for (int j = 1; j <= r; ++j) {
            for (int k = 1; k <= c; ++k) {
                if (a[j][k] == '#') {
                    if (j+1 <= r && k+1 <= c && a[j+1][k] == '#' && a[j][k+1] == '#' && a[j+1][k+1] == '#') {
                        a[j][k] = '/';
                        a[j][k+1] = '\\';
                        a[j+1][k] = '\\';
                        a[j+1][k+1] = '/';
                    }
                    else {
                        fail = true;
                    }
                }
                if (fail) break;
            }
            if (fail) break;
        }
        
        cout << "Case #" << i << ":" << endl;
        if (fail) {
            cout << "Impossible" << endl;
        }
        else {
            for (int j = 1; j <= r; ++j) {
                for (int k = 1; k <= c; ++k) {
                    cout << a[j][k];
                }
                cout << endl;
            }
        } 
        
    }
}