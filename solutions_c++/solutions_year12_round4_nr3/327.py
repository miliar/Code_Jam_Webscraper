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
#define for_size(var, size) \
    for(int var = 0; var < (size); ++var)
#define for_range(var, from, to) \
    for(int var = (from); var < (to); ++var)
#define for_ranges(var, from, to, step) \
    for(int var = (from); var < (to); var += (step))
#define for_each(var, container) \
    for(typeof((container).begin()) var = (container).begin(); var != (container).end(); ++var)

using namespace std;

const int MAX_N = 2000;
int h[MAX_N + 1];
vector<int> g[MAX_N + 1];
int next[MAX_N + 1];

bool dfs(int i, int j, int d, int lj, int ld) {
    h[j] = d;
    int l = i;
    for_each(it, g[j]) {
        int k = *it; 
        if (k < i)
            return false;
        if (k > i) {
            if (lj == j) {
                if (!dfs(l, k, d - 1, j, d))
                    return false;
            }
            else {
                if (!dfs(l, k, d - (j - k) * (ld - d) / (lj - j) - 2, j, d)) 
                    return false;
            }
        }
        l = k;
    }
    return true;
}
int main()
{
   freopen("C-small-attempt1.in", "r", stdin);
   freopen("C.out", "w", stdout);
    
    int testNum;
    cin >> testNum;
    for_size(testIdx, testNum) {
        int n;
        cin >> n;
        for_size(i, n + 1) {
            g[i].clear();
        }
        for_size(i, n - 1) {
            int j;
            cin >> j;
            j--;
            g[j].push_back(i); 
            next[i] = j;
        }
        next[n - 1] = n;
        for_size(i, n) {
            sort(g[i].begin(), g[i].end());
        }
        bool failed = false;
        for (int i = 0; !failed && i < n; i = next[i]) {
            failed |= !dfs(i, next[i], 0, next[i], 0);
        }
        
        printf("Case #%d:", testIdx + 1);
        if (failed) {
            printf(" Impossible");
        } else {
            int minH = 0;
            for_size(i, n) {
                minH = min(minH, h[i]);
            }
            for_size(i, n) {
                printf(" %d", h[i] - minH + 1);
            }
        }
        printf("\n");
    }
    return 0;
}
