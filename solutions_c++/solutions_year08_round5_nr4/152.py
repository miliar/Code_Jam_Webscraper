#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <gmpxx.h> // BigIntegers http://gmplib.org/
using namespace std;

typedef long long lint;

const int INF = 0x3f3f3f3f;

const int N = 101;

int H, W, R;
int a[N][N];

bool b[N][N];

int go(int r, int c)
{
    if (r >= H || r < 0 || c >= W || c < 0) return 0;
    if (r == H-1 && c == W - 1) return 1;
    if (b[r][c]) return 0;
    int &res = a[r][c];
    if (res >= 0) return res;
    res = (go(r + 2, c + 1) + go(r + 1, c + 2)) % 10007;
    return res;
}

int main()
{
    //freopen("D.in", "r", stdin);
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; ++cs)
    {
        memset(a, -1, sizeof(a));
        memset(b, 0, sizeof(b));
        scanf("%d %d %d", &H, &W, &R);
        for (int i = 0; i < R; ++i)
        {
            int r, c;
            scanf("%d %d", &r, &c);
            r--; c--;
            b[r][c] = true;
        }
        int res = go(0, 0);
        printf("Case #%d: %d\n", cs, res);
    }
    return 0;
}
