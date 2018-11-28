/*
  ID: nigo1
  LANG: C++
  TASK: candy
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

int N, T;
int a[1000];

int xorr (int mask) {
    int res = 0;
    for (int i = 0; i < N; i++)
        if (mask & (1<<i))
            res ^= a[i];

    return res;
}

int sum (int mask) {
    int res = 0;
    for (int i = 0; i < N; i++)
        if (mask & (1<<i))
            res += a[i];

    return res;
}

int main()
{
	freopen ("candy.in", "r", stdin);
	freopen ("candy2.out", "w", stdout);

    scanf ("%d", &T);
    for (int t = 0; t < T; t++) {
        printf ("Case #%d: ", t + 1);

        scanf ("%d", &N);

        int x = 0;
        long long sum = 0, minn = 1 << 30;

        for (int i = 0; i < N; i++)
            scanf ("%d", a + i),
            x ^= a[i], sum += (long long)a[i],
            minn = min (minn, (long long)a[i]);

        if (x != 0)
            printf ("NO\n");
        else
            printf ("%lld\n", sum - minn);

    }
}
