/*
  ID: nigo1
  LANG: C++
  TASK: C
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
long long L, H;

long long a[100];

int main()
{
	freopen ("C.in", "r", stdin);
	freopen ("C.out", "w", stdout);

    scanf ("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf ("Case #%d: ", t);

        scanf ("%d%d%d", &N, &L, &H);
        for (int i = 0; i < N; i++)
            scanf ("%d", a + i);

        sort (a, a + N);

        for (int i = L; i <= H; i++) {
            int j;
            for (j = 0; j < N; j++) {
                if (a[j] < i and i%a[j] == 0) continue;
                if (a[j] >= i and a[j]%i == 0) continue;

                break;
            }

            if (j == N) {
                printf ("%d\n", i);
                break;
            }
            if (i == H) {
                printf ("NO\n");
            }
        }
    }
}
