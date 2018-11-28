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
        vector<int> highest(N);
        ii ((N-1))
            cin >> highest[i];
        ii (N)
            highest[i]--;

        vector<LL> hs(N);
        hs[N-1] = hs[N-2] = 500000000;
        vector<int> prev_to(N, -1);
        prev_to[N-1] = N-2;
        bool impossible = false;
        for (int i = N-3; i >= 0; --i) {
            int ih = highest[i];
            if (ih == i+1) {
                double upper_m = (hs[highest[ih]] - hs[ih]) /
                                (0.0 + highest[ih] - ih);
                double upper_c = hs[ih] - ih*upper_m;
                double upper_here = i*upper_m + upper_c;
                hs[i] = int(upper_here-100.1);

                prev_to[ih] = i;
            } else if (ih == N-1) {
                double lower_m = (hs[ih] - hs[prev_to[ih]]) /
                                (0.0 + ih - prev_to[ih]);
                double lower_c = hs[ih] - lower_m*ih;
                double lower_here = lower_m*i + lower_c;
                hs[i] = int(lower_here + 200.1);

                prev_to[ih] = i;
            } else {
                if (prev_to[ih] == -1) {
                    impossible = true;
                    break;  //TODO
                }
                double upper_m = (hs[highest[ih]] - hs[ih]) /
                                (0.0 + highest[ih] - ih);
                double upper_c = hs[ih] - ih*upper_m;
                double upper_here = i*upper_m + upper_c;
                
                double lower_m = (hs[ih] - hs[prev_to[ih]]) /
                                (0.0 + ih - prev_to[ih]);
                double lower_c = hs[ih] - lower_m*ih;
                double lower_here = lower_m*i + lower_c;

                int tentative = int(lower_here + 1.1);
                if (tentative > upper_here) {
                    err("ERROR!!!\n");
                    exit(1);
                }
                hs[i] = tentative;

                prev_to[ih] = i;
            }

            for (int p = i+1; p < ih; ++p)
                prev_to[p] = -1;
        }

        printf("Case #%d:", tcase);
        if (impossible)
            printf(" Impossible\n");
        else {
            ii (N)
                printf(" %d", hs[i]);
            printf("\n");
        }

    }

    return 0;
}






