#include <iostream>
#include <cstdio>
using namespace std;

#define REP(x, n) for(int (x)=0; (x)<(n); ++(x))

#define MAXN 10000

int M[MAXN];

int solve(int a, int b){
    if (a >= b) return 0;
    bool ok = true;
    for(int i=a; i<b; ++i) if ( M[i] > 0 ) ok = false;
    if ( ok ) return 0;
    
    for(int i=a; i<b; ++i) M[i] --;
    return solve( a, (a + b) / 2 ) + solve( (a + b) / 2, b ) + 1;
}

int testcase(){
    int p; scanf("%d", &p);
    int n = (1 << p);
    
 //   cerr << "n " << n << endl;
    
    REP( i, n ) scanf("%d", &M[i]);
    REP(i, n){
        M[i] = p - M[i];
    }
    
    int a;
    REP(i, n-1) {scanf("%d", &a);
   // cerr  << "wywalam " << a << endl;
    }
    return solve( 0, n );
}

int main(){
    int z; scanf("%d", &z);
    REP(i, z){
        cerr << "case " << i+1 << "/" << z << endl;
        printf("Case #%d: %d\n", i+1, testcase());
    }
}

