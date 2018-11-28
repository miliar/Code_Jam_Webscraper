#include <iostream>
#include <math.h>

using namespace std;

int main() {
    unsigned int t;

    cin >> t;

    for(double tt = 0; tt < t; tt++) {
        int r, c;
        cin >> r >> c;
        char p[r+1][c+1];

        for(int i = 0; i < r; i++) {
            cin >> p[i];
        }

        for(int i = 0; i < r-1; i++) {
            for(int j = 0; j < c-1; j++) {
                if(p[i][j] == '#' && p[i+1][j] == '#' && p[i][j+1] == '#' && p[i+1][j+1] == '#') {
                    p[i][j] = p[i+1][j+1] = '/';
                    p[i+1][j] = p[i][j+1] = '\\';
                }
            }
        }

        int ok = 1;
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                if(p[i][j] == '#') ok = 0;
            }
        }

        cout << "Case #" << tt+1 << ":\n";
        if(!ok)
            cout << "Impossible\n";
        else {
            for(int i = 0; i < r; i++) 
                cout << p[i] << "\n";
        }

    }

    return 0;
}
