/*
 * File:   Perfect_Harmony.cpp
 * Author: Kimi
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <climits>

#define Fill(A, n) memset(A, n, sizeof(A))
#define pb push_back
#define FILENAME "C-small-attempt0"

using namespace std;

const int MAX_N = 1000;
int a[MAX_N];

bool harmony(int c, int size)
{
    for (int i = 0; i < size; i++)
        if (a[i] % c && c % a[i]) return false;
    return true;
}

int main() {
    freopen(FILENAME ".in", "r", stdin);
    freopen(FILENAME ".out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int N, L, H;
        scanf("%d%d%d", &N, &L, &H);
        for (int i = 0; i < N; i++)
            scanf("%d", &a[i]);
        int best = -1;
        for (int i = L; i <= H; i++)
            if (harmony(i, N)) {
                best = i;
                break;
            }
        if (best < 0) printf("Case #%d: NO\n", t + 1);
        else printf("Case #%d: %d\n", t + 1, best);
    }

    return 0;
}

