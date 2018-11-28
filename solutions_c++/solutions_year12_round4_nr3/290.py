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

#define MAXN 2010

int x[MAXN];
int n;
int A[MAXN];

int offset = 12;

bool possible(){
    x[n-1] = n-1;
    REP(i, n) REP(j, n) if ( i < j ) {
        if ( x[i] <= j ) continue;
        if ( x[j] > x[i] ) return false;
    }
    return true;
}

void testcase(){
    scanf("%d", &n);
    REP(i, n-1) {
        scanf("%d", &x[i]);
        x[i]--;
    }
    if ( ! possible() ){
        printf(" Impossible\n"); return;
    }
    A[n-1] = A[n] = 1000000000 - 10;
    x[n-1] = n;
    
    for(int i=n-2; i>=0; i--){
        int a = x[i];
        int b = x[a];
        long double dy = A[b] - A[a];
        long double dx = b - a;
        long double sx = a - i;
        long double sy = (dy * sx) / dx;
        A[i] = A[a] - sy - offset;
        //cout << "licze " << i << ' ' << a << ' ' << b << " sy " << sy << endl;  
    }
    REP(i, n){
        printf(" %d", A[i]);
    }
    printf("\n");
}

int main(){
int z; scanf("%d", &z);
for(int i=1; i<=z; i++) {
    printf("Case #%d:", i);
    testcase();    
}
return 0;
}

