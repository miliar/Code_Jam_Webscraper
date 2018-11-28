#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

#define MAX 10000000
int knapsack[MAX], lastmax = 0;

int main() {
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt) {
		vector<int> A;
		int N;
		scanf("%d", &N);
		int x = 0;
		for (int i=0; i<N; ++i) {
			int tmp;
			scanf("%d", &tmp);
			A.push_back(tmp);
			x ^= tmp;
		}
		if ( x != 0 ) {
			printf("Case #%d: NO\n", tt);
			continue;
		}

		long long mmm = (1LL << N) / 2;
		int mx = 0;
		for (long long i=1; i<mmm; ++i) {
			int s0 = 0, s1 = 0, sum0 = 0, sum1 = 0;
			for (int t=0; t<N; ++t)
				if ( (1LL << t) & i )
					s1 ^= A[t], sum1 += A[t];
				else
					s0 ^= A[t], sum0 += A[t];
			if ( s1 == s0 )
				mx = max(mx, max(sum1, sum0));
		}
		printf("Case #%d: %d\n", tt, mx);
	}
	return 0;
}
