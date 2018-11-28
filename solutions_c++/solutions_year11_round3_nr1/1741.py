#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool solve(istream& ifs, ostream& ofs);

int main()
{
    ifstream ifs("input.txt");
    ofstream ofs("output.txt");
    
    int turns;
    ifs >> turns;
    for (int i = 1; i <= turns; ++i) {
        ofs << "Case #" << i << ":" << endl;
        if (!solve(ifs, ofs)) {
            ofs << "Impossible" << endl;
        }
    }
    
    system("pause");
    return 0;
}

bool solve(istream& ifs, ostream& ofs)
{
    int row;
    int column;
    ifs >> row >> column;
    
    vector< vector<char> > picture(row, vector<char>(column));
    for (int i = 0; i != row; ++i) {
        for (int j = 0; j != column; ++j) {
            ifs >> picture[i][j];
        }
    }
    
    for (int i = 0; i != row; ++i) {
        for (int j = 0; j != column; ++j) {
            if (i != row - 1 && j != column - 1) {
                if (picture[i][j] == '#' && picture[i][j + 1] == '#' && picture[i + 1][j] == '#' && picture[i + 1][j + 1] == '#') {
                    picture[i][j] = '/';
                    picture[i][j + 1] = '\\';
                    picture[i + 1][j] = '\\';
                    picture[i + 1][j + 1] = '/';
                }
            }
        }
    }
    for (int i = 0; i != row; ++i) {
        for (int j = 0; j != column; ++j) {
            if (picture[i][j] == '#') {
                return false;
            }
        }
    }
    
    for (int i = 0; i != row; ++i) {
        for (int j = 0; j != column; ++j) {
            ofs << picture[i][j];
        }
        ofs << endl;
    }
    return true;
}
