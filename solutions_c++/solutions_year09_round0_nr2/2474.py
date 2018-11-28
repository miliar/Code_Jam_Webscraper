#include <iostream>
#include <string>

using namespace std;

char label;
int h, w;

char getLabel(int *alt, char *map, int x, int y) {
    //cout << "h: " << h << "; w: " << w << "; x: " << x << "; y: " << y << endl;
    int dir, low;
    int pos;
    pos = y*w+x;
    dir = 0;
    low = alt[pos];
    if(map[pos]) {
        return map[pos];
    }
    if(y > 0) {
        if(alt[pos-w] < low) {
            dir = 1;
            low = alt[pos-w];
        }
    }
    if(x > 0) {
         if(alt[pos-1] < low) {
            dir = 2;
            low = alt[pos-1];
        }
    }
    if(x < w - 1) {
         if(alt[pos+1] < low) {
            dir = 3;
            low = alt[pos+1];
        }
    }
    if(y < h - 1) {
        if(alt[pos+w] < low) {
            dir = 4;
            low = alt[pos+w];
        }
    }
    //cout << "dir: " << dir << endl;
    switch(dir) {
        case 0:
            //cout << "label: " << label << " " << x << " " << y << endl;
            map[pos] = label;
            label++;
            break;
        case 1:
            map[pos] = getLabel(alt, map, x, y-1);
            break;
        case 2:
            map[pos] = getLabel(alt, map, x-1, y);
            break;
        case 3:
            map[pos] = getLabel(alt, map, x+1, y);
            break;
        case 4:
            map[pos] = getLabel(alt, map, x, y+1);
            break;
        default:
            break;
    }
    return  map[pos];
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int t;
    int i, x, y;
    int dir, low;
    char tmpLabel;

    cin >> t;

    for(i = 1; i <= t; i++) {
        cout << "Case #" << i << ":" << endl;
        cin >> h >> w;
        label = 'a';
        int alt[h][w];
        char map[h][w];

        for(y = 0; y < h; y++) {
            for(x = 0; x < w; x++) {
                cin >> alt[y][x];
                map[y][x] = 0;
            }
        }

        for(y = 0; y < h; y++) {
            for(x = 0; x < w; x++) {
                if(!map[y][x]) {
                    tmpLabel = getLabel(&(alt[0][0]), &(map[0][0]), x, y);
                }
            }
        }

        for(y = 0; y < h; y++) {
            for(x = 0; x < (w - 1); x++) {
                cout << map[y][x] << ' ';
            }
            cout << map[y][x] << endl;
        }
    }

    return 0;
}
