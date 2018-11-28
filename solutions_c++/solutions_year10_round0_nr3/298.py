#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		LL R,k,n;
		cin >> R >> k >> n;
		vector<LL> g(n);
		for (int i=0;i<n;++i) cin >> g[i];
		vector<LL> seen(n,-1), cost(n,0), succ(n,-1);
		LL totsum = accumulate(g.begin(),g.end(),0LL);
		if (totsum <= k) {
			succ[0] = 0;
			cost[0] = totsum;
		}
		else {
			int j = 0;
			LL sum = 0;
			for (int i=0;i<n;++i) {
				while (sum + g[j] <= k) {
					sum += g[j];
					j = (j+1)%n;
				}
				succ[i] = j;
				cost[i] = sum;
				sum -= g[i];
			}
		}
		LL ans = 0;
		int at = 0, t = 0;
		while (R > 0 && seen[at] == -1) {
			seen[at] = t;
			ans += cost[at];
			at = succ[at];
			++t;
			--R;
		}
		LL cyclen = t - seen[at], cyccost = 0, numaround = R / cyclen;
		int p = at;
		do {
			cyccost += cost[p];
			p = succ[p];
		} while (p!=at);
		R %= cyclen;
		ans += numaround*cyccost;
		while (R-- > 0) ans += cost[at], at = succ[at];
		printf("Case #%d: %lld\n", z,ans);
	}
}
