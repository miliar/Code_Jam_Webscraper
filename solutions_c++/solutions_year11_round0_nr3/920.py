#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

int pairChar(char c1, char c2) {
	return (((int)c1)&255) | ((((int)c2)&255)<<8);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; ++t) {
		int N;
		scanf("%d", &N);
		int minC = 0;
		int sum = 0;
		int xSum = 0;
		for(int n=0; n<N; ++n) {
			int C;
			scanf("%d", &C);
			if(n==0 || C<minC) {
				minC = C;
			}
			sum += C;
			xSum ^= C;
		}
		if(xSum==0) {
			printf("Case #%d: %d\n", t + 1, sum - minC);
		}
		else {
			printf("Case #%d: NO\n", t + 1);
		}

	}
	return 0;
}
