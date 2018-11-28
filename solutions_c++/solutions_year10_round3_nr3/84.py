#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <queue>
using namespace std;
bool a[512][512];
int mtab[512][512];
char trans[256];
void problem(int id)
{
    int m, n;
    assert(2 == scanf("%d%d", &m, &n));
    for (int i = 0; i < int (m); ++i) {
        char b[513];
        assert(1 == scanf("%s", b));
        for (int jj = 0; jj < int (n / 4); ++jj) {
            for (int o = 0; o < int (4); ++o) {
                int j = jj * 4 + o;
                a[i][j] = (bool) (trans[(int) b[jj]] & (1 << (3 - o)));
            }
        }
    }
    priority_queue < pair < int, pair < int, int > > > q;
    for (int i = int (m) - 1; i >= 0; --i)
        for (int j = int (n) - 1; j >= 0; --j) {
            int &v = mtab[i][j];
            if (i == m - 1 || j == n - 1)
                v = 1;
            else if (a[i][j] == a[i][j + 1] || a[i][j] == a[i + 1][j] ||
             a[i][j] != a[i + 1][j + 1])
                v = 1;
            else
                v =
                 1 + min(min(mtab[i][j + 1], mtab[i + 1][j]),
                 mtab[i + 1][j + 1]);
            q.push(make_pair(v, make_pair(-i, -j)));
        }
    map < int, int >ma;
    while (!q.empty()) {
        int sz = q.top().first;
        int r = -q.top().second.first;
        int c = -q.top().second.second;
        q.pop();
        if (mtab[r][c] == -1)
            continue;
        if (mtab[r][c + sz - 1] == -1 || mtab[r + sz - 1][c] == -1 ||
         mtab[r + sz - 1][c + sz - 1] == -1) {
            q.push(make_pair(sz - 1, make_pair(-r, -c)));
            continue;
        }
        ma[sz]++;
        for (int i = r; i < int (r + sz); ++i)
            for (int j = c; j < int (c + sz); ++j)
                mtab[i][j] = -1;
    }
    printf("Case #%d: %d\n", id + 1, ma.size());
    for (typeof(ma.rbegin())it = ma.rbegin(); it != ma.rend(); it++)
        printf("%d %d\n", it->first, it->second);
}
int main(int argc, char **argv)
{
    for (int i = 0; i < int (16); ++i) {
        char b[2];
        sprintf(b, "%x", i);
        int mask = 0xff ^ (i >= 10 ? 32 : 0);
        trans[(int) b[0] & mask] = i;
    }
    int n;
    assert(1 == scanf("%d", &n));
    int id = 0;
    while (n--) {
        problem(id++);
    }
    return 0;
}
