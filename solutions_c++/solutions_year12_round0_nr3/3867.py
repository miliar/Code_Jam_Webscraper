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

const int RANGE = 2000000;
bool flag[RANGE + 1];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    
    char buf[30];
    int testNum;
    cin >> testNum;
    for_size(testIdx, testNum) {
        int a, b;
        cin >> a >> b;
        fill(flag + a, flag + b + 1, false);
        int sum = 0;
        for_range(i, a, b + 1) {
            if (flag[i])
                continue;
            sprintf(buf, "%d", i);
            int l = strlen(buf);
            int cnt = 0;
            for_size(j, l) {
                rotate(buf, buf + 1, buf + l);
                int gen = atoi(buf);
                if (a <= gen && gen <= b && !flag[gen]) {
                    cnt++;
                    flag[gen] = true;
                }
            }
            sum += cnt * (cnt - 1) / 2;
        }
        printf("Case #%d: %d\n", testIdx + 1, sum);
    }
    return 0;
}
