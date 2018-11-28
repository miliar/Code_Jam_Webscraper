#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <utility>

using namespace std;

int main() {
    int t;
    cin >> t;
    char grid[100][100];
    
    for (int cn = 1; cn <= t; cn++) {
        int r, c;
        char temp;
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> grid[i][j];
            }
        }
        
        bool possible = true;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '#') {
                    if (j == c - 1 || grid[i][j + 1] == '.') {
                        possible = false;
                        break;
                    } else if (i == r - 1 || grid[i + 1][j] == '.') {
                        possible = false;
                        break;
                    } else if (grid[i + 1][j + 1] == '.') {
                        possible = false;
                        break;
                    } else {
                        grid[i][j] = '/';
                        grid[i + 1][j] = '\\';
                        grid[i][j + 1] = '\\';
                        grid[i + 1][j + 1] = '/';
                    }                    
                }
            }
            if (!possible)
                break;
        }
        
        if (!possible)
            cout << "Case #" << cn << ":\nImpossible\n";
        else {
            cout << "Case #" << cn << ":\n";
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    cout << grid[i][j];
                }
                cout << endl;
            }
        }
    }
}