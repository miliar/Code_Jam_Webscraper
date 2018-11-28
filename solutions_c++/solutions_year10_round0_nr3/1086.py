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

int minx(int n) {
    unsigned long l = -1;
    unsigned long ret = l >> (32-n);
    dbg(ret);
    return ret;
}

int main() {
	string fname = "C-small-attempt0";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int T;

	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) {
		int r, k, n;
        int g[S1];
        
		scanf("%d%d%d", &r, &k, &n);
        for (int i = 0 ; i<n; i++) {
            scanf("%d", &g[i]);
        }
		int s[S1];
        int next[S1];
        LL v[S2];
        memset(s, 0, sizeof(s));
        memset(next, -1, sizeof(next));
        memset(v, 0, sizeof(v));
        int x=0;
        LL l=0;
        LL l1;
        int p;
        int val;
        LL cval;
        int step=0;
        int step1;
        bool round = false;
        while(true) {
            //l+=move(s,g,v,x);
            s[x]++;
            if (s[x] == 2 && round == false) {
                round = true;
                l1=l;
                step1=step;
            } else if (s[x]==3) {
                break;
            }
            p=x;
            val=0;
            while(val+g[p] <= k) {
                val += g[p];
                if(++p>=n) p=0;
                if(p == x) break;
            }
            next[x]=p;
            v[x]=val;
            l+=val;
            x=p;
            step++;
        }
        int roundx=x;
        cval=l-l1;
        int cstep=step-step1;
        l1-=cval;
        step1-=cstep;
        
        LL ret=0;
        
        if(r<step1) {
            ret=0;
            x=0;
            for (int i=0; i<r; i++) {
                ret+=v[x];
                x=next[x];
            }
        } else {
            ret+=l1;
            step = r-step1;
            ret += (step/cstep) *cval;
            int leave=step%cstep;
            x=roundx;
            for (int i=0; i<leave; i++) {
                ret+=v[x];
                x=next[x];
            }
        }

        printf("Case #%d: %lld\n", c, ret);
	}
    
	return 0;
}

