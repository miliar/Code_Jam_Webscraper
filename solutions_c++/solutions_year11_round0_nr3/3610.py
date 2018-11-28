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



void testcase(){
    int n; scanf("%d", &n);
    long long sum = 0;
    long long xsum = 0;
    long long minval = 1000000000;
    
    while(n--){
        int a; scanf("%d", &a);
        long long al = a;
        
        minval = min(minval, al);
        sum += al;
        xsum ^= al;
    }
    
    if ( xsum != 0 ){
        printf("NO\n");
    } else {
        printf("%lld\n", sum - minval);
    }
}

int main(){
    int z; scanf("%d", &z);
    REP(i, z){
        printf("Case #%d: ", i+1);
        testcase();
    }
return 0;
}

