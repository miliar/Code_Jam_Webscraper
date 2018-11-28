#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>

using namespace std;

#include <ext/numeric>
#include <ext/functional>
using namespace __gnu_cxx;

int R, C, D;

long long d[512][512];

void process(int testcase, bool solvecase) {
    if (!scanf("%d %d %d ", &R, &C, &D)) exit(1);
    for(int i = 0; i < R; ++i) {
        char s[512];
        if (!fgets(s, 512, stdin)) exit(1);
        for (int j = 0; j < C; ++j)
            d[1+i][1+j] = D + s[j]-'0';
    }
    if (solvecase) {
        int res = 0;
        for (int k = 3; k <= R && k <= C; k += 2) {
            for (int i = 1; i + k <= R + 1 && res < k; ++i)
                for (int j = 1; j + k <= C + 1; ++j) {
                    int p = (k >> 1);
                    int ci = i + p;
                    int cj = j + p;
                    long long totx = 0;
                    long long toty = 0;
                    for (int x = -p; x <= p; ++x)
                        for (int y = -p; y <= p; ++y) 
                        {
                            if (x == -p && y == -p) continue;
                            if (x == +p && y == -p) continue;
                            if (x == +p && y == +p) continue;
                            if (x == -p && y == +p) continue;
                            totx += (x + 0.0) * d[ci+x][cj+y];
                            toty += (y + 0.0) * d[ci+x][cj+y];
                        }
                    if (totx == 0 && toty == 0) res = k;
                }
        }

        for (int k = 4; k <= R && k <= C; k += 2) {
            for (int i = 1; i + k <= R + 1 && res < k; ++i)
                for (int j = 1; j + k <= C + 1; ++j) {
                    int p = k >> 1;
                    int ci = i + p;
                    int cj = j + p;
                    long long totx = 0;
                    long long toty = 0;
                    for (int x = -p; x < p; ++x)
                        for (int y = -p; y < p; ++y) 
                        {
                            if (x == -p && y == -p) continue;
                            if (x+1 == +p && y == -p) continue;
                            if (x+1 == +p && y+1 == +p) continue;
                            if (x == -p && y+1 == +p) continue;
                            totx += (2*x+1) * d[ci+x][cj+y];
                            toty += (2*y+1) * d[ci+x][cj+y];
                        }
                    if (totx == 0 && toty == 0) res = k;
                }
        }

        cout << "Case #" << testcase << ": ";
        if (res < 3) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
}

void test() {

}

#ifndef EXTERNAL_MAIN
int main() {
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; ++i)
        process(i, true);
    return 0;
}
#endif