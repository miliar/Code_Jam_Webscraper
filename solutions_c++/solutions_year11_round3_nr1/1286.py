#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> TIV;
typedef vector<short> TSV;

typedef vector<char> TCV;
typedef vector<TCV> TTCV;

bool replaceblue(TTCV &grid){
    size_t row = 0;
    size_t col = 0;

    for(; row < grid.size(); ++row) {
        for(col = 0; col < grid[row].size(); ++col){
            if( grid[row][col] == '#' ) {
                if(grid[row].size() <= (col + 1)
                   || grid.size() <= (row + 1)){
                    return false;
                }
                else {
                    if(grid[row][col] == '/' || grid[row][col] == '\\' || grid[row][col] == '.') {
                        return false;
                    }
                    else {
                        grid[row][col] = '/';
                    }

                    if(grid[row][col+1] == '/' || grid[row][col+1] == '\\' || grid[row][col+1] == '.'){
                        return false;
                    }
                    else {
                        grid[row][col+1] = '\\';
                    }

                    if(grid[row+1][col] == '/' || grid[row+1][col] == '\\' || grid[row+1][col] == '.'){
                        return false;
                    }
                    else {
                        grid[row+1][col] = '\\';
                    }

                    if(grid[row+1][col+1] == '/' || grid[row+1][col+1] == '\\' || grid[row+1][col+1] == '.'){
                        return false;
                    }
                    else {
                        grid[row+1][col+1] = '/';
                    }
                }
            }
        }
    }
    return true;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    for(int c = 0; c < numCases; c++) {
        TTCV grid;

        short r = 0;
        short col = 0;
        char co = 0;

        in >> r;
        in >> col;

        for(short i = 0; i < r; i++){
            TCV row;
            for(short j = 0; j < col; j++){
                in >> co;
                row.push_back(co);
            }
            grid.push_back(row);
        }

        bool replaced = replaceblue(grid);

        out << "Case #" << c + 1 << ":" << endl;
        if(replaced){
            TTCV::iterator rit = grid.begin();
            for(; rit != grid.end(); ++rit){
                TCV::iterator cit = rit->begin();
                for(;cit!=rit->end(); ++cit){
                    out << *cit;
                }
                out << endl;
            }
        }
        else {
            out << "Impossible" << endl;
        }
    }

    in.close();
    out.close();
    return 0;
}
