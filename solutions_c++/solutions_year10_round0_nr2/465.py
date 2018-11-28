#include <cstdlib>
#include <cstring>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <climits>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

const int S1=1001;
const int S2=3001;
typedef long long LL;

LL gcd(LL x, LL y) {
    if (y==0) return x;
    return gcd(y, x%y);
}

int comp(const void* a, const void* b) {
    LL l = *((const LL*)a) - *((const LL*)b);
    if (l>0) {
        return 1;
    } else if (l==0){
        return 0;
    }else {
        return -1;
    }
}

int main() {
	string fname = "B-small-attempt2";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int T;
    
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) {
		int n;
        LL t[S1];
        
		scanf("%d", &n);
        for (int i = 0 ; i<n; i++) {
            scanf("%lld", &t[i]);
        }
        qsort(t, n, sizeof(LL), comp);
        LL mid[S1];
        for (int i=0; i<n-1; i++) {
            mid[i] = t[i+1]-t[i];
        }
        LL g=mid[0];
        for (int i=1; i<n-1; i++) {
            g=gcd(g,mid[i]);
        }
        LL ret = g - (t[0] % g);
        ret = ret % g;
        printf("Case #%d: %lld\n", c, ret);
	}
    
	return 0;
}

