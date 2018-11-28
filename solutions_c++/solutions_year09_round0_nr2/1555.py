#include <iostream>
#include <cstring>

using namespace std;

int A[128][128], H, W;
int dirs[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
char basin;
char label[128][128];

void dfs(int i, int j)
{
    int k, bi = -1, bj, ni, nj;
    if (label[i][j])
        return;
    for (k = 0; k < 4; k++) {
        ni = i + dirs[k][0];
        nj = j + dirs[k][1];
        if (A[ni][nj] && (bi < 0 || A[ni][nj] < A[bi][bj])) {
            bi = ni;
            bj = nj;
        }
    }
    if (bi > 0 && A[bi][bj] < A[i][j]) {
        dfs(bi, bj);
        label[i][j] = label[bi][bj];
    } else {
        label[i][j] = basin++;
    }
}

void solve_one(void)
{
    int i, j;
    cin >> H >> W;
    basin = 'a';
    memset(A, 0, sizeof(A));
    memset(label, 0, sizeof(label));
    for (i = 1; i <= H; i++)
    for (j = 1; j <= W; j++) {
        cin >> A[i][j];
        A[i][j] ++;
    }
    for (i = 1; i <= H; i++) {
        for (j = 1; j <= W; j++) {
            dfs(i, j);
            if (j > 1)
                cout << " ";
            cout << label[i][j];
        }
        cout << endl;
    }
}

int main(void)
{
    int i, T;
    cin >> T;
    for (i = 1; i <= T; i++) {
        cout << "Case #" << i << ":\n";
        solve_one();
    }
    
    return 0;
}
