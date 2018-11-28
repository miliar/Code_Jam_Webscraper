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
    int t, tCtr, i;
    scanf("%d", &t);

    REP(tCtr, t) {
        int n, low, high;
        scanf("%d %d %d", &n, &low, &high);
        vector<int> v(n);
        REP(i, n)
        scanf("%d", &v[i]);
        int r = 0;

        REP(i, high - low + 1) {
            
                int j;
                r = 0;
                REP(j, n) {

                    if (v[j] % (i + low) == 0 || (i + low) % v[j] == 0) {
                        r++;
                    }
                }

            
            if (r == n) {
                break;
            }
        }
        
        if (r == n)
            printf("Case #%d: %d\n", tCtr + 1, i + low);
        else
            printf("Case #%d: NO\n", tCtr + 1);
    }
    return 0;
}