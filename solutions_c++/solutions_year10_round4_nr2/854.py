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

int N, T, M[1024];

int main()
{
	freopen ("B-small.in", "r", stdin);
	//freopen ("B-large.in", "r", stdin);

	freopen ("B-small.out", "w", stdout);
    //freopen ("B-large.out", "w", stdout);


    sf ("%i", &T);

    for (int c = 1; c < T + 1; c++) {
        sf ("%i", &N);
        for (int i = 0; i < (1 << N); i++) sf ("%i", M + i);

        int x;
        for (int i = N - 1; i >= 0; i--)
            for (int j = 0; j < (1 << i); j++)
                sf ("%i", &x);

        int ans = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < (1 << (N - i - 1)); j++) {
                int b = 1;
                for (int k = (1 << (i + 1))*j; k < (1 << (i + 1))*(j + 1); k++)
                    if (!M[k]) b = 0;

                if (b)
                    for (int k = (1 << (i + 1))*j; k < (1 << (i + 1))*(j + 1); k++) M[k]--;
                else ans++;
            }
        }

        pf ("Case #%d: %d\n", c, ans);
    }



}
