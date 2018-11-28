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

int N, T, K;

int main()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);

    sf ("%i", &T);
    for (int i = 0; i < T; i++) {
        sf ("%i%i", &N, &K);
        pf ("Case #%i: ", i + 1);

        if ((((1 << N) - 1) & K) == ((1 << N) - 1)) pf ("ON\n");
        else pf ("OFF\n");
    }
}
