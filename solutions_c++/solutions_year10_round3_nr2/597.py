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

int foo(int a, int b, int base) {
    int x=a;
    int count=0;
    while (x<b) {
        x*=base;
        count++;
    }
    return count;
}
                
int main() {
	string fname = "B-small-attempt2";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int T;
    
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) {
		int l,p,cc;
        
		scanf("%d%d%d", &l,&p,&cc);
        
        int z=foo(l,p,cc);
        LL rc=foo(1,z,2);
        
        printf("Case #%d: %lld\n", c, rc);
	}
    
	return 0;
}

