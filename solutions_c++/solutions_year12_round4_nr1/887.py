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
#include <iterator>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <hash_set>
#define for_size(var, size) \
    for(int var = 0; var < (size); ++var)
#define for_range(var, from, to) \
    for(int var = (from); var < (to); ++var)
#define for_ranges(var, from, to, step) \
    for(int var = (from); var < (to); var += (step))
#define for_each(var, container) \
    for(typeof((container).begin()) var = (container).begin(); var != (container).end(); ++var)

using namespace std;
using namespace __gnu_cxx;

typedef pair<int, int> PII;

const int MAX_N = 10000;
int d[MAX_N + 2];
int l[MAX_N + 2];
const int INF = 2000000000;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int testNum;
    cin >> testNum;
    for_size(testIdx, testNum) {
        int n;
        int D;
        d[0] = 0;
        l[0] = INF;
        cin >> n;
        for_range(i, 1, n + 1) {
            cin >> d[i] >> l[i];
        }
        cin >> D;
        
        queue<PII> q;
        q.push(make_pair(0, 1));
        hash_set<int> h;
        h.insert(1);
        bool success = false;
        while (!q.empty()) {
            int i = q.front().first;
            int j = q.front().second;
            if (min(l[j], d[j] - d[i]) >= D - d[j]) {
                success = true;
                break;
            }
            q.pop();
            for_range(k, j + 1, n + 1) {
                if (min(l[j], d[j] - d[i]) < d[k] - d[j])
                    break;
                if (h.find(j * (n + 2) + k) == h.end()) {
                    q.push(make_pair(j, k));
                    h.insert(j * (n + 2) + k);
                }
            }
        }
         
        printf("Case #%d: %s\n", testIdx + 1, success ? "YES" : "NO" );
    }

    return 0;
}
