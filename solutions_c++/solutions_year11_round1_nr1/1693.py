#include <vector>

#include <string>
#include <cstdio>

#include <algorithm>
#include <utility>
#include <cstring>

#include <map>
#include <set>

#include <cassert>

#include <numeric>
#include <bitset>

#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

#include <cmath>
#include <cstdlib>

#include <list>
#include <deque>
#include <queue>
#include <stack>

#include <functional>
#include <cctype>
#include <ctime>

using namespace std;
typedef long long ll;
typedef pair<int, pair<int, int> > triple;

#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define REP(i,n) for ((i) = 0; int(i) <int(n); ++(i))
#define MP make_pair
#define PB push_back
#define sz size()
#define ln length()
#define fill(f, a) memset(f, a, sizeof(f))
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define for_each(s,container) for (typeof((container).begin()) s = (container).begin(); s != (container).end(); s++)

int main() {
    int t, tCtr;
    scanf("%d", &t);

    REP(tCtr, t) {
        ll N, Pd, Pg;
        scanf("%lld %lld %lld", &N, &Pd, &Pg);
        ll D, G;
        bool flag = false;
        REP(D, N) {
            if(Pd * (D + 1) % 100 == 0) {
                flag = true;
            }
        }
        
        if (flag && (Pg != 0 || Pd == 0) && (Pg != 100 || Pd == 100))
            printf("Case #%d: Possible\n", tCtr + 1);
        else
            printf("Case #%d: Broken\n", tCtr + 1);
    }
    return 0;
}