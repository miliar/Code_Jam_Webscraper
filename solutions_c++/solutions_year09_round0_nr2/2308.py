#include <cstdio>
#include <climits>
#include <cstring>
#include <cassert>
#include <algorithm>
using namespace std;

int** field;
char** result;
int H, W;
char basin;

void flow(int i, int j)
{
    //fprintf(stderr, "flow %d %d\n", i, j);
    result[i][j] = 1;
    static int di[] = {-1,  0, 0, 1};
    static int dj[] = { 0, -1, 1, 0};

    int bval = INT_MAX, bi, bj;
    for (int q = 0; q < 4; q++) {
        int ni = i + di[q];
        int nj = j + dj[q];
        if (ni < 0 || nj < 0 || ni >= H || nj >= W)
            continue;
        if (field[ni][nj] >= field[i][j] || result[ni][nj] == 1)
            continue;
        if (bval > field[ni][nj]) {
            bval = field[ni][nj];
            bi = ni;
            bj = nj;
        }
    }

    if (bval == INT_MAX) {
        result[i][j] = basin++;
        return;
    }

    if (!result[bi][bj])
        flow(bi, bj);
    result[i][j] = result[bi][bj];
}

void solve()
{
    scanf("%d %d", &H, &W);
    field = new int*[H];
    result = new char*[H];
    for (int i = 0; i < H; i++) {
        field[i] = new int[W];
        result[i] = new char[W];
        for (int j = 0; j < W; j++) {
            scanf("%d", &field[i][j]);
            result[i][j] = 0;
        }
    }

    basin = 'a';
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (result[i][j])
                continue;
            flow(i, j);
        }
    }

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++)
            printf("%c ", result[i][j]);
        printf("\n");
        delete [] field[i];
        delete [] result[i];
    }
    delete [] field;
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        printf("Case #%d:\n", i + 1);
        solve();
    }
    return 0;
}
