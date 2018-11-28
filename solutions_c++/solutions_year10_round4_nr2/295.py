/* 
 * File:   World_Cup_2010.cpp
 * Author: kimi
 *
 * Created on June 5, 2010, 11:29 PM
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
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

string Filename = "B-large";

const int MAX = 1e9, TWO[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048};
int f[100000][20], cost[100000];

int main() {
    freopen((Filename + ".in").c_str(), "r", stdin);
    freopen((Filename + ".out").c_str(), "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int p;
        scanf("%d", &p);
        int pp = TWO[p];
        Fill(f, 0);
        for (int i = 0; i < pp; i++) {
            int x;
            scanf("%d", &x);
            for (int k = x + 1; k <= p + 1; k++) f[2 * pp - i - 1][k] = MAX;
        }
        for (int i = pp - 1; i >= 1; i--)
            scanf("%d", &cost[i]);
        for (int i = pp - 1; i >= 1; i--) {
            f[i][p + 1] = MAX;
            for (int miss = p; miss >= 0; miss--) {
                f[i][miss] = min(cost[i] + f[2 * i][miss] + f[2 * i + 1][miss], f[2 * i][miss + 1] + f[2 * i + 1][miss + 1]);
                f[i][miss] = min(f[i][miss], f[i][miss + 1]);
            }
        }
        printf("Case #%d: %d\n", t + 1, f[1][0]);
    }
    return (EXIT_SUCCESS);
}
