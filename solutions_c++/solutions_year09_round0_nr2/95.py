#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

int H, W;
int M[100][100];
char S[100][100];
const int dr[4] = { -1, 0, 0, 1 };
const int dc[4] = { 0, -1, 1, 0 };
char cont;

inline bool check(int r, int c)
{ return 0 <= r && r < H && 0 <= c && c < W; }

bool selneigh(int r, int c, int &nr, int &nc) {
    nr = r, nc = c;
    for (int k = 0; k < 4; k++) {
        int mr = r + dr[k];
        int mc = c + dc[k];
        if (check(mr, mc)) {
            if (M[mr][mc] < M[nr][nc])
                nr = mr, nc = mc;
        }
    }
    return nr != r || nc != c;
}

void flow(int r, int c) {
    int nr, nc;
    char sink = cont;
    vector< pair<int,int> > Q;
    Q.push_back(make_pair(r, c));

    while (selneigh(r, c, nr, nc)) {
        //printf("(%d, %d) -> (%d, %d)\n", r, c, nr, nc);
        if (S[nr][nc] != '\0') {
            sink = S[nr][nc];
            break;
        }
        Q.push_back(make_pair(nr, nc));
        r = nr, c = nc;
    }
    //printf("ok\n");
    for (int i = 0; i < Q.size(); i++)
        S[Q[i].first][Q[i].second] = sink;
    if (sink == cont) ++cont;
    //printf("ok\n");
}

int main() {
    int T; scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        scanf("%d%d", &H, &W);
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                scanf("%d", &M[i][j]);
                S[i][j] = '\0';
            }
        }
        //printf("ok\n");
        cont = 'a';
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
                if (S[i][j] == '\0')
                    flow(i, j);
                else
                    assert('a' <= S[i][j] && S[i][j] <= 'z');
        printf("Case #%d:\n", c);
        for (int i = 0; i < H; i++) {
            putchar(S[i][0]);
            for (int j = 1; j < W; j++) {
                putchar(' ');
                putchar(S[i][j]);
            }
            putchar('\n');
        }
    }
    return 0;
}
