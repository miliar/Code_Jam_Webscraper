#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i,a,b) for(int i=(a); i<(b); ++i)

int main() {
	int T;
	scanf("%d", &T);
	rep(t,0,T) {
		int N;
		scanf("%d", &N);
		int mi = 1<<28, sum = 0, x = 0;
		rep(n,0,N) {
			int C;
			scanf("%d", &C);
			mi = min(mi, C);
			sum += C;
			x ^= C;
		}
		if(x) printf("Case #%d: NO\n", t+1);
		else printf("Case #%d: %d\n", t+1, sum-mi);
	}
	return 0;
}