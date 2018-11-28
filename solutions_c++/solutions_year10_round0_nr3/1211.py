#include <cstdio>
#include <memory>

using namespace std;

const int maxn = 1000;
int r, n, k;
int a[maxn];
int  next[maxn];
long long sum[maxn];
long long res_sum;
void calculate_sums () {
	for (int i = 0; i < n; i++) {
		int j;
		sum[i] = 0;
		for (j = 0; j < n && sum[i] + a[(i+j) % n] <= k; j++) {
			sum[i] += a[(i+j) % n];
		}
		next[i] = (i+j) % n;
	}
	/*
	for (int i = 0; i < n; i++) {
		printf ("%I64d ", sum[i]);
	}
	printf ("\n");
	for (int i = 0; i < n; i++) {
		printf ("%d ", next[i]);
	}
	printf ("\n");
	*/
}

void calculate () {
	static bool was[maxn];
	static int step[maxn];
	static long long cur_sum[maxn];
	long long cycle_val;
	int cycle_length, cycle_start;

	memset (was, 0, sizeof (was));
	int cur = 0;
	for (int i = 0; ; i++, cur = next[cur], r--) {
		if (r == 0) {
			return;
		}
		if (was[cur]) {
			cycle_start = cur;
			cycle_length = i - step[cur];
			cycle_val = res_sum - cur_sum[cur] + sum[cur];
			break;
		}
		was[cur] = true;
		step[cur] = i;
		res_sum += sum[cur];
		cur_sum[cur] = res_sum;
	}
	res_sum += (r / cycle_length) * cycle_val;
	r %= cycle_length;
	cur = cycle_start;
	for (int i = 0; i < r; i++) {
		res_sum += sum[cur];
		cur = next[cur];		
	}
}

int main () {
	freopen ("coaster.in", "rt", stdin);
	freopen ("coaster.out", "wt", stdout);
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf ("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i++) {
			scanf ("%d", a+i);
		}
		res_sum = 0;
		calculate_sums ();
		calculate ();
		printf ("Case #%d: %I64d\n", t, res_sum);
	}
	return 0;
}
