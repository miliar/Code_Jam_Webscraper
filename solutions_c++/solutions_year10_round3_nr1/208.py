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

int N, T, A[1000], B[1000];

int main()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);

    sf ("%i", &T);
    for (int c = 1; c < T + 1; c++) {
        sf ("%i", &N);
        for (int i = 0; i < N; i++)
            sf ("%i%i", A + i, B + i);
        int ans = 0;

        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (A[j] > A[i] && B[j] < B[i]) ans++;

        pf ("Case #%i: %i\n", c, ans);
    }
}
