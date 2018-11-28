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

int N, T;
bool a[128][128], b[128][128];

int main()
{
	freopen ("C-small.in", "r", stdin);
	//freopen ("C-large.in", "r", stdin);

	freopen ("C-small.out", "w", stdout);
    //freopen ("C-large.out", "w", stdout);

    sf ("%i", &T);
    for (int c = 0; c < T; c++) {
        sf ("%i", &N);
        int x1, y1, x2, y2;
        for (int i = 0; i < N; i++) {
            sf ("%i%i%i%i", &x1, &y1, &x2, &y2);

            for (int x = x1; x <= x2; x++)
                for (int y = y1; y <= y2; y++)
                    a[x][y] = 1;
        }

        int ans = 0;
        while (true) {
            bool B = 0;
            for (int i = 1; i < 128; i++)
                for (int j = 1; j < 128; j++)
                    if (a[i][j]) B = 1;

            if (!B) break;
            ans++;
            memset (b, 0, sizeof(b));

            for (int i = 1; i < 128; i++)
                for (int j = 1; j < 128; j++)
                    if (a[i][j]) {
                        if (a[i - 1][j] || a[i][j - 1])
                            b[i][j] = 1;
                    } else
                        if (a[i - 1][j] && a[i][j - 1])
                            b[i][j] = 1;

            memcpy (a, b, sizeof(a));
        }
        pf ("Case #%d: %d\n", c + 1, ans);
    }


}
