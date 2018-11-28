#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef long long ll;

int gs[1010];
int pos[1010];
ll ss[1010];

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		int R, k, n;
		cin >> R >> k >> n;
		printf("Case #%d: ", t + 1);
		for(int i = 0; i < n; ++i) cin >> gs[i];
		set<int> used;
		int p = 0, ind = 0;
		ll f = 0;
		while(used.insert(p).second) {
			ll num = 0;
			int st = p;
			for(; num + gs[p] <= k && (p != st || num == 0); p = (p + 1) % n) {
				num += gs[p];
				f += gs[p];
			}
			pos[st] = ind++;
			ss[ind] = f;
		}
		int loop = ind - pos[p];
		ll res = 0;
		if(R < pos[p]) {
			R = 0;
			res = ss[R];
		}else {
			R -= pos[p];
			res = ss[pos[p]] + R / loop * (f - ss[pos[p]]) + ss[R % loop + pos[p]] - ss[pos[p]];
		}
		printf("%lld\n", res);
	}
	return 0;
}
