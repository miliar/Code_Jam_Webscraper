#include <iostream>
#include <fstream>

using namespace std;

int main() {
    fstream fin ("A-large.in", fstream::in);
    int cases; fin >> cases;
    string answers[cases];
    fstream fout ("output.txt", fstream::out);
    for (int t = 0; t < cases; t++) {
        int R, C;
        fin >> R >> C;
        string grid[R];
        for (int i = 0; i < R; i++) fin >> grid[i];
        bool poss = true;
        fout << "Case #" << t+1 << ":" << endl;
        for (int y = 0; y < R && poss; y++) {
            for (int x = 0; x < C && poss; x++) {
                if (grid[y][x] == '#') {
                    if (y+1 != R && x+1 != C &&
                        grid[y+1][x] == '#' &&
                        grid[y][x+1] == '#' &&
                        grid[y+1][x+1] == '#') {
                        grid[y][x] = '/';
                        grid[y+1][x] = '\\';
                        grid[y][x+1] = '\\';
                        grid[y+1][x+1] = '/';
                    }
                    else {
                        fout << "Impossible" << endl;
                        poss = false;
                    }
                }
            }
        }
        for (int y = 0; y < R && poss; y++) {
            for (int x = 0; x < C && poss; x++) {
                fout << grid[y][x];
            }fout << endl;
        }
    }
    return 0;
}
