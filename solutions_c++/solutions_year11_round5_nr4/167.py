#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

int main() {
    freopen("D-small.in", "r", stdin); freopen("D-small.out", "w", stdout);
//    freopen("D-large.in", "r", stdin); freopen("D-large.out", "w", stdout);
    int tests; scanf("%d", &tests);
    for (int testId = 1; testId <= tests; ++testId) {
        printf("Case #%d: ", testId);
        string str;
        cin >> str;
        int cnt = 0;
        for (int i = 0; i < str.size(); ++i)
            if (str[i] == '?')
                ++cnt;
        int m;
        for (m = 0; m < 1 << cnt; ++m) {
            long long x = 0;
            int cur = 0;
            for (int j = 0; j < str.size(); ++j) {
                x *= 2LL;
                if (str[j] == '?') {
                    x += ((m >> cur) & 1);
                    ++cur;
                } else x += str[j] - '0';
            }
            long long tmp = (long long)sqrt(x);
            if (tmp * tmp == x) {
                break;
            }
        }
        int cur = 0;
        for (int j = 0; j < str.size(); ++j)
            if (str[j] == '?') {
                printf("%d", (m >> cur) & 1);
                ++cur;
            } else printf("%c", str[j]);
        printf("\n");
    }
    return 0;
}
