#include <cstdio>
#include <algorithm>

int T, N, Pd, Pg;

int main() {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("1-small.out", "w", stdout);
	scanf("%d", &T);
	for(int cc=1; cc<=T; cc++) {
		bool can = true;
		scanf("%I64d%d%d", &N, &Pd, &Pg);
		int tdwin=Pd, tdply=100, win=0, ply=0;
		tdwin /= std::__gcd(Pd, 100);
		tdply /= std::__gcd(Pd, 100);
		if(tdply > N) can = false;
		if(Pg == 100 && Pd != 100) can = false;
		if(Pg == 0 && Pd != 0) can = false;
		printf("Case #%d: %s\n", cc, can?"Possible":"Broken");
	}
}
