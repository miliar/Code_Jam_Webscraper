#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <ctime>
#define MAXN
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-9;
typedef long long LL;
typedef pair<int, int> pii;

set<pii> rem;

void solve(int v, int a, int b) {
	char buf[10];
	sprintf(buf, "%d", v);
	int len = strlen(buf);

	int mod = 1;
	int mul = 1;
	for(int i=0; i<len; ++i) {
		mul *= 10;
	}
	for(int i=1; i<len; ++i) {
		mod *= 10;
		mul /= 10;
		int x = v%mod;
		int y = v/mod;
		int t = x*mul + y;
		if(a<=t && t<=b) {
			if(t > v) {
				rem.insert(make_pair(v, t));
			} else if(v < t) {
				rem.insert(make_pair(t, v));
			}
		}
	}
}

int main() {
#ifndef ONLINE_JUDGE
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
#endif

    int dataset;
    scanf("%d", &dataset);
    for(int cas=1; cas<=dataset; ++cas) {
    	int a, b;
    	scanf("%d %d", &a, &b);
    	rem.clear();
    	for(int i=a; i<=b; ++i) {
    		solve(i, a, b);
    	}
    	printf("Case #%d: %d\n", cas, rem.size());
    }

    return 0;
}
