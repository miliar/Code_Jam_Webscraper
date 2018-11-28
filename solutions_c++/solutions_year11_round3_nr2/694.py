/*
 * File:   Space_Emergency_Small.cpp
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
#define FILENAME "B-small-attempt0"

using namespace std;

const int MAX_N = 2000, MAX_L = 10;
int a[MAX_N];
long long F[MAX_N][MAX_L];

int main() {
    freopen(FILENAME ".in", "r", stdin);
    freopen(FILENAME ".out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int L, N, C;
        long long time;
        scanf("%d", &L);
        cin >> time;
        scanf("%d%d", &N, &C);
        for (int i = 0; i < C; i++) scanf("%d", &a[i]);
        for (int i = C; i < N; i++) a[i] = a[i % C];
        Fill(F, -1);
        F[0][0] = 0;
        for (int i = 1; i <= N; i++)
            for (int j = 0; j <= L; j++) {
                // Don't build one
                F[i][j] = F[i - 1][j] + a[i - 1] * 2;

                // Build one
                if (j) {
                    long long added;
                    if (F[i - 1][j - 1] >= time) added = a[i - 1];
                    else {
                        if (F[i - 1][j - 1] + 2 * a[i - 1] <= time) added = a[i - 1] * 2;
                        else {
                            added = time - F[i - 1][j - 1];
                            added += a[i - 1] - added / 2;
                        }
                    }
                    F[i][j] = min(F[i][j], F[i - 1][j - 1] + added);
                }
            }
        long long result = F[N][0];
        for (int i = 1; i <= L; i++)
            result = min(result, F[N][i]);
        printf("Case #%d: ", t + 1);
        cout << result << endl;
    }

    return 0;
}

