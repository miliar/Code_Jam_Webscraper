#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cmath>
#include <complex>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
typedef long long LL;
long long player[10100];
int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int bb = 1;
    while (T--) {
        int N;
        long long L, H;
        scanf("%d%lld%lld", &N, &L, &H);
        for (int i = 0; i < N; ++i) {
            scanf("%lld", player + i);
        }
        long long ans = -1;
        for (long long i = L; i <= H; ++i) {
            bool can = true;;
            for (int j = 0; j < N; ++j) {
                if (player[j] == 0) {
                    continue;
                }
                if (player[j] % i != 0 && i % player[j] != 0) {
                    can = false;
                    break;
                }
            }
            if (can) {
                ans = i;
                break;
            }
        }
        printf("Case #%d: ", bb++);
        if (ans != -1) {
            printf("%lld\n", ans);
        } else {
            puts("NO");
        }
    }
    return 0;
}