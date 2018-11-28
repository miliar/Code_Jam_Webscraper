#include <cstdio>
#include <cmath>

using namespace std;
int N;
int maxD, pD, pG;

int multi(int x) {	//input is x%, output of first integer a to satisfy a
	for(int i = 1; i <= 100; i++) {
		if((((x * i) / 100) * 100) == x * i) {
//			printf("multiple of %dpercent is %d\n", x, i);
			return i;
		}
	}
}
void solve(int i) {
	scanf("%d %d %d", &maxD, &pD, &pG);
	int m = multi(pD);
	int m2 = multi(pG);
	if(m > maxD) {
		printf("Case #%d: Broken\n", i);
		return;
	}
	if(pG == 100 && pD != 100) {
		printf("Case #%d: Broken\n", i);
		return;
	}
	if(pG == 0 && pD != 0) {
		printf("Case #%d: Broken\n", i);
		return;
	}
	printf("Case #%d: Possible\n", i);
	return;
}

int main() {

	freopen("small.txt", "r", stdin);
	freopen("smallout.txt", "w", stdout);
	scanf("%d", &N);
	for(int i = 1; i <= N; i++) solve(i);
//
//	freopen("large.txt", "r", stdin);
//	freopen("largeout.txt", "w", stdout);
//	scanf("%d", &N);
//	for(int i = 1; i <= N; i++) solve(i);
	return 0;
}
