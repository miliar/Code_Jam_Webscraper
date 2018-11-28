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

bool pr[1000001];
long long N;

int main() {
    freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
    //freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
    memset(pr, true, sizeof pr);
    for (int i = 2; i * i <= 1000000; ++i) {
        if (pr[i]) {
            for (int j = i * i; j <= 1000000; j += i) {
                pr[j] = 0;
            }
        }
    }
    int T;
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d: ", caseId);
        cin >> N;
        long long ans = 0;
        for (int i = 2; (long long)i * i <= N; ++i) {
            if (pr[i]) {
                long long t, x;
                for (t = 0, x = N; x >= i; x /= i) ++t;
                ans += t - 1; 
            }
        }
        if (N > 1) ans++;
        printf("%I64d\n", ans);
    }
    return 0;
}

