#include <cstdio>
FILE *in, *out;

//R - runs, N - groups, k - max load
const int MAX_N = 2005;
int T, R, N, k;


long long int sumar[MAX_N];
int groups[MAX_N];

long long int sum(int a, int b) {
	return sumar[a+b]-sumar[a];
}

int bsearch(int from, int start, int size) {
	long long int mid = sum(from, (start-from)+size/2);
	if (size == 1) return start - ((mid+groups[start]) > k ? 1 : 0);
	if (mid == k) return start+size/2-1;
	else if (mid > k)
		return bsearch(from, start, size/2);
	else
		return bsearch(from, start+size/2, size/2+size%2);

}


int main() {
	in = fopen("C-large.in", "r"); out = fopen("dashboard.out", "w");
	fscanf(in, "%d", &T);

	for (int i = 1; i <= T; ++i) {
		fscanf(in, "%d %d %d", &R, &k, &N);
		for (int n = 0; n < N; ++n) {
			fscanf(in, "%d", &groups[n]);
			groups[n+N] = groups[n];
		}
		for (int n = 1; n <= N*2; ++n)
			sumar[n] = sumar[n-1]+groups[n-1];

		int index = 0;
		long long money = 0;
		for (int r = 0; r < R; ++r) {
			int next = bsearch(index, index, N)+1;
			money += sum(index, (next-index));
			index = next%N;
		}
		fprintf(out, "Case #%d: %lld\n", i, money);
	}
}
