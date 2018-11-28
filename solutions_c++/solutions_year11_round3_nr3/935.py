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

LL slowsolve(LL N, LL L, LL H, const vector<LL>& f) {
	for (int i=L;i<=H;++i) {
		bool ok = 1;
		for (int j=0;j<N;++j) {
			if (f[j] % i == 0 || i % f[j] == 0);
			else {
				ok = 0;
				break;
			}
		}
		if (ok) return i;
	}
	return -1;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		LL N,L,H;
		cin >> N >> L >> H;
		vector<LL> f(N);
		for (int i=0;i<N;++i) cin >> f[i];
		LL res = slowsolve(N,L,H, f);
		printf("Case #%d: ", z);
		if (res == -1) printf("NO\n");
		else printf("%lld\n", res);
	}
}
