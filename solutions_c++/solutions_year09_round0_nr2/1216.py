#include <iostream>
using namespace std;

const int dh[4] = {-1,0,0,1};
const int dw[4] = {0,-1,1,0};

int T,H,W;
int altitude[105][105];
int id[105][105];
char label[105][105];
char nextlabel;
bool visited[105][105], labeled[105][105];
int X;

int updateid(int h, int w);
void updatelabel(int h, int w);

int main() {
    cin >> T;
    for (X = 1; X <= T; X++) {
        cin >> H >> W;
        for (int i = 0; i <= H+1; i++)
            altitude[i][0] = altitude[i][W+1] = 10001;
        for (int i = 0; i <= W+1; i++)
            altitude[0][i] = altitude[H+1][i] = 10001;
        for (int i = 1; i <= H; i++)
            for (int j = 1; j <= W; j++) {
                cin >> altitude[i][j];
                id[i][j] = (i-1)*W + (j-1);
                visited[i][j] = labeled[i][j] = false;
            }

        for (int i = 1; i <= H; i++)
            for (int j = 1; j <= W; j++)
                if (!visited[i][j])
                    updateid(i,j);
        nextlabel = 'a';
        for (int i = 1; i <= H; i++)
            for (int j = 1; j <= W; j++)
                if (!labeled[i][j])
                    updatelabel(i,j);

        cout << "Case #" << X << ":" << endl;
        for (int i = 1; i <= H; i++)
            for (int j = 1; j <= W; j++)
                cout << label[i][j] << (j<W ? ' ' : '\n');
    }

    return 0;
}

int updateid(int h, int w) {
    if (!visited[h][w]) {
        visited[h][w] = true;
        int min = altitude[h][w];
        int minid = -1;
        for (int i = 0; i < 4; i++)
            if (altitude[h+dh[i]][w+dw[i]] < min) {
                min = altitude[h+dh[i]][w+dw[i]];
                minid = i;
            }
        if (minid != -1)
            id[h][w] = updateid(h+dh[minid],w+dw[minid]);
    }
    return id[h][w];
}

void updatelabel(int h, int w) {
    for (int i = 1; i <= H; i++)
        for (int j = 1; j <= W; j++)
            if (id[i][j] == id[h][w]) {
                labeled[i][j] = true;
                label[i][j] = nextlabel;
            }
    nextlabel++;
}
