/*
  ID: nigo1
  LANG: C++
  TASK:
*/
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>

#define pf printf
#define sf scanf
#define TIME pf("%f", (double)clock()/CLOCKS_PER_SEC);

using namespace std;

int N, M, T, a[512][512], ans[512 + 1];
bool grid[512][512], used[512][512];

char hex2dec (char c) {
    if (c >= '0' && c <= '9') return c - '0';
    else return 10 + c - 'A';
}
void clear () {
    memset (grid, 0, sizeof(grid));
    memset (ans, 0, sizeof(ans));
    memset (used, 0, sizeof(used));
    memset (a, 0, sizeof(a));
}
void calc_a () {
    for (int i = 1; i < N; i++)
        for (int j = 1; j < M; j++)
            if (!used[i][j]) {
                if (grid[i][j] == grid[i - 1][j - 1] && grid[i][j] != grid[i - 1][j] && grid[i - 1][j] == grid[i][j - 1])
                    a[i][j] = min (a[i - 1][j - 1], min (a[i - 1][j], a[i][j - 1])) + 1;
                else a[i][j] = 1;
            }
}
void find_max (int &maxx) {
    maxx = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            if (maxx < a[i][j])
                maxx = a[i][j];

}
int main()
{
	freopen ("C-large.in", "r", stdin);
	freopen ("C-large.out", "w", stdout);

    sf ("%i\n", &T);
    for (int c = 1; c < T + 1; c++) {
        sf ("%i %i\n", &N, &M);
        char tmp;
        clear();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M/4; j++) {
                sf ("%c", &tmp);
                tmp = hex2dec(tmp);
                for (int k = 3; k >= 0; k--)
                    if (tmp & (1 << k)) grid[i][j*4 + 3 - k] = 1;
            }
            sf ("\n");
        }
        for (int i = 0; i < N; i++) a[i][0] = 1;
        for (int i = 0; i < M; i++) a[0][i] = 1;

        int maxx, maxi, maxj;
        calc_a();
        find_max (maxx);

        int cnt = 0, last = N*M, K;

        while (maxx > 1) {
            vector < pair <int, int> > v;
            K = 0;

            for (int i = 0; i < N; i++)
                for (int j = 0; j < M; j++)
                    if (a[i][j] == maxx && !used[i][j]) {
                        int k;
                        for (k = 0; k < K; k++)
                            if ((v[k].first - maxx + 1 <= i - maxx + 1 && i - maxx + 1 <= v[k].first) || (v[k].first - maxx + 1 <= i && i<= v[k].first))
                                    if ((v[k].second - maxx + 1 <= j - maxx + 1 && j - maxx + 1 <= v[k].second) || (v[k].second - maxx + 1 <= j && j <= v[k].second))
                                        break;
                        if (k == K) v.push_back (make_pair (i, j)), K++;
                    }
            for (int k = 0; k < K; k++) {
                maxi = v[k].first, maxj = v[k].second;
                for (int i = maxi - maxx + 1; i <= maxi; i++)
                    for (int j = maxj - maxx + 1; j <= maxj; j++)
                        a[i][j] = 0, used[i][j] = 1;
            }
            cnt++;
            ans[maxx] = K;
            last -= maxx*maxx*K;

            calc_a();
            find_max (maxx);
        }
        if (last) cnt++, ans[1] = last;
        pf ("Case #%i: %i\n", c, cnt);

        for (int i = max(M, N); i > 0; i--)
            if (ans[i]) pf ("%i %i\n", i, ans[i]);
    }
}
