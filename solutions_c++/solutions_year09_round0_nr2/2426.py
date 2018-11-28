#include <iostream>
#include <fstream>

using namespace std;

int map[100][100];
char basin[100][100];
int h, w, empty;
int x, y;

void lowest(int i, int j) {
    x = -1; y = -1;
    int alt = 100000;
    if (i > 0) {
        if (alt > map[i - 1][j] && map[i - 1][j] < map[i][j]) {
            alt = map[i - 1][j];
            x = i - 1;
            y = j;
        }
    }
    if (j > 0) {
        if (alt > map[i][j - 1] && map[i][j - 1] < map[i][j]) {
            alt = map[i][j - 1];
            x = i;
            y = j - 1;
        }
    }
    if (j < w - 1) {
        if (alt > map[i][j + 1] && map[i][j + 1] < map[i][j]) {
            alt = map[i][j + 1];
            x = i;
            y = j + 1;
        }
    }
    if (i < h - 1) {
        if (alt > map[i + 1][j] && map[i + 1][j] < map[i][j]) {
            alt = map[i + 1][j];
            x = i + 1;
            y = j;
        }
    }
}

void floodfill(int i, int j, int b) {
    if (!basin[i][j]) {
        basin[i][j] = b;
        empty--;
        lowest(i, j);
        if (x != -1)
            floodfill(x, y, b);
        if (i > 0) {
            lowest(i - 1, j);
            if (x == i && y == j)
                floodfill(i - 1, j, b);
        }
        if (j > 0) {
            lowest(i, j - 1);
            if (x == i && y == j)
                floodfill(i, j - 1, b);
        }
        if (i < h - 1) {
            lowest(i + 1, j);
            if (x == i && y == j)
                floodfill(i + 1, j, b);
        }
        if (j < w - 1) {
            lowest(i, j + 1);
            if (x == i && y == j)
                floodfill(i, j + 1, b);
        }
    }
}

int main () {
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");

    int t;
    fin >> t;
    int total = t;

    while (t) {
        int temp;
        fin >> h >> w;
        empty = h * w;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                fin >> temp;
                map[i][j] = temp;
                basin[i][j] = 0;
            }
        }
        int b = 1;
        for (int j = 0; j < h; j++) {
            for (int k = 0; k < w; k++) {
                if (!basin[j][k])
                    floodfill(j, k, b++);
                if (!empty)
                    break;
            }
            if (!empty)
                break;
        }
        fout << "Case #" << total - t + 1 << ":\n";
        for (int i = 0; i < h; i++) {
            fout << (char) (basin[i][0] + 'a' - 1);
            for (int j = 1; j < w; j++)
                fout << " " << (char) (basin[i][j] + 'a' - 1);
            fout << endl;
        }
        t--;
    }
}
