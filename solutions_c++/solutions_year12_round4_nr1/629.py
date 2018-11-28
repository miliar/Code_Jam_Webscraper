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

#define MAXN 10010

int D[MAXN], L[MAXN];
int low[MAXN];

bool testcase(){
    int n; scanf("%d", &n);
    REP(i, n){
        scanf("%d %d", &D[i], &L[i]);
        low[i] = -1;
    }
    int e; scanf("%d", &e);
    low[0] = D[0];
    REP(i, n){
        if ( low[i] > 0 ){
            for(int j=i+1; j<n && D[i] + low[i] >= D[j]; j++){
                low[j] = max( low[j], min(L[j], D[j] - D[i]) );
            }
        }
    }
    REP(i, n){
        if ( D[i] + low[i] >= e  ) return true;
    }
    return false;
}

int main(){
int z; scanf("%d", &z);
for(int i=1; i<=z; i++) {
    printf("Case #%d: %s\n", i, testcase() ? "YES" : "NO");
    
}
return 0;
}

