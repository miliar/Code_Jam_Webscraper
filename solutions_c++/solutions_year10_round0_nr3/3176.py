#include <stdio.h>
#include <stdlib.h>

#define N 1024

using namespace std;

typedef unsigned long long llu;
llu A[N], S[N];
int n;

llu c(int begin, int end) {
	if (begin < end) {
		return S[end] - S[begin];
	}
	return S[end] + S[n] - S[begin];
}

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		int r, k;
		printf("Case #%d: ", test+1);
		scanf("%d %d %d", &r, &k, &n);
		S[0] = 0;
		for (int i = 0; i < n; i++) {
			scanf("%llu", &A[i]);
			S[i+1] = S[i]+A[i];
		}
		int begin = 0;
		llu output = 0;
		for (int i = 0; i < r; i++) {
			int a = 1, b = n+1, s, end;
			while (b - a > 1) {
				s = (a+b)/2;
				end = (begin+s)%n;
				if (c(begin, end) > k) {
					b = s;
				} else {
					a = s;
				}
			}
			s = (a+b)/2;
			end = (begin+s)%n;
			output+= c(begin, end);
			begin = end;
		}
		printf("%llu\n", output);
	}
	return 0;
}

