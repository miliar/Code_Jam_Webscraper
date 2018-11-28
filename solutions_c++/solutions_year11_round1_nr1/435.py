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

#define IMP "Broken"
#define POS "Possible"

int main() {
    freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
    //freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
    //freopen("input.txt", "r", stdin);
    int T, pD, pG;
    long long N;
    cin >> T;
    for (int caseId = 1; caseId <= T; caseId ++) {
        printf("Case #%d: ", caseId);
        cin >> N >> pD >> pG;
        if (pD < 100 && pG == 100) {
            puts(IMP);
            continue;
        }
        if (pD > 0 && pG == 0) {
            puts(IMP);
            continue;
        }
        int i, j;
        for (i = 1; i <= 100 && i <= N; i ++) {
            if (i * pD % 100 == 0) {
                break;
            }
        }
        if (i > N) {
            puts(IMP);
            continue;
        }
        int x = pD * i / 100;
        int y = __gcd(pG, 100);
        int t = 100 / y;
        long long lo = 1, hi = 100000000ll * 100000000ll, ans = -1;
        while (lo <= hi) {
            long long mid = (lo + hi) / 2;
            long long tot = t * mid;
            long long WIN = tot / 100 * pG; 
            if (tot - WIN < i - x) {
                lo = mid + 1;
            } else {
                ans = mid;
                hi = mid - 1;
            }
        }
        if (ans == -1) {
            puts(IMP);
        } else {
            puts(POS);
        }
    }
    return 0;
}

