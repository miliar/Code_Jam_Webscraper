#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
#include <list>
#include <vector>
#include <cassert>

#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FOREACH(i,x) for (__typeof((x).begin())i=(x).begin(); i!=(x).end(); ++i)
#define S(t,i) scanf("%"#t, &i)
#define SI(i) scanf("%d", &i)
#define LL long long

using namespace std;

int main() {
    
    int t, s, p, ti, n;
    
    SI(t);
    REP(i,t) {
        SI(n);
        SI(s);
        SI(p);
        
        int best=0;
        int normal=3*p-2;
        int surprise=3*p-4;
        REP(ni, n){
            SI(ti);
            if (ti>=normal) {
                ++best;
            } else if (ti>=surprise && s>0 && ti>=2 && ti<=28){
                s--;
                ++best;
            }
        }
        
        printf("Case #%d: %d\n",i+1,best);
    }
    
	return 0;
}
