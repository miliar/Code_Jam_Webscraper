#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define MAXDIMS 101
#define MAXSINKS 26
#define NORTH 4
#define WEST 3
#define EAST 2
#define SOUTH 1
#define SINK 0

using namespace std;

int gridvals[MAXDIMS][MAXDIMS];
int gridmarked[MAXDIMS][MAXDIMS];
int height, width;
int mark;

int flowdir(int h, int w) {
    int lowest = INT_MAX;
    int loc = SINK;
    if (h - 1 >= 0 && gridvals[h - 1][w] < lowest && gridvals[h - 1][w] < gridvals[h][w]) {
        lowest = gridvals[h - 1][w];
        loc = NORTH;
    }
    if (w - 1 >= 0 && gridvals[h][w - 1] < lowest && gridvals[h][w - 1] < gridvals[h][w]) {
        lowest = gridvals[h][w - 1];
        loc = WEST;
    }
    if (w + 1 < width && gridvals[h][w + 1] < lowest && gridvals[h][w + 1] < gridvals[h][w]) {
        lowest = gridvals[h][w + 1];
        loc = EAST;
    }
    if (h + 1 < height && gridvals[h + 1][w] < lowest && gridvals[h + 1][w] < gridvals[h][w]) {
        loc = SOUTH;
    }
    return loc;
}

void marker(int h, int w) {
    gridmarked[h][w] = mark;
    
    if (h + 1 < height && !gridmarked[h + 1][w] && flowdir(h + 1, w) == NORTH) 
        marker(h + 1, w);
    if (w + 1 < width && !gridmarked[h][w + 1] && flowdir(h, w + 1) == WEST)
        marker(h, w + 1);
    if (w - 1 >= 0 && !gridmarked[h][w - 1] && flowdir(h, w - 1) == EAST)
        marker(h, w - 1);
    if (h - 1 >= 0 && !gridmarked[h - 1][w] && flowdir(h - 1, w) == SOUTH)
        marker(h - 1, w);
}

int main() {
    int numcases;
    
    cin >> numcases;
    for (int casenum = 1; casenum <= numcases; casenum++) {
        mark = 1;
        cin >> height >> width;

        for (int h = 0; h < height; h++)
            for (int w = 0; w < width; w++) {
                gridmarked[h][w] = 0;
                cin >> gridvals[h][w];
            }

        for (int h = 0; h < height; h++)
            for (int w = 0; w < width; w++) {
                if (!gridmarked[h][w] && !flowdir(h, w)) {
                    marker(h, w);
                    mark++;
                }
            }
       
        char chars[MAXSINKS + 1];
        for (int i = 0; i < MAXSINKS; i++)
           chars[i] = 0;

        char countsink = 'a';

        cout << "Case #" << casenum << ":" << endl;
        for (int h = 0; h < height; h++){
            for (int w = 0; w < width; w++) { 
                if (!chars[gridmarked[h][w]])
                   chars[gridmarked[h][w]] = countsink++;
                cout << chars[gridmarked[h][w]] << " ";
            }
            cout << endl;
        } 
    }
    vector<string> dict;

    return 0;
}

