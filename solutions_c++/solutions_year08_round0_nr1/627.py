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

int max_cnt[102][1003];

int getN(int ns, vector<string>& s, int nq, vector<string>& q) {
    FILL0(max_cnt);
    for (int i = nq - 1; i >= 0; --i) {
        for (int j = 0; j < ns; ++j) {
            if (q[i] != s[j]) {
                max_cnt[j][i] = max_cnt[j][i + 1] + 1;
            }
        }
    }

    int res = 0;
    int curq = 0;
    while (curq < nq) {
        int max_n = 0;
        for (int i = 0; i < ns; ++i) {
            max_n = max(max_n, max_cnt[i][curq]);
        }
        curq += max_n;
        ++res;
    }

    return res - 1;
}

int main()
{
    char buffer[200];
    int n;
    fgets(buffer, 200, stdin);
    n = atoi(buffer);
    for (int i = 1; i <= n; ++i) {
        char buffer[200];
        int ns;
        fgets(buffer, 200, stdin);
        ns = atoi(buffer);
        vector<string> s(ns);
        for (int j = 0; j < ns; ++j) {
            fgets(buffer, 200, stdin);
            s[j] = string(buffer);
            if (s[j][SIZE(s[j]) - 1] == '\n')
                s[j].resize(SIZE(s[j]) - 1);
            if (s[j][SIZE(s[j]) - 1] == '\r')
                s[j].resize(SIZE(s[j]) - 1);
        }
        int nq;
        fgets(buffer, 200, stdin);
        nq = atoi(buffer);
        vector<string> q(nq);
        for (int j = 0; j < nq; ++j) {
            fgets(buffer, 200, stdin);
            q[j] = string(buffer);
            if (q[j][SIZE(q[j]) - 1] == '\n')
                q[j].resize(SIZE(q[j]) - 1);
            if (q[j][SIZE(q[j]) - 1] == '\r')
                q[j].resize(SIZE(q[j]) - 1);
        }

        int res = nq <= 1? 0: getN(ns, s, nq, q);
        printf("Case #%d: %d\n", i, res);
    }

    return 0;
}
