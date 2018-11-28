#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int H, W;
vector<vector<int> > basin;
vector<vector<char> > sink;

char go(const int y, const int x, const char label) 
{
    static int d[4][2] = {
        {-1, 0}, { 0,-1}, { 0, 1}, { 1, 0} };
    if (sink[y][x] != '?') return sink[y][x];
    int lowest = -1;
    int lowestApptitude = INT_MAX;
    for (int i = 0; i < 4; i++) {
        const int dy = y + d[i][0];
        const int dx = x + d[i][1];
        if (0<=dy&&dy<H && 0<=dx&&dx<W
                && basin[dy][dx] < lowestApptitude 
                && basin[dy][dx] < basin[y][x]) {
            lowest = i;
            lowestApptitude = basin[dy][dx];
        }
    }
    if (lowest == -1) {
        sink[y][x] = label;
    } else {
        sink[y][x] = go(y+d[lowest][0],x+d[lowest][1],label);
    }
    return sink[y][x];
}

int main(void)
{
    int T;
    cin >> T;
    for (int caseNo = 1; caseNo <= T; caseNo++) {
        cin >> H >> W;
        basin = vector<vector<int> >(H, vector<int>(W));
        sink = vector<vector<char> >(H, vector<char>(W,'?'));
        for (int y = 0; y < H; y++)
            for (int x = 0; x < W; x++)
                cin >> basin[y][x];

        char label = 'a';
        for (int y = 0; y < H; y++) 
            for (int x = 0; x < W; x++)
                if (sink[y][x] == '?') {
                    if (go(y, x, label) == label)
                        label++;
                }

        printf("Case #%d:\n", caseNo);
        for (int y = 0; y < H; y++)
            for (int x = 0; x < W; x++) {
                cout << sink[y][x];
                if (x == W-1) cout << endl;
                else cout << " ";
            }
    }

    return 0;
}

