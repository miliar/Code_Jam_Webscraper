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
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;


int main()
{
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        int n, L;
        scanf("%d", &n);
        vector<int> pos(n), len(n);
        for (int i = 0; i < n; i++)
            scanf("%d%d", &pos[i], &len[i]);
        scanf("%d", &L);
        vector<int> opt(n);
        for (int i = n - 1; i >= 0; i--) {
            opt[i] = L - pos[i];
            for (int j = i + 1; j < n; j++) {
                if (min(pos[j] - pos[i], len[j]) >= opt[j])
                    opt[i] = min(opt[i], pos[j] - pos[i]);
            }
        }
        printf("Case #%d: %s\n", ++cas, opt[0] <= pos[0] ? "YES" : "NO");
    }
}
