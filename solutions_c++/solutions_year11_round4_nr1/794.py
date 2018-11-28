#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

typedef pair<int, int> pii;
typedef long double ld;

const int N = 2000;
int a[N], b[N], w[N];
pii p[N];
pii p2[N];

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        int L, s, r, rt, n;
        cin >> L >> s >> r >> rt >>  n;

        ld res = 0;
        rep(i, n) {
            scanf("%d %d %d", &a[i], &b[i], &w[i]);
        }

        ld rem = 0;
        int it = 0;

        rep(i, n) p[i] = pii(b[i], i);
        sort(p, p + n);

        rep(j, n + 1) {

            int i = p[j].second;
            int d;

            if(j == 0) d = a[i];
            else if(j == n) d = L - b[p[j - 1].second];
            else d = a[i] - b[p[j - 1].second];

            if(rem < rt) {

                ld nrem = rem + ld(d) / r;
                if(nrem < rt) {
                    res += nrem - rem;
                    rem = nrem;
                }
                else {

                    ld t0 = rt - rem;
                    res += ld((d - t0 * (r)) / (s));
                    res += ld(t0);
                    rem = rt;

                } 

            }
            else {
                res += ld(d) / (s);
            }

        }

        rep(i, n) p[i] = pii(w[i], i);
        sort(p, p + n);

        while(it < n) {

            int i = p[it].second;
            int d = b[i] - a[i];

            if(rem < rt) {

                ld nrem = rem + ld(d) / (r + w[i]);
                if(nrem < rt) {
                    res += nrem - rem;
                    rem = nrem;
                }
                else {

                    ld t0 = rt - rem;
                    res += ld(d - t0 * (r + w[i])) / (s + w[i]);
                    res += ld(t0);
                    rem = rt;

                }

            }
            else {
                res += ld(d) / (s + w[i]);
            }

            it++;
        }


        printf("%.8llf\n", res);

    }
}
