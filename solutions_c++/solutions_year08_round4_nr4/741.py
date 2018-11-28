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

#define ALL(c) (c).begin(), (c).end()
#define SIZE(s) int((s).size())
#define FILL0(a) memset(a, 0, sizeof(a))
#define FILL1(a) memset(a, -1, sizeof(a))

int getRes(int k, string s) {
    vector<int> v(k);
    for (int i = 0; i < k; ++i) {
        v[i] = i;
    }

    int res = -1;
    do {
        string ss = s;
        for (int i = 0; i < SIZE(ss); ++i) {
            ss[i] = s[i / k * k + v[i % k]];
        }
        int this_res = 0;
        char prev = 0;
        for (int i = 0; i < SIZE(ss); ++i) {
            if (ss[i] != prev) {
                ++this_res;
                prev = ss[i];
            }
        }
        if (res == -1 || this_res < res)
            res = this_res;
    }
    while (next_permutation(ALL(v)));

    return res;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        int k;
        string s;
        cin >> k >> s;

        int res = getRes(k, s);
        printf("Case #%d: %d\n", i, res);
    }

    return 0;
}
