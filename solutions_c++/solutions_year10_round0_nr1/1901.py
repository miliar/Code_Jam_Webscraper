#include <iostream>
using namespace std;

int TCase, N, K;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; ++Case) {
		scanf("%d%d", &N, &K);
		if ((K+1) % (1 << N) == 0) printf("Case #%d: ON\n", Case);
		else printf("Case #%d: OFF\n", Case);
	}
	return 0;
}
