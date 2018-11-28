#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <iostream>

using namespace std;

#ifdef __GNUC__
#define LL long long
#define LL_FMT "%lld"
#define LL_CONST(num) num##ll
#else
#define LL __int64
#define LL_FMT "%I64d"
#define LL_CONST(num) num##i64
#endif

#define ALL(c) (c).begin(), (c).end()
#define SIZE(s) int((s).size())
#define FILL0(a) memset(a, 0, sizeof(a))
#define FILL1(a) memset(a, -1, sizeof(a))


LL getRes(int n, vector<int>& v1, vector<int>& v2) {
    sort(ALL(v1));
    sort(ALL(v2));
    int ind1 = 0;
    int ind2 = n - 1;
    LL res = 0;
    for (; ind1 < n; ++ind1, --ind2) {
        res += (LL)v1[ind1] * v2[ind2];
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        int m;
        cin >> m;
        vector<int> v1(m), v2(m);
        for (int j = 0; j < m; ++j) {
            cin >> v1[j];
        }
        for (int j = 0; j < m; ++j) {
            cin >> v2[j];
        }
        LL res = getRes(m, v1, v2);
        printf("Case #%d: " LL_FMT "\n", i, res);
    }

    return 0;
}
