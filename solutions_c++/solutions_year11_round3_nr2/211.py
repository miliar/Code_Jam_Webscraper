/*
  ID: nigo1
  LANG: C++
  TASK: B
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

int N, T, C, L;

long long t;

long long a[1000009];

long long dist[1000009];

long long d[1000009];

vector < long long > v;

int main()
{
	freopen ("B.in", "r", stdin);
	freopen ("B.out", "w", stdout);

    scanf ("%d", &T);
    for (int test = 1; test <= T; test++) {
        printf ("Case #%d: ", test);
        v.clear();

        scanf ("%d%lld%d%d", &L, &t, &N, &C);
        for (int i = 0; i < C; i++)
            scanf ("%d", a + i);

        for (int i = 0; i < C; i++)
            for (int k = 0; k*C + i < N; k++)
                dist[k*C + i + 1] = a[i];

       // for (int i = 1; i <= N; i++)
       //     printf ("Dist (%d -> %d) = %d\n", i - 1, i, dist[i]);

        for (int i = 1; i <= N; i++)
            d[i] = d[i - 1] + dist[i];

        int start;
        for (start = 0; start <= N; start++)
            if (d[start]*2ll >= t) break;

        if (start == N + 1) {
            printf ("%lld\n", d[N]*2ll);
        } else {
            //printf ("Starting star - %d\n", start - 1);

            v.push_back (d[start]*2ll - t);
            for (int i = start + 1; i <= N; i++)
                v.push_back (dist[i]*2ll);

            sort (v.begin(), v.end());

           // printf ("v:\n");
           // for (int i = 0; i < v.size(); i++)
          //      printf ("v[%d] = %lld\n", i, v[i]);

            int size = v.size();

            long long ans = 0;

            for (int k = 0; k < size - L; k++)
                ans += v[k];

            for (int k = max (size - L, 0); k < size; k++)
                ans += v[k]/2ll;

            printf ("%lld\n", ans + t);
        }
    }
}
