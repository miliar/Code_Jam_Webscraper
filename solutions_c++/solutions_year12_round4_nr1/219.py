#include <cstdio>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <sstream>
using namespace std;

#define MP make_pair
#define SS size()
#define PB push_back
#define ff(a, b) for (int a = 0; a < int(b); ++a)
#define f1(a, b) for (int a = 1; a < int(b); ++a)
#define ii(n)    ff(i, n)
#define FF first
#define CC second
#define BB begin()
#define EE end()
#define all(x)  (x).BB, (x).EE
#define ite(v)   typeof((v).BB)
#define fe(i, v) for(ite(v) i = (v).BB; i != (v).EE; ++i)

#define err(...)    { fprintf(stderr, __VA_ARGS__); fflush(stderr); }

typedef long long LL;
typedef pair<int, int> pii;

#define MOD (LL)


int main() {
    int T;

    cin >> T;

    for (int tcase = 1; tcase <= T; ++tcase) {
        int N;
        cin >> N;
        vector<pii> dls(N);
        ii (N)
            cin >> dls[i].FF >> dls[i].CC;
        int D;
        cin >> D;

        vector<int> furthest(N, 0);
        furthest[0] = dls[0].FF;

        bool can = false;
        ff (iv, N) {
            int have = furthest[iv];
            int limit = have + dls[iv].FF;
            if (limit >= D) {
                can = true;
                break;
            }
            for (int nv = iv+1; nv < N; ++nv) {
                if (dls[nv].FF > limit)
                    break;
                int f = min(dls[nv].CC, dls[nv].FF - dls[iv].FF);
                furthest[nv] = max(furthest[nv], f);
            }
        }

        printf("Case #%d: %s\n", tcase, can ? "YES" : "NO");
    }

    return 0;
}






