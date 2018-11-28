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
#include <cfloat>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

const int N=1001;
typedef long long LL;

int foo(int *a,int n, int x) {
    for (int i=0; i<n; i++) {
        if(a[i]==x) {
            return i;
        }
    }
    return 0;
}
                
int main() {
	string fname = "A-small-attempt0";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int T;
    
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) {
		int n;
        int a[N];
        int b[N];
        int na[N];
        int nb[N];
        int ra[N];
        int rb[N];
        
        LL rc;
        
		scanf("%d", &n);
        
        for (int i=0; i<n; i++) {
            scanf("%d%d",&a[i], &b[i]);
            na[i]=a[i];
            nb[i]=b[i];
        }
        
        sort(na, na+n);
        sort(nb, nb+n);
        
        rc=0;
        for (int i=0; i<n; i++) {
            ra[i]=foo(na, n, a[i]);
            rb[i]=foo(nb, n, b[i]);
        }
        
        for (int i=0; i<n; i++) {
            rc+=abs(ra[i]-rb[i]);
        }
        rc /= 2;
        
        printf("Case #%d: %lld\n", c, rc);
	}
    
	return 0;
}

