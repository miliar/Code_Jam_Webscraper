#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

const int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

void color(vector<vector<int> > &flow,
           vector<vector<char> > &label,
           int height, int width,
           int row, int col, char letter)
{
    label[row][col] = letter;

    for (int i = 0; i < 4; ++i) {
        int r = row + dir[i][0];
        int c = col + dir[i][1];
        if (r < 0 || r >= height ||
            c < 0 || c >= width ||
            label[r][c] != '\0') continue;
        if (flow[row][col] == i ||
            flow[r][c] == 3 - i) {
            color(flow, label, height, width, r, c, letter);
        }
    }
}

void solve(vector<vector<int> > &map)
{
    int height = map.size();
    int width = map[0].size();

    vector<vector<int> > flow;
    flow.resize(height);
    for (int i = 0; i < height; ++i) {
        flow[i].resize(width);
    }

    vector<vector<char> > label;
    label.resize(height);
    for (int i = 0; i < height; ++i) {
        label[i].resize(width);
        for (int j = 0; j < width; ++j) {
            label[i][j] = '\0';
        }
    }

    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            int minAlt = map[i][j];
            int minDir = -1;
            for (int k = 0; k < 4; ++k) {
                int row = i + dir[k][0];
                int col = j + dir[k][1];
                if (row < 0 || row >= height ||
                    col < 0 || col >= width) continue;
                if (map[row][col] < minAlt) {
                    minAlt = map[row][col];
                    minDir = k;
                }
            }
            flow[i][j] = minDir;
        }
    }

    char curLabel = 'a';

    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            if (label[i][j] == '\0') {
                color(flow, label, height, width, i, j, curLabel++);
            }
        }
    }

    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            cout << label[i][j] << " ";
        }
        cout << endl;
    }
}

int main(int argc, char **argv)
{
    ifstream fin(argv[1]);

    int T;
    fin >> T;

    for (int i = 0; i < T; ++i) {
        int H, W;
        fin >> H >> W;

        vector<vector<int> > map;
        map.resize(H);
        for (int j = 0; j < H; ++j) {
            map[j].resize(W);
            for (int k = 0; k < W; ++k) {
                fin >> map[j][k];
            }
        }

        cout << "Case #" << i + 1 << ":" << endl;
        solve(map);
    }

    fin.close();

    return 0;
}

