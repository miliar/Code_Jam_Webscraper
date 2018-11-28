#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
using namespace std;
typedef long long ll;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define FOR(i,k,n) for (int i=(k); i<(int)(n); ++i)
#define FOREQ(i,k,n) for (int i=(k); i<=(int)(n); ++i)
#define DEC(i,k) for (int i=(k); i>=0; --i)

#define SZ(v) (int)((v).size())
#define MEMSET(v,h) memset((v),(h),sizeof(v))
#define FIND(m,w) ((m).find(w)!=(m).end())

ll inv(ll a, ll p) {
    return ( a == 1 ? 1 : (1 - p*inv(p%a, a)) / a + p );
}

ll seq[12];

int main()
{
    vector<ll> primes;
    primes.push_back(2);
    for (ll j=3; j<=1000100; j+=2) {
        REP(k,SZ(primes)) {
            if (primes[k]*primes[k]>j) break;
            if (j%primes[k]==0)
                goto NEXT;
        }
        primes.push_back(j);
NEXT:;
    }
    int T;
    cin>>T;
    while (T--) {
        static int test=1;
        printf("Case #%d: ",test++);
        ll D,K;
        cin>>D>>K;
        REP(j,K) cin>>seq[j];

        if (K==1) {
            puts("I don't know.");
        }
        else if (seq[0]==seq[1]) {
            printf("%d\n", seq[1]);
        }
        else if (K==2) {
            puts("I don't know.");
        }
        else if (K>=3) {
            ll ma=0;
            REP(j,K) ma=max(ma,seq[j]);
            ll upper=1; REP(j,D) upper*=10;

            ll cand=-1;
            for (int j=0; primes[j]<=upper; ++j) {
                if (ma>=primes[j]) continue;
                int P=primes[j];

                ll u=(seq[1]-seq[0]+P)%P; //u!=0
                ll A=(inv(u,P)*((seq[2]-seq[1]+P)%P))%P;
                ll B=(seq[1]-A*seq[0])%P;
                B=(B+P)%P;

                ll s=seq[0];
                FOR(j,1,K) {
                    s=(A*s+B)%P;
                    if (s!=seq[j]) goto NEXT3;
                }
                s=(A*s+B)%P;
                if (cand==-1) cand=s;
                else if (cand!=s) {
                    puts("I don't know.");
                    goto NEXT2;
                }
NEXT3:;
            }
            if (cand==-1) puts("I don't know.");
            else printf("%lld\n", cand);
        }
NEXT2:;
    }
}
