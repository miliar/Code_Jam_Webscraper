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
using namespace std;

int N, d[10005], l[10005], D;
map <pair <int, int>, int> dp;


bool solve(int idx, int len) {
    if (dp.find(make_pair(idx, len)) != dp.end())
        return dp[make_pair(idx, len)];
    if (d[idx] + len >= D) {
        return dp[make_pair(idx, len)] = true;
    }    
    if (idx == N - 1) {
        return dp[make_pair(idx, len)] = false;
    }    
    bool res = false;
    for (int i = idx + 1; i < N; ++i) {
        if (d[i] <= d[idx] + len) {
            int next_len = min(d[i] - d[idx], l[i]);
            if (solve(i, next_len)) {
                res = true;
                break;
            }     
        } else {
            break;
        }        
    }    
    return dp[make_pair(idx, len)] = res;
}  

    
int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int caseId = 1; caseId <= T; ++caseId) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) scanf("%d %d", &d[i], &l[i]);
        scanf("%d", &D);
        dp.clear();
        if (solve(0, d[0])) {
            printf("Case #%d: YES\n", caseId);
        } else {
            printf("Case #%d: NO\n", caseId);
        }    
    }    
    //while (1);
    //system("pause");
    return 0;
}    
