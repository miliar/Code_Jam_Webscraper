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

const int MAX=100050;
LL x[MAX];
LL y[MAX];
LL cnt[3][3];

LL choose1(LL x) { return x; }
LL choose2(LL x) { return (x*(x-1))/2; }
LL choose3(LL x) { return (x*(x-1)*(x-2))/6; }

int main() {
	int T;
	cin >> T;
	for (int z=1;z<=T;++z) {
		memset(cnt,0,sizeof cnt);
		LL n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		x[0]=x0, y[0]=y0;
		for (LL i=1;i<=n-1;++i) {
			x[i] = (A*x[i-1] + B) % M;
			y[i] = (C*y[i-1] + D) % M;
		}
		for (int i=0;i<n;++i) cnt[x[i]%3][y[i]%3]++;
		LL ans=0;
		for (int i=0;i<9;++i) {
			int i0 = i/3, i1 = i%3;
			for (int j=i;j<9;++j) {
				int j0 = j/3, j1 = j%3;
				for (int k=j;k<9;++k) {
					int k0 = k/3, k1 = k%3;
					if ((((i0 + j0 + k0)%3) == 0) &&
							((((i1 + j1 + k1)%3) == 0))) {
						if (i==j && j==k) {
							ans += choose3(cnt[i0][i1]);
						}
						else if (i==j) {
							ans += choose2(cnt[i0][i1])*choose1(cnt[k0][k1]);
						}
						else if (j==k) {
							ans += choose1(cnt[i0][i1])*choose2(cnt[j0][j1]);
						}
						else {
							ans += cnt[i0][i1]*cnt[j0][j1]*cnt[k0][k1];
						}
					}
				}
			}
		}
		printf("Case #%d: %lld\n", z, ans);
	}
}
