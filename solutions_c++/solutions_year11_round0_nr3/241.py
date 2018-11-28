#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;

//BEGIN TEMPLATE HERE
typedef long long int64;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
//END TEMPLATE HERE

const int maxn = 1000 + 5;

int c[maxn];

int main() {
    freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
    //freopen("C-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);
    //freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
    //freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T, N;
    scanf("%d", &T);
    for (int caseId = 1; caseId <= T; caseId ++) {
        printf("Case #%d: ", caseId);
        scanf("%d", &N);
        int S = 0, q = 0;
        for (int i = 0; i < N; i ++) {
            scanf("%d", &c[i]);
            S += c[i];
            q ^= c[i];
        }
        /*
        int ans = -1, cnt = 0;
        for (int i = 1; i < (1 << N) - 1; i ++) {
            int S1 = 0, S2 = 0;
            for (int j = 0; j < N; j ++) {
                if (i & 1 << j) {
                    cnt ^= c[j];
                    S1 += c[j];
                }
            }
            S2 = S - S1;
            if (cnt == (q ^ cnt)) {
                ans = max(ans, max(S2, S1));
            }
        }
        */
        if (q != 0) {
            puts("NO");
        } else {
            sort(c, c + N);
            printf("%d\n", S - c[0]);
        }
    }
    return 0;
}

