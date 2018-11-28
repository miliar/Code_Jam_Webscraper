#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;

#define REP(i, n) for(int i=0; i<n; ++i)
#define ST first
#define ND second
#define PB push_back
#define VAR(v,n) __typeof__(n) v=(n)
#define FE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()

#define NIL -1


PII triplets(int total){
    int k = total / 3;
    int normal = NIL;
    int suprising = NIL;
    for(int a=k-1; a<=k+2; a++)
    for(int b=a; b<=k+2; b++)
    for(int c=b; c<=k+2; c++){
        if ( a < 0 || b < 0 || c < 0 ) continue;
        if ( a > 10 || b > 10 || c > 10 ) continue;
        if ( a + b + c != total ) continue;
        if ( c - a <= 1 ) normal = max(normal, c);
        if ( c - a == 2 ) suprising = max(suprising, c);
    }
    return PII(normal, suprising);
}

#define MAXS 105
int T[MAXS+10];

int solve(){
    int n, s, p;
    scanf("%d%d%d", &n, &s, &p);
    REP(i, MAXS) T[i] = NIL;
    T[0] = 0;
    
    REP(i, n) {
        int a; scanf("%d", &a);
        PII r = triplets(a);
        
        for(int i=MAXS; i>0; i--){
            if ( r.ST >= p && T[i] != NIL ) {
                T[i] = max( T[i], T[i]+1 );
            }
            if ( r.ND >= p && T[i-1] != NIL ) {
                T[i] = max( T[i], T[i-1] + 1 );
            }
            if ( r.ND != -1 && T[i-1] != NIL ) {
                T[i] = max( T[i], T[i-1] );
            }
            
        }
        
        if ( r.ST >= p ) T[0]++;
        
    }
    
    return T[s];
}

int main(){
    int z; scanf("%d", &z);
    REP(i, z) printf("Case #%d: %d\n", i+1, solve());
return 0;
}

