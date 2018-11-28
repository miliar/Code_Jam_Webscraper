#include <cstdio>
#include <algorithm>

using namespace std;

void Solve() {
	int N, S, p;
	scanf("%d %d %d", &N, &S, &p);
	int uEnough = 0, cEnough = 0;
	for (int i = 0; i < N; i++) {
		int sum;
		scanf("%d", &sum);
		if (p > 10) continue;
		int low = sum / 3;
		switch (sum % 3) {
		case 0 : {
			if (low >= p) uEnough++;
			else
				if (low + 1 >= p && low > 0) cEnough++;
				 } break;
		case 1 : {
			if (low + 1 >= p) uEnough++;
				 } break;
		case 2 : {
			if (low + 1 >= p) uEnough++;
			else
				if (low + 2 >= p) cEnough++;
				 } break;
		}
	}
	printf("%d\n", uEnough + min(cEnough, S));
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}