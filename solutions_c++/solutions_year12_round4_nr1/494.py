/*
  ID: nigo1
  LANG: C++
  TASK: A
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

#define TIME pf("%f", (double)clock()/CLOCKS_PER_SEC);


using namespace std;

int N, T, D;
int d[10010];
int l[10010];

int b[10010];


int main()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);

    scanf ("%d", &T);

    for (int test = 1; test <= T; test++) {
        printf ("Case #%d: ", test);

        memset (b, 0, sizeof b);

        scanf ("%d", &N);
        for (int i = 0; i < N; i++)
            scanf ("%d%d", d + i, l + i);
        scanf ("%d", &D);

        b[0] = d[0];

        bool ans = 0;
        int j = 0;
        for (int i = 0; i < N; i++) {
            if (!b[i]) break;
            for (j = min (i + 1, j); j < N; j++)
                if (d[j] <= d[i] + b[i]) {
                    b[j] = max (b[j], min (d[j] - d[i], l[j]));
                } else break;

            if (d[i] + b[i] >= D) {
                ans = 1;
                break;
            }
        }
        printf (ans ? "YES\n" : "NO\n");
    }
}
