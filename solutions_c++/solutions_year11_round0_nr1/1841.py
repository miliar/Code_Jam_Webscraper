#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x " = " << x << std::endl; }

#define maxn (1 << 10)

char robot[maxn], lett[2] = {'O', 'B'};

int pos[maxn];
int next[2][maxn];

inline int sign(int x) {
    return (x == 0) ? 0 : (x < 0 ? -1 : 1);
}

int main() {
    int t, tc, n;
    for(scanf("%d", &tc), t = 1; t <= tc; ++t) {
        printf("Case #%d:", t);

        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf(" %c %d", robot+i, pos+i);
        next[0][n] = next[1][n] = -1;
        for(int i = n-1; i >= 0; i--)
            for(int j = 0; j < 2; j++)
                next[j][i] = (robot[i] == lett[j]) ? pos[i] : next[j][i+1];
        int ps[2] = {1, 1}, dest[2] = {next[0][0], next[1][0]}, ind;
        int ans = 0;
        for(ind = 0; ind < n; ++ans) {
            int i0 = ind;
            //fprintf(stderr, "[%d, %d] - %d\n", ps[0], ps[1], ind);
            for(int j = 0; j < 2; j++) {
                if(robot[i0] == lett[j] && ps[j] == pos[i0]) 
                    dest[j] = next[j][++ind];
                else
                    ps[j] += sign(dest[j] - ps[j]);
            }
        }

        printf(" %d\n", ans);
    }
    return 0;
}
