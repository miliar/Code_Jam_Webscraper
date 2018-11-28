#include <iostream>
using namespace std;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tt, cc, N, K;
    scanf("%d", &tt);
    for(cc = 1; cc <= tt; cc++) {
		scanf("%d%d", &N, &K);
		K &= (1 << N) - 1;
		printf("Case #%d: %s\n", cc, (K == (1 << N) - 1 ? "ON" : "OFF"));
	}
    return 0;
}
