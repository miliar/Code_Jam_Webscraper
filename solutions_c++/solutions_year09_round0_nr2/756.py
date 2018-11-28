#include <iostream>
#include <cstring>

using namespace std;

unsigned int map[100+2][100+2];
int label[100+2][100+2];
int curlabel;

char names[26];

void flow(int x, int y){
    int lowx = -1, lowy = -1;
    unsigned int lowest = 99999999;

    if (label[x][y] != -1)
        return;

    if (map[x][y-1] < lowest){ //North
        lowx = x;
        lowy = y-1;
        lowest = map[x][y-1];
    }

    if (map[x-1][y] < lowest){ //West
        lowx = x-1;
        lowy = y;
        lowest = map[x-1][y];
    }

    if (map[x+1][y] < lowest){ //East
        lowx = x+1;
        lowy = y;
        lowest = map[x+1][y];
    }

    if (map[x][y+1] < lowest){ //South
        lowx = x;
        lowy = y+1;
        lowest = map[x][y+1];
    }

    if (lowest < map[x][y]){
        flow(lowx, lowy);
        label[x][y] = label[lowx][lowy];
    } else {
        label[x][y] = curlabel; //new sink
        curlabel++;
    }
}

int main(){
    int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        int H, W;
        cin >> H >> W;

        //set outer cells to infinite heigth
        memset(map, -1, sizeof(map));

        memset(label, -1, sizeof(label));
        curlabel = 0;
        memset(names, 0, sizeof(names));

        for (int y = 1; y <= H; y++)
            for (int x = 1; x <= W; x++)
                cin >> map[x][y];

        for (int y = 1; y <= H; y++)
            for (int x = 1; x <= W; x++)
                flow(x, y);

        int n = 0;
        for (int y = 1; y <= H; y++)
            for (int x = 1; x <= W; x++)
                if (names[label[x][y]] == 0){
                    names[label[x][y]] = n + 'a';
                    n++;
                }

        cout << "Case #" << t+1 << ":"<< endl;
        for (int y = 1; y <= H; y++)
            for (int x = 1; x <= W; x++){
                cout << names[label[x][y]];
                if (x < W)
                    cout << " ";
                else
                    cout << endl;
            }
    }
    return 0;
}
