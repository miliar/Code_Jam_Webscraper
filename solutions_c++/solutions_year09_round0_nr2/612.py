#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

const char iname[] = "B-large.in";
const char oname[] = "B-large.out";

const int MAXN = 105;

void DF(int rows, int cols, int r, int c, int M[][MAXN], int hasMark[][MAXN], int &countMarks)
{
    int dx[] = {-1, 0, 0, +1};
    int dy[] = {0, -1, +1, 0};
    int countdirs = sizeof(dx) / sizeof(dx[0]);
    int height = -1, dir;

    for (int i = 0; i < countdirs; ++ i) {
        int x = r + dx[i];
        int y = c + dy[i];
        if (x < 0 || y < 0 || x >= rows || y >= cols)
            continue ;
        if (M[x][y] < height || height == -1)
            height = M[x][y], dir = i;
    }
    if (height >= M[r][c] || height == -1) {
        // (r, c) is a sink
        if (hasMark[r][c] == 0)
            hasMark[r][c] = (++ countMarks);
    }
    else {
        int x = r + dx[dir];
        int y = c + dy[dir];
        if (hasMark[x][y] == 0)
            DF(rows, cols, x, y, M, hasMark, countMarks);
        hasMark[r][c] = hasMark[x][y];
    }
}

int main(void)
{
    ifstream in(iname);
    ofstream out(oname);
    int runs;
    int M[MAXN][MAXN], hasMark[MAXN][MAXN];

    in >> runs;
    for (int iruns = 0; iruns < runs; ++ iruns) {
        int rows, cols;
        in >> rows >> cols;
        for (int i = 0; i < rows; ++ i) {
            for (int j = 0; j < cols; ++ j)
                in >> M[i][j];
        }
        int countMarks = 0;
        memset(hasMark, 0, sizeof hasMark);
        for (int i = 0; i < rows; ++ i) {
            for (int j = 0; j < cols; ++ j)
                if (hasMark[i][j] == 0)
                    DF(rows, cols, i, j, M, hasMark, countMarks);
        }
        char whichMark[27], letter = 'a';
        memset(whichMark, 0, sizeof whichMark);

        out << "Case #" << (iruns + 1) << ":\n";
        for (int i = 0; i < rows; ++ i) {
            for (int j = 0; j < cols; ++ j) {

                if (!whichMark[ hasMark[i][j] - 1 ])
                    whichMark[ hasMark[i][j] - 1 ] = (letter ++);

                out << whichMark[ hasMark[i][j] - 1 ];
                if (j < cols - 1)
                    out << " ";
            }
            out << "\n";
        }
    }
    in.close(), out.close();
    return 0;
}
