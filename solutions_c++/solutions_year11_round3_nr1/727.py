
#include <iostream>

using namespace std;

char table[51][51];

int main(void)
{
    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        int r, c;
        cin >> r >> c;
        for (int j=0; j<r; j++) {
            cin >> table[j];
            table[j][c] = '\0';
        }

        cout << "Case #" << i << ":" << endl;

        for (int x=0; x<r; x++) {
            for (int y=0; y<c; y++) {
                if (table[x][y] == '.' || table[x][y] == '/' || table[x][y] == '\\') {
                    continue;
                }
                if (x == r-1 || y == c-1) {
                    goto impossible;
                }
                if (table[x][y+1] == '#' && table[x+1][y] == '#'  && table[x+1][y+1] == '#') {
                    table[x][y] = '/';
                    table[x][y+1] = '\\';
                    table[x+1][y] = '\\';
                    table[x+1][y+1] = '/';
                } else {
                    goto impossible;
                }
                
            }
        } 

        for (int x=0; x<r; x++) {
            cout << table[x] << endl;
        }
        continue;

    impossible:
        cout << "Impossible" << endl;
    }
    return 0;
}
