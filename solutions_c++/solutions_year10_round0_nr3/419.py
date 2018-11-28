#include <cstdio>

using namespace std;

#define MAX_N 1002

int  g[MAX_N];
long long ride[MAX_N+1];
int ff[MAX_N+1];

void clear(int n) {
	for(int i=0; i<=n; ++i) {
		ride[i] = 0;
		ff[i] = -1;
	}
}

long long tc() {
	int R, k, N;


	scanf("%d %d %d", &R, &k, &N);
	for(int i=0; i<N; ++i)
		scanf("%d", &g[i]);
	clear(N);

	int first = 0;
	long long sum = 0;
	int r;
	ride[0] = 0;
	ff[0] = 0;
	for (r=1; r <= R; ++r) {
		int in = 0;
		for(int i=0; i<N; ++i) {
			if (in+g[first] > k)
				break;

			in += g[first];
			first = (first+1)%N;
		}
		sum += in;
		ride[r] = sum;

		if (ff[first] >= 0)
			break; // cykl
		ff[first] = r;
	}

	if (r>R) {
//		printf("doliczylem\n");
		return sum;
	}
	
	long long c_start = ff[first];
	long long c_len = r - c_start;
	long long c_val = ride[r] - ride[c_start];

//	printf("wyliczam z cyklu - start: %d, len: %d, val: %d\n", 
//			c_start, c_len, c_val);
	sum = 0;
	sum += ride[c_start];
	R -= c_start;

	long long full = R / c_len;
	long long rest = R % c_len;
//	printf("wyliczam z cyklu - full: %d, rest: %d\n", 
//			full, rest);

	sum += full*c_val;
	sum += ride[c_start+rest] - ride[c_start];

	return sum;
}

int main() {
	int T;

	scanf("%d", &T);
	for(int i=1; i<=T; ++i)
		printf("Case #%d: %lld\n", i, tc());

	return 0;
}

