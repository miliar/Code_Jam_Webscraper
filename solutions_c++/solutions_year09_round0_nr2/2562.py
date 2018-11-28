#include <iostream>
#include <climits>
#include <map>

using namespace std;

int mapi[105][105];
char mapx[105][105];

int h, w;
char color = 'a';

void mergec(int y, int x, char c) {
    int w = mapx[y][x];
    if (w == c) return;
    mapx[y][x] = c;

    if (y-1 >= 0 && w == mapx[y-1][x]) {
        mergec(y-1, x, c);
    }

    if (x-1 >= 0 && w == mapx[y][x-1]) {
        mergec(y, x-1, c);
    }

    if (x+1 < h && w == mapx[y][x+1]) {
        mergec(y, x+1, c);
    }

    if (y+1 < h && w == mapx[y+1][x]) {
        mergec(y+1, x, c);
    }
}

void merge(int y1, int x1, int y2, int x2) {
    if (mapx[y1][x1] == ' ' && mapx[y2][x2] != ' ') {
        mapx[y1][x1] = mapx[y2][x2];
    } else if (mapx[y1][x1] != ' ' && mapx[y2][x2] == ' ') {
        mapx[y2][x2] = mapx[y1][x1];
    } else if (mapx[y1][x1] == ' ' && mapx[y2][x2] == ' ') {
        mapx[y1][x1] = color;
        mapx[y2][x2] = color;
        color++;
    } else {
        char c = mapx[y1][x1] < mapx[y2][x2] ? mapx[y1][x1] : mapx[y2][x2];

        mergec(y1, x1, c);
        mergec(y2, x2, c);
    }
}

int main() {
    int cases;
    cin >> cases;

    for (int tc = 0; tc < cases; tc++) {
        color = 'a';
        cin >> h >> w;

        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                mapx[y][x] = ' ';
                cin >> mapi[y][x];
            }
        }

        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                char d = ' ';
                int mind = INT_MAX;

                if (y-1 >= 0 && mapi[y][x] > mapi[y-1][x] && mapi[y-1][x] < mind) {
                    d = 'N';
                    mind = mapi[y-1][x];
                }

                if (x-1 >= 0 && mapi[y][x] > mapi[y][x-1] && mapi[y][x-1] < mind) {
                    d = 'W';
                    mind = mapi[y][x-1];
                }

                if (x+1 < w && mapi[y][x] > mapi[y][x+1] && mapi[y][x+1] < mind) {
                    d = 'E';
                    mind = mapi[y][x+1];
                }

                if (y+1 < h && mapi[y][x] > mapi[y+1][x] && mapi[y+1][x] < mind) {
                    d = 'S';
                    mind = mapi[y+1][x];
                }

                switch (d) {
                    case 'N':
                        merge(y, x, y-1, x);
                        break;
                    case 'W':
                        merge(y, x, y, x-1);
                        break;
                    case 'E':
                        merge(y, x, y, x+1);
                        break;
                    case 'S':
                        merge(y, x, y+1, x);
                        break;
                    case ' ':
                        if (mapx[y][x] == ' ') {
                            merge(y, x, y, x);
                        }
                        break;
                }
            }
        }

        map<char, char> cm;
        color = 'a';

        cout << "Case #" << tc+1 << ":" << endl;

        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if (cm.find(mapx[y][x]) == cm.end()) {
                    cm[mapx[y][x]] = color;
                    color++;
                }

                cout << cm[mapx[y][x]];
                if (x != w-1) {
                    cout << " ";
                }
            }
            cout << endl;
        }
    }

    return 0;
}
