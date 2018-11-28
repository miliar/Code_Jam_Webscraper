#include <iostream>
#include <cstdio>
using namespace std;

#define REP(x, n) for(int (x)=0; (x)<(n); (x)++)
#define MAXN 1010

long long G[MAXN];
long long Z[MAXN];
int next[MAXN];

void testcase(int tcase){
    int r, k, n; scanf("%d%d%d", &r, &k, &n);
    REP(i, n) scanf("%lld", &G[i]);
    
    REP(i, n){
        next[i] = -1;
        
        int q = i;
        long long s = 0;
        
        while(true){
            if ( q == n ) q = 0;
            
            if ( s + G[q] > k ) {
                break;
            }
            else {
                s += G[q];
            }
            
            q ++;
            q %= n;
            next[i] = q;
            Z[i] = s;
            
            if ( q == i ) break;
            
        }
    }
    
    int p = 0;
    long long sol = 0;
    while( r-- ){
        sol += Z[p];
        p = next[p];
    }
    printf("Case #%d: %lld\n", tcase, sol);
}

int main(){
    int z; scanf("%d", &z);
    REP(x, z) testcase(x+1);
return 0;
}

