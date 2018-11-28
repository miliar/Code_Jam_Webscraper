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

inline int d(int a, int b){
    if (a > b) return a - b;
    return b - a;
}

int testcase(){
    int opos = 1;
    int otime = 0;
    int bpos = 1;
    int btime = 0;
    
    int n; scanf("%d", &n);
    while(n--){
        char r[5]; int a; scanf("%s %d", r, &a);
        if ( r[0] == 'O' ){
            otime += d( a, opos );
            otime = max(otime, btime) + 1;
            opos = a;
        } else {
            btime += d( a, bpos );
            btime = max(otime, btime) + 1;
            bpos = a;
        }
    }
    
    return max(otime, btime);
}

int main(){
    int z; scanf("%d", &z);
    REP(i, z)
        printf("Case #%d: %d\n", i+1, testcase());
return 0;
}

