#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    char grid[51][51] = {0};
    for (int r = 0; r < T; r++){
        cout << "Case #" << r+1 << ":" << endl;
        int R, C;
        cin >> R >> C;
        for (int i = 0; i < R; i++) cin >> grid[i];
        int cnt = 0;
        for (int y = 0; y < R; y++){
            for (int x = 0; x < C; x++){
                if (grid[y][x] == '#') cnt++;
            }
        }
        if (cnt%4 != 0) {
            cout << "Impossible" << endl;
            continue;
        }
        if (cnt == 0) {
            for (int y = 0; y < R; y++) cout << grid[y] << endl;
            continue;
        }
        for (int y = 0; y < R; y++){
            for (int x = 0; x < C; x++){
                if (grid[y][x] == '#' && grid[y+1][x] == '#' && grid[y][x+1] == '#' && grid[y+1][x+1] == '#'){
                    grid[y][x] = '/';
                    grid[y+1][x] = '\\';
                    grid[y][x+1] = '\\';
                    grid[y+1][x+1] = '/';
                }
            }
        }
        bool flag = false;
        for (int y = 0; y < R; y++){
            for (int x = 0; x < C; x++){
                if (grid[y][x] == '#') {
                    cout << "Impossible" << endl;
                    flag = true;
                }
                if (flag == true) break;
            }
            if (flag == true) break;
        }
        if (flag == true) continue;
        for (int y = 0; y < R; y++) cout << grid[y] << endl;
    }
    return 0;
}
