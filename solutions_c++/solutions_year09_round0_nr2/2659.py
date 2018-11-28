#include <iostream>
#include <new>
#include <algorithm>

#define INF 10001;
#define NORTH 0
#define WEST 1
#define EAST 2
#define SOUTH 3

using namespace std;

int h, w;
int map[100][100];
int newmap[100][100];
char current;

int minaltitude(int north, int west, int east, int south) {
    int m = min(north, min(west, min(east, south)));

    if (m == north) return NORTH;
    else if (m == west) return WEST;
    else if (m == east) return EAST;
    else return SOUTH;
}

char rec(int i, int j, char f) {
    int north, west, east, south;

    //cout << "#" << i << " " << j << "\n";

    newmap[i][j] = f;

    // north
    if (i > 0) north = map[i-1][j];
    else north = INF;
    // west
    if (j > 0) west = map[i][j-1];
    else west = INF;
    // east
    if (j < w-1) east = map[i][j+1];
    else east = INF;
    // north
    if (i < h-1) south = map[i+1][j];
    else south = INF;

    // case sink
    if (min(north, min(west, min(east, south))) >= map[i][j]) return f;

    int flow = minaltitude(north, west, east, south);

    switch(flow) {
        case NORTH:
            if (newmap[i-1][j] != 0) { newmap[i][j] = newmap[i-1][j]; current--; return newmap[i][j]; }
            newmap[i][j] = rec(i-1, j, f);
            break;
        case WEST:
            if (newmap[i][j-1] != 0) { newmap[i][j] = newmap[i][j-1]; current--; return newmap[i][j]; }
            newmap[i][j] = rec(i, j-1, f);
            break;
        case EAST:
            if (newmap[i][j+1] != 0) { newmap[i][j] = newmap[i][j+1]; current--; return newmap[i][j]; }
            newmap[i][j] = rec(i, j+1, f);
            break;
        case SOUTH:
            if (newmap[i+1][j] != 0) { newmap[i][j] = newmap[i+1][j]; current--; return newmap[i][j]; }
            newmap[i][j] = rec(i+1, j, f);
            break;
    }

    return newmap[i][j];
}

int main()
{
    int t;

    cin >> t;

    // number of maps
    for (int x=0; x<t; x++) {
        cout << "Case #" << (x+1) << ":\n";
        cin >> h;
        cin >> w;

        memset(newmap, 0, 101 * 101); // setting 0's

        current = 'a';
        // reading
        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
                cin >> map[i][j];
            }
        }

        // computing
        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
                if (newmap[i][j] != 0) continue;
                rec(i, j, current++);
            }
        }

        //printing
        int i, j;
        for (i=0; i<h; i++) {
            for (j=0; j<w-1; j++) {
                cout << (char)newmap[i][j] << " ";
            }
            cout << (char)newmap[i][j] << "\n";
        }
    }
}
