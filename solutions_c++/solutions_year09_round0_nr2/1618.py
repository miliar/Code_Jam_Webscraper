#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
int H, W, basins[101][101], sols[101][101];
int wherefalls(int a, int b, int &aa, int &bb) {
    aa = a, bb = b;
    int cur = basins[a][b];
    if (a && cur > basins[a-1][b]) aa = a - 1, bb = b, cur = basins[a-1][b];
    if (b && cur > basins[a][b-1]) bb = b - 1, aa = a,  cur = basins[a][b-1];
    if (b + 1 < W && cur > basins[a][b+1]) bb = b + 1, aa = a, cur = basins[a][b+1];
    if (a + 1 < H && cur > basins[a+1][b]) aa = a + 1, bb = b, cur = basins[a+1][b];
    return sols[aa][bb];
}
int fallfrom(int a, int b) {
    int aa, bb;
    wherefalls(a, b, aa, bb);
    if (sols[aa][bb]) return sols[aa][bb];
    sols[aa][bb] = sols[a][b];
    return fallfrom(aa, bb);
}
void fallreplace(int a, int b, int r) {
    int aa, bb;
    sols[a][b] = r;
    wherefalls(a, b, aa, bb);
    if (sols[aa][bb] == r) return;
    fallreplace(aa, bb, r); 
}
void b_case(FILE *fp, int casen) {
    cout << "Case #" << casen << ":" << endl;
    int c='a', aa, bb;
    fscanf(fp, "%d %d", &H, &W);
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            fscanf(fp, "%d", &basins[i][j]);
            sols[i][j] = 0;
        }
    }
    for (int x = 0; x < H; x++) {
        for (int y = 0; y < W; y++) {
            if (!sols[x][y]) {
                int w = wherefalls(x, y, aa, bb);
                sols[x][y] = w ? w : c++;
                int r = fallfrom(x, y);
                if (!w && r < c - 1) {
                    fallreplace(x, y, r);
                    c--;
                }
            }
            cout << (char)sols[x][y] << ((y+1==W)?"\n":" ");
        }
    }
}
int main(int argc, char **argv) {
    int maps;
    FILE *fp = fopen(argv[1], "r");
    fscanf(fp, "%d", &maps);
    for (int c = 1; c <= maps; c++) b_case(fp, c);
    fclose(fp);
    return 0;
}

