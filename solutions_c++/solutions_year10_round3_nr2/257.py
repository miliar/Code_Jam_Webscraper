#include <iostream>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	int cs = 1;
	while(T--) {
		long long L, P, C;
		scanf("%lld%lld%lld", &L, &P, &C);
		long long count = 0;
		while(C * L < P) {
			long long sq = (int)floor(sqrt((double)L * P));
			if(sq * sq < L * P)
				++sq;
			P = sq;
			++count;
		}
		printf("Case #%d: %lld\n", cs, count);
		++cs;
	}
	return 0;
}
