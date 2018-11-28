#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <queue>
using namespace std;
int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		int N;
		scanf("%d", &N);
		int e_sum, sum, min_c;
		e_sum = sum = 0;
		min_c = 9999999;
		for (int n=1; n<=N; n++) {
			int c;
			scanf("%d ", &c);
			e_sum ^= c;
			sum += c;
			if (min_c > c) min_c = c; 
		}
		if (e_sum == 0) {
			printf("%d\n", sum-min_c);
		} else {
			printf("NO\n");
		}
	}
}
