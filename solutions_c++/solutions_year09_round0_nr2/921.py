#include <iostream>
#include <vector>

using namespace std;

enum flowdir {
    NONE,
    NORTH,
    WEST,
    EAST,
    SOUTH
};

inline bool known(char c) {
    return c != 0;
}

flowdir dirOf(const vector< vector<int> >& map, int row, int col) {
    int lowest = 50000;
    flowdir dir = NONE;

    // Down
    if (row < map.size() - 1) {
        int x = map[row+1][col];
        if (x <= lowest) {
            lowest = x;
            dir = SOUTH;
        }
    }

    // Right
    if (col < map[row].size() - 1) {
        int x = map[row][col+1];
        if (x <= lowest) {
            lowest = x;
            dir = EAST;
        }
    }

    // Left
    if (col > 0) {
        int x = map[row][col-1];
        if (x <= lowest) {
            lowest = x;
            dir = WEST;
        }
    }

    // Above
    if (row > 0) {
        int x = map[row-1][col];
        if (x <= lowest) {
            lowest = x;
            dir = NORTH;
        }
    }

    if (lowest < map[row][col]) {
        return dir;
    } else {
        return NONE;
    }
}

// Return if changed
bool refine(const vector< vector<flowdir> >& fd, vector< vector<char> >& ws, int row, int col) {
    if (known(ws[row][col])) return false;

    char other = 0;
    switch (fd[row][col]) {
        case NORTH:
            other = ws[row-1][col];
            break;

        case WEST:
            other = ws[row][col-1];
            break;

        case EAST:
            other = ws[row][col+1];
            break;

        case SOUTH:
            other = ws[row+1][col];
            break;
    }

    if (known(other)) {
        ws[row][col] = other;
        return true;
    } else {
        return false;
    }
}

void rename(char from, char to, vector< vector<char> >& map) {
    vector< vector<char> >::iterator rit;
    for (rit = map.begin(); rit != map.end(); rit++) {
        vector<char>::iterator cit;
        vector<char>& row = *rit;
        for (cit = row.begin(); cit != row.end(); cit++) {
            if (*cit == from) {
                *cit = to;
            }
        }
    }
}

void dumpWsMap(vector< vector<char> > map) {
    vector< vector<char> >::const_iterator rit;
    for (rit = map.begin(); rit != map.end(); rit++) {
        vector<char>::const_iterator cit;
        const vector<char>& row = *rit;
        bool first = true;
        for (cit = row.begin(); cit != row.end(); cit++) {
            if (!first) {
                cout << ' ';
            } else {
                first = false;
            }
            cout << (*cit == 0 ? '.' : *cit);
        }
        cout << endl;
    }
}

void doCase(int num) {
    int H, W;
    cin >> H >> W;


    // Build the map
    vector< vector<int> > map(H);
    for (int i = 0; i < H; i++) {
        map[i].resize(W);
        vector<int>& row = map[i];
        for (int j = 0; j < W; j++) {
            cin >> row[j];
        }
    }

    // Create flow map
    vector< vector<flowdir> > fd(H);
    for (int i = 0; i < H; i++) {
        fd[i].resize(W);
        for (int j = 0; j < W; j++) {
            fd[i][j] = dirOf(map, i, j);
        }
    }

    // Identify sinks
    vector< vector<char> > ws(H);
    char currSink = 'A';
    for (int i = 0; i < H; i++) {
        ws[i].resize(W);
        for (int j = 0; j < W; j++) {
            if (fd[i][j] == NONE) {
                ws[i][j] = currSink++;
            }
        }
    }

    // Refine iteratively
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                changed = refine(fd, ws, i, j) || changed;
            }
        }
    }

    // Translate watershed names
    currSink = 'a';
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            char c = ws[i][j];
            if (c >= 'A' && c <= 'Z') {
                rename(c, currSink++, ws);
            }
        }
    }

    cout << "Case #" << num << ":" << endl;
    dumpWsMap(ws);
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i + 1);
    }
}
