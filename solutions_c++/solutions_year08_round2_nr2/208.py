#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;

typedef long long ll;
typedef unsigned int uint;

#define FOR(I,A,B) for(uint I=(A);I<=(B);I++)
#define REP(I,N) for(uint I=0;I<(N);I++)
#define VAR(V,I) typeof(I) V=(I)
#define FOREACH(I,C) for(VAR(I,(C).begin());I != (C).end(); I++)

#define all(X) (X).begin(),(X).end()
#define pb push_back
#define mp make_pair
#define fi first
#define se second

#define INTPINF  2147483647
#define INTNINF  2147483648
#define UINTINF  4294967295
#define LLPINF   9223372036854775807
#define LLNINF   9223372036854775808
#define ULLINF   18446744073709551615

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

int main() {
    uint tests;
    scanf("%d", &tests);
    
    uint sets[100008];
    bool v[100008];
    
    for (uint t = 1; t <= tests; t++) {
        ll A, B, P;
        scanf("%lld %lld %lld", &A, &B, &P);
        
        REP(i, B-A+1) {
            sets[i] = i;
        }
        memset(v, false, sizeof(bool)*100008);
        
        FOR(p, P, B) {
            bool prime = true;
            FOR(d, 2, p-1) {
                if (p % d == 0) prime = false;
            }
            
            if (!prime) continue;
            
            FOR(a, A, B) {
                if (a % p != 0) continue;
                FOR(b, a+1, B) {
                    if (b % p != 0) continue;
                    
                    uint newset = min(sets[a-A], sets[b-A]);
                    uint chdset = max(sets[a-A], sets[b-A]);
                    if (newset == chdset) continue;
                    
                    REP(i, B-A+1) {
                        if (sets[i] == chdset) sets[i] = newset;
                    }
                }
            }
        }
        
        uint count = 0;
        REP(i, B-A+1) {
            if (!v[sets[i]]) {
                v[sets[i]] = true;
                count++;
            }
        }
        
        printf("Case #%d: %d\n", t, count);
    }

    return 0;
}

