/*
 * File:   Square_Tiles.cpp
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

const int MAX_N = 100;
char a[MAX_N][MAX_N];

int main() {
    freopen(FILENAME ".in", "r", stdin);
    freopen(FILENAME ".out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int N, M;
        scanf("%d%d",&N,&M);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                while (scanf("%c",&a[i][j]), a[i][j] != '#' && a[i][j] != '.');
        bool ok = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++)
                if (a[i][j] == '#') {
                    if (i + 1 >= N || j + 1 >= M || a[i][j+1] !='#' || a[i+1][j] !='#' || a[i+1][j+1] !='#') {
                        ok = false;
                        break;
                    }
                    a[i][j] = a[i+1][j+1] ='/';
                    a[i][j+1] = a[i+1][j] = '\\';
                }
            if (!ok) break;
        }
        printf("Case #%d:\n", t + 1);
        if (ok)
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++)
                    printf("%c",a[i][j]);
                printf("\n");
            }
        else printf("Impossible\n");
    }

    return 0;
}

