#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>

using namespace std;

struct Instance {
    int r, c;
    int tiles;
    vector<vector<bool> > colors;
    void topLeft(int* x, int* y);
    bool solve(vector<vector<char> >& output_tiles);

    Instance(int _r, int _c) 
        : r(_r), c(_c),
          tiles(0),
          colors(vector<vector<bool> >(r, vector<bool>(c, false)))
    {}
};

bool Instance::solve(vector<vector<char> >& output_tiles) {
    //cerr << "SOLVE" << endl;
    output_tiles = vector<vector<char> >(r, vector<char>(c, '.'));
    while(tiles > 0) {
        int x;
        int y;
        topLeft(&y, &x);
        //cerr << "topLeft: " << y << " " << x << endl;
        if(x == -1 && y == -1) {
            return false;
        }
        if(x == c - 1 || y == r - 1) {
            return false;
        }
        if(colors[y][x] && colors[y + 1][x] && colors[y][x + 1] && colors[y + 1][x + 1]) {
            //cerr << "Tile at " << y << " " << x << endl;
            colors[y][x] = colors[y + 1][x] = colors[y][x + 1] = colors[y + 1][x + 1] = false;
            tiles -= 4;
            output_tiles[y][x] = '/';
            output_tiles[y][x + 1] = '\\';
            output_tiles[y + 1][x] = '\\';
            output_tiles[y + 1][x + 1] = '/';

        } else {
            return false;
        }
    }
}


void Instance::topLeft(int* x, int* y) {
    *x = -1;
    *y = -1;
    for(int i = 0; i < r; ++i) {
        for(int j = 0; j < c; ++j) {
            if(colors[i][j]) {
                //cerr << "colors " << i << " " << j << endl;
                *y = j;
                *x = i;
                return;
            }
        }
    }
}
                

void readInput(vector<Instance>* instances) {
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i) {
        int r, c;
        cin >> r >> c;
        Instance current(r, c);
        for(int rr = 0; rr < r; ++rr) {
            string ss;
            cin >> ss;
            for(int cc = 0; cc < c; ++cc) {
                if(ss[cc] == '#') {
                    current.colors[rr][cc] = true;
                    ++current.tiles;
                }
            }
        }
        instances->push_back(current);
    }
}


void outputSol(int n, bool possible, const vector<vector<char> >& tiles) {
    cout << "Case #" << n + 1 << ":" << endl;
    if(possible) {
        for(int r = 0; r < tiles.size(); ++r) {
            for(int c = 0; c < tiles[r].size(); ++c) {
                cout << tiles[r][c];
            }
            cout << endl;
        }
    } else {
        cout << "Impossible" << endl;
    }
}

int main() {
    vector<Instance> input;
    readInput(&input);
    for(int i = 0; i < input.size(); ++i) {
        vector<vector<char> > output;
        bool p = input[i].solve(output);
        outputSol(i, p, output);
    }
    return 0;
}
