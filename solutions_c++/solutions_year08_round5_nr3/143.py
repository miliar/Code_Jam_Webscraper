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

const int N = 10;

int n, m;

char a[N][N + 1];

int  b[N];
int  d[N][1 << N];

int go(int r, int can)
{
    if (r < 0) return 0;
    can &= b[r];
    int &res = d[r][can];
    if (res >= 0) return res;
    res = 0;
    for (int k = 0; k < (1 << n); ++k)
    if ((k & can) == k)
    {
        int cnt = 0;
        bool good = true;
        int nxt = 0;
        for (int i = 0; i < n; ++i)
        if (k & (1 << i))
        {
            cnt++;
            if (i > 0) 
            { 
                if (k & (1 << (i-1))) { good = false; break;}
                nxt |= (1 << (i-1));
            }
            if (i + 1 < n)
            {
                if (k & (1 << (i+1))) { good = false; break;}
                nxt |= (1 << (i+1));
            }
        }
        if (good)
        {
            res= max(res, cnt + go(r-1, ((1 << n)-1) & ~nxt));
        }
    }
    return res;
}

int main()
{
    //freopen("C.in", "r", stdin);
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; ++cs)
    {
        scanf("%d %d", &m, &n);
        for (int i = 0; i < m; ++i)
        {
            scanf(" %s", a[i]);
            int k = 0;
            for (int j = 0; j < n; ++j)
                if (a[i][j] == '.')
                {
                    k |= 1 << j;
                }
            b[i] = k;
        }
        memset(d, -1, sizeof(d));
        int res = go(m - 1, (1 << n) - 1);
        printf("Case #%d: %d\n", cs, res);
    }
    return 0;
}
