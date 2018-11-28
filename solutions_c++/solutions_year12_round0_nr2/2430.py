/*
  ID: nigo1
  LANG: C++
  TASK: B
*/
#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>

#define TIME pf("%f", (double)clock()/CLOCKS_PER_SEC);

using namespace std;

int T, N, S, p, t[128];

bool used[128];

int main()
{
	freopen ("B.in", "r", stdin);
	freopen ("B.out", "w", stdout);

    scanf ("%d", &T);

    for (int test = 1; test <= T; test++) {
        scanf ("%d", &N);
        scanf ("%d", &S);
        scanf ("%d", &p);

        for (int i = 0; i < N; i++)
            scanf ("%d", t + i);

        sort (t, t + N);

        memset (used, 0, sizeof used);

        int ans = 0;

        for (int i = N - 1; i >= 0; i--) {
            for (int x = 10; x >= p; x--) {
                for (int k1 = 0; k1 < 2 && x - k1 >= 0; k1++)
                    for (int k2 = 0; k2 < 2 && x - k2 >= 0; k2++)
                        if (3*x - k1 - k2 == t[i]) {
                            used[i] = 1;
                            ans++;
                            goto next1;
                        }
            }
            next1:;
        }
        for (int i = N - 1; i >= 0 && S; i--)
            if (!used[i]) {
                for (int x = 10; x >= p; x--) {
                    for (int k1 = 0; k1 <= 2 && x - k1 >= 0; k1++)
                        for (int k2 = 0; k2 <= 2 && x - k2 >= 0; k2++)
                            if (3*x - k1 - k2 == t[i]) {
                                used[i] = 1;
                                ans++;
                                S--;
                                goto next2;
                            }
                }
                next2:;
            }

        printf ("Case #%d: %d\n", test, ans);
    }

    return 0;
}
