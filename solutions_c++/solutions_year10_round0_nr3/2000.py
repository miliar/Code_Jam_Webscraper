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

typedef long long unsigned llu;

int N, R, K, T, d[10000];
llu s[10000], g[10000];

int main()
{
	freopen ("C-large.in", "r", stdin);
	freopen ("C-large.out", "w", stdout);

    sf ("%i", &T);
    for (int t = 0; t < T; t++) {
        sf ("%i%i%i", &R, &K, &N);
        for (int i = 0; i < N; i++) sf ("%i", g + i);
        pf ("Case #%i: ", t + 1);

        int r = 1;
        llu sum = g[0], res = 0;
        if (g[0] > K) pf ("0\n");
        else {
            for (; sum + g[r] <= K && r < N; r++) sum += g[r];
            d[0] = r%N;
            s[0] = sum;

            for (int i = 1; i < N; i++) {
                sum -= g[i - 1];
                s[i] = 0;
                if (r == i)
                    if (sum + g[r] > K) goto next;
                    else sum += g[r++], r %= N;

                for (; sum + g[r] <= K && r != i; r++, r %= N) sum += g[r];

                s[i] = sum;
                next:;
                d[i] = r;
            }
            int iter = 0;
            for (int i = 0; i < R; i++) {
                res += s[iter];
                iter = d[iter];
            }
            pf ("%llu\n", res);
        }
    }


}
