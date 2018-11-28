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

int N, M, T;

string dir[200], path;

int main()
{
	freopen ("A-small.in", "r", stdin);
	freopen ("A-small.out", "w", stdout);

    sf ("%i", &T);
    for (int t= 1; t < T + 1; t++) {
        sf ("%i%i", &N, &M);
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            cin >> dir[i];
            dir[i] += "/";
        }
        dir[N++] = "/";

        for (int i = 0; i < M; i++) {
            cin >> path;
            path += "/";
            int maxx = 0, n = path.size(), m;

            for (int j = 0; j < N; j++) {
                m = dir[j].size();
                if (m < maxx) continue;
                int k = 0;
                for (k = 0; k < min(m, n); k++)
                    if (dir[j][k] != path[k]) break;

                if (k > maxx) maxx = k;
            }

            if (maxx == n) continue;

            for (; maxx < n; maxx++)
                if (path[maxx] == '/') cnt++;

            dir[N++] = path;
        }

        pf ("Case #%i: %i\n", t, cnt);
    }
}
