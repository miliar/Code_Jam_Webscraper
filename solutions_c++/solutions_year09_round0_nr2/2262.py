#include <iostream>
#include <algorithm>
using namespace std;

/*
alejolp@alejolp.com
*/

struct cell {
    short altitude;
    signed char basin;
    signed char visited;
};

cell mapdata[100][100];
int T, W, H;

void walkfrom(int x, int y, int& nextbasin) {
    int minx, miny, minalt;

    if (mapdata[y][x].visited)
        return;

    mapdata[y][x].visited = 1;

    if (nextbasin == -1 && mapdata[y][x].basin != -1) {
        nextbasin = mapdata[y][x].basin;
    }

    if (1)
    {

        minalt = mapdata[y][x].altitude;
        minx = miny = -1;

        // Up
        if (y > 0 && mapdata[y - 1][x].altitude < minalt) {
            minalt = mapdata[y - 1][x].altitude;
            minx = x;
            miny = y - 1;
        }

        // Left
        if (x > 0 && mapdata[y][x - 1].altitude < minalt) {
            minalt = mapdata[y][x - 1].altitude;
            minx = x - 1;
            miny = y;
        }

        // Right
        if (x < (W - 1) && mapdata[y][x + 1].altitude < minalt) {
            minalt = mapdata[y][x + 1].altitude;
            minx = x + 1;
            miny = y;
        }

        // Down
        if (y < (H - 1) && mapdata[y + 1][x].altitude < minalt) {
            minalt = mapdata[y + 1][x].altitude;
            minx = x;
            miny = y + 1;
        }

        if (nextbasin != -1 && mapdata[y][x].basin == -1) {
            mapdata[y][x].basin = nextbasin;
        }

        if (minx != -1)
            walkfrom(minx, miny, nextbasin);

        mapdata[y][x].visited = 0;
    }
}

void printmap() {
    for (int y = 0; y < H; ++y) {
        cout << (char)((int)'a' + mapdata[y][0].basin);
        for (int x = 1; x < W; ++x) {
            cout << " " << (char)((int)'a' + mapdata[y][x].basin);
        }
        cout << endl;
    }
}

int main(int argc, char** argv) {
    cin >> T;

    for (int mapnum = 0; mapnum < T; ++mapnum) {
        cin >> H;
        cin >> W;

        for (int y = 0; y < H; ++y) {
            for (int x = 0; x < W; ++x) {
                cin >> mapdata[y][x].altitude;
                mapdata[y][x].basin = -1;
                mapdata[y][x].visited = 0;
            }
        }

        int nextbasinglobal = 0;

        for (int y = 0; y < H; ++y) {
            for (int x = 0; x < W; ++x) {
                int nextbasin = -1;

                walkfrom(x, y, nextbasin);

                if (nextbasin == -1)
                    nextbasin = nextbasinglobal++;

                walkfrom(x, y, nextbasin);
            }
        }

        cout << "Case #" << (mapnum + 1) << ":" << endl;

        printmap();
    }

    return 0;
}

