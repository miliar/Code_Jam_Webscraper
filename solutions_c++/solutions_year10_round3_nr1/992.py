//compiled in vc
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
#include <string>
#include <complex>
/* C++ */
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>

#define MAXN 1000

using namespace std;

int pwin[MAXN][2];

int main() {
    int t, n;

    scanf("%d", &t);

    for(int kase = 1; kase <= t; kase++) {
        int ret = 0;

        scanf("%d", &n);

        for(int i = 0; i < n; i++)
            scanf("%d%d", &pwin[i][0], &pwin[i][1]);

        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                //Case 1:
                if(i != j && pwin[i][0] > pwin[j][0] && pwin[i][1] < pwin[j][1])
                    ret++;
                //Case 2:
                else if(i != j && pwin[i][0] < pwin[j][0] && pwin[i][1] > pwin[j][1])
                    ret++;
            }
        }

        printf("Case #%d: %d\n", kase, ret);
    }
    return 0;
}
