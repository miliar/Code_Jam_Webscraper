#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#define forn(i, n) for(int i = 0; i<(int) n; i++)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ford(i, n) for(int i = (int)n -1; i>=0; i--)

using namespace std;
int primes[1000004];
int main() {
    int tests;
    int n, m;
    n = 0;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &tests);
   // memset(primes, 0, sizeof(primes));
    forn(i, 1000000)
        primes[i] = 0;
    primes[0] = 1;
    primes[1] = 1;
    forn(i, 1000000)
        if (!primes[i]){
            int j = i+i;
            while (j<1000002){
                primes[j] = 1;
                j+=i;
            }
        }
    vector<int> pr(0);
    forn(i, 1000000)
        if(!primes[i])
            pr.pb(i);
    int d, k; long long p[14];
    int tp[9];
    tp[0] = 1;
    forn(i, 8)
        tp[i+1] = tp[i]*10;
    forn(test, tests){
        printf("Case #%d: ", test+1);
        scanf("%d%d", &d, &k);
        int tmp;
        forn(i, k){
            scanf("%d", &tmp), p[i] = tmp;
        }
        int tnum = 0;
        int tans = -12313;
        if (k == 1){
            printf("I don't know.\n");
            continue;
        }
        forn(i, pr.size()){
            if (tnum>1) break;
            if (pr[i]>=tp[d]) break;
            int okk = 1;
            forn(ii, k)
            if (p[ii]>=pr[i]){
                okk = 0;
                break;
            }
            if (!okk)
                continue;
            forn(a, pr[i]){
                long long tb = (-p[1]+p[0]*a+pr[i])%pr[i];
                long long b = (pr[i]-tb)%pr[i];
                int ok = 1;
                for(int ii = 2; ii<k; ii++)
                    if (p[ii]!=(p[ii-1]*a+b)%pr[i])
                    {
                        ok = 0; break;
                    }
                if (ok&& tans!=(p[k-1]*a+b)%pr[i])
                   tnum ++, tans = (p[k-1]*a+b)%pr[i];//cerr<<pr[i]<<" "<<a<<endl;

            }
        }
        if (tnum == 1)
            printf("%d\n", tans);
        else
            printf("I don't know.\n");
    }

    return 0;
}

