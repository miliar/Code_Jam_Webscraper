#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int N = 20000;
char a[N][11], list[27], board[N+1];
int len[N], exist[256], R[N+1], L[N+1];

int solve(int n, int w)
{
    int last = n;
    for (int i = 0; i < n; i++)
        if (len[i] == len[w]) {
            R[last] = i;
            L[i] = last;
            last = i;
        }
    R[last] = n;
    L[n] = last;
    memset(exist, -1, sizeof(exist));
    memset(board, 0, sizeof(board));

    int appear = 0, res = 0;
    for (char *x = list; x < list+26 && appear < len[w]; x++) {
        bool flag = false;
        for (int i = R[n]; i != n && !flag; i = R[i])
            for (int j = 0; j < len[w] && !flag; j++)
                if (a[i][j] == *x)
                    flag = true;
        if (!flag) continue;
        
        int appear2 = appear;
        for (int j = 0; j < len[w]; j++)
            if (a[w][j] == *x) {
                board[j] = *x;
                appear2++;
            }
        if (appear2 > appear) exist[*x] = 1;
        else exist[*x] = 0, res++;
        appear = appear2;
        for (int i = R[n]; i != n; i = R[i])
            for (int j = 0; j < len[w]; j++)
                if ((exist[a[i][j]] > 0 || board[j]) && board[j] != a[i][j] || !exist[a[i][j]]) {
                    L[R[i]] = L[i];
                    R[L[i]] = R[i];
                    break;
                }
    }
    return res;
}

int main()
{
    int cases, n, m;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", a[i]);
            len[i] = strlen(a[i]);
        }
        printf("Case #%d:", T);
        for (int i = 0; i < m; i++) {
            scanf("%s", list);
            int opt = -1, optx;
            for (int j = 0; j < n; j++) {
                int t = solve(n, j);
                if (t > opt) {
                    opt = t;
                    optx = j;
                }
            }
            printf(" %s", a[optx]);
        }
        puts("");
    }
}
