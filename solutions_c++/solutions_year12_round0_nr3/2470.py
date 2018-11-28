/*
  ID: nigo1
  LANG: C++
  TASK: C
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

int N, T;

int A, B;

long long used[2000010];
bool u[2000010];

void calc (int x) {
    int P = 1;
    int tmp = x;
    while (tmp) P *= 10, tmp /= 10;

    for (int p1 = 10, p2 = P/10; p1 < P; p1 *= 10, p2 /= 10) {
        tmp = (x % p1)*p2 + x/p1;

        if (tmp <= p1*p2/10 or tmp >= x) continue;

        u[tmp] = 1;
    }

    for (int p1 = 10, p2 = P/10; p1 < P; p1 *= 10, p2 /= 10) {
        tmp = (x % p1)*p2 + x/p1;

        if (tmp <= p1*p2/10 or tmp >= x) continue;

        if (u[tmp]) used[tmp]++;

        u[tmp] = 0;
    }
}

int main()
{
	freopen ("C.in", "r", stdin);
	freopen ("C.out", "w", stdout);

    scanf ("%d", &T);

    for (int test = 1; test <= T; test++) {
        printf ("Case #%d: ", test);

        scanf ("%d%d", &A, &B);

        memset (used, 0, sizeof used);

        for (int x = A; x <= B; x++) {
            calc (x);
        }

        long long res = 0;
        for (int i = A; i <= B; i++)
            res += used[i];

        cout << res << endl;
    }


    return 0;
}
