/*
 * File:   RPI.cpp
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
#define FILENAME "A-large"

using namespace std;

const int MAX_N = 101;
double a[MAX_N][MAX_N], WP[MAX_N], OWP[MAX_N], OOWP[MAX_N];
int main() {
    freopen(FILENAME ".in", "r", stdin);
    freopen(FILENAME ".out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++) {
                char ch;
                while (scanf("%c",&ch), ch != '0' && ch != '1' && ch != '.');
                if (isdigit(ch)) a[i][j] = ch - '0';
                else a[i][j] = -1;
            }
        Fill(WP, 0);
        Fill(OWP, 0);
        Fill(OOWP, 0);
        for (int i = 0; i < N; i++) {
            double win = 0, sum = 0;
            for (int j = 0; j < N; j++)
                if (i != j) {
                    if (a[i][j] >= 0) sum++;
                    if (a[i][j] == 1) win++;
                    if (a[j][i] >= 0) sum++;
                    if (a[j][i] == 0) win++;
                }
            WP[i] = win / sum;
        }
        for (int i = 0; i < N; i++) {
            double win = 0, sum = 0;
            for (int j = 0; j < N; j++)
                if (i != j && (a[i][j] >= 0 || a[j][i] >= 0)) {
                    sum++;
                    double win1 = 0, sum1 = 0;
                    for (int k = 0; k < N; k++)
                        if (k!=i && k!=j) {
                            if (a[k][j] >= 0) sum1++;
                            if (a[k][j] == 0) win1++;
                            if (a[j][k] >= 0) sum1++;
                            if (a[j][k] == 1) win1++;
                        }
                    win += win1 / sum1;
                }
            OWP[i] = win / sum;
        }
        for (int i = 0; i < N; i++) {
            double win = 0, sum = 0;
            for (int j = 0; j < N; j++)
                if (i != j && (a[i][j] >= 0 || a[j][i] >= 0)) {
                    sum++;
                    win += OWP[j];
                }
            OOWP[i] = win / sum;
        }
        printf("Case #%d:\n", t + 1);
        for (int i = 0; i < N; i++)
            printf("%lf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
    }

    return 0;
}

