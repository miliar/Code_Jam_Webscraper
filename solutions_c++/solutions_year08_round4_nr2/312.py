#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long lint;

int mabs(int a)
{
    return a < 0 ? -a : a;
}

int main()
{
    //freopen("B.in", "r", stdin);
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; ++cs)
    {
        int A, X, Y;
        scanf("%d %d %d",&X, &Y, &A);
        //if (X > Y) swap(X, Y);
        char res[32] = "IMPOSSIBLE";
        for (int x2 = 1; x2 <= X; ++x2)
            for (int x3 = 0; x3 <= X; ++x3)
                for (int y2 = 0; y2 <= Y; ++y2)
                {
                    int q = A + x3*y2;
                    if (q % x2 != 0) continue;
                    int y3 = q / x2;
                    if (y3 > Y) continue;
                    assert(mabs(x2 * y3 - x3 * y2) == A);
                    sprintf(res, "0 0 %d %d %d %d", x2, y2, x3, y3);
                }
        printf("Case #%d: %s\n", cs, res);
    }
    return 0;
}
