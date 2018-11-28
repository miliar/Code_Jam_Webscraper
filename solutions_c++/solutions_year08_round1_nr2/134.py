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

typedef pair<int, int> PII;


vector<int> getRes(int N, int M, vector< vector<PII> >& v) {
    vector<int> res(N, 0);
    while (1) {
        int inv_ind = -1;
        for (int i = 0; i < M; ++i) {
            bool this_valid = false;
            for (int j = 0; j < SIZE(v[i]); ++j) {
                if (res[v[i][j].first] == v[i][j].second) {
                    this_valid = true;
                    break;
                }
            }
            if (!this_valid) {
                inv_ind = i;
                break;
            }
        }

        if (inv_ind == -1)
            break;

        int ind1 = -1;
        for (int i = 0; i < SIZE(v[inv_ind]); ++i) {
            if (v[inv_ind][i].second == 1) {
                ind1 = v[inv_ind][i].first;
                break;
            }
        }
        if (ind1 == -1)
            return vector<int>();

        res[ind1] = 1;
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        int N, M;
        cin >> N >> M;
        vector< vector<PII> > v(M);
        for (int j = 0; j < M; ++j) {
            int T;
            cin >> T;
            for (int k = 0; k < T; ++k) {
                PII p;
                cin >> p.first >> p.second;
                --p.first;
                v[j].push_back(p);
            }
        }
        vector<int> res = getRes(N, M, v);
        if (res.empty()) {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
        else {
            printf("Case #%d:", i);
            for (int j = 0; j < N; ++j) {
                printf(" %d", res[j]);
            }
            printf("\n");
        }
    }

    return 0;
}
