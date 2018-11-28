#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

#define MAX 200000

using namespace std;

int n = 0;
int all_sum = 0;
int a[MAX] = {0};
int f[MAX] = {0};
int aa[111] = {0};
int bb[111] = {0};
int res[111] = {0};
int cc[111] = {0};

int do_sum(int a, int b) {
	
	memset(aa, 0, 111);
	aa[0] = 0;
	while (a > 0) {
		aa[++aa[0]] = a%2;
		a /= 2;
	}
	
	memset(bb, 0, 111);
	bb[0] = 0;
	while (b > 0) {
		bb[++bb[0]] = b%2;
		b /= 2;
	}

	int ans = 0;
	
	memset(res, 0, 111);
	res[0] = max(aa[0], bb[0]);
	for (int i = 1; i <= res[0]; i++) {
		if (i > aa[0]) aa[i] = 0;
		if (i > bb[0]) bb[i] = 0;
		res[i] = (aa[i] + bb[i]) % 2;
		ans += res[i] * pow(2, (float)(i-1));
	}

	return ans;
}

int do_min(int a, int b) {
	
	memset(aa, 0, 111);
	aa[0] = 0;
	while (a > 0) {
		aa[++aa[0]] = a%2;
		a /= 2;
	}
	
	memset(bb, 0, 111);
	bb[0] = 0;
	while (b > 0) {
		bb[++bb[0]] = b%2;
		b /= 2;
	}

	int ans = 0;
	
	memset(res, 0, 111);
	res[0] = max(aa[0], bb[0]);
	for (int i = 1; i <= res[0]; i++) {
		if (i > aa[0]) aa[i] = 0;
		if (i > bb[0]) bb[i] = 0;
		res[i] = fabs((float)((aa[i] - bb[i]) % 2));
		ans += res[i] * pow(2, (float)(i-1));
	}

	return ans;
}


int rec() {
	int nn = pow(2, (float)n);
	int ans = -1;
	for (int i = 0; i < nn; i++) {
		int q = i;
		memset(cc, 0, 111);
		cc[0] = 0;
		while (q > 0) {
			cc[++cc[0]] = q%2;
			q /= 2;
		}
		int my_sum = 0;
		int you_sum = 0;
		int cur_ans = 0;
		for (int j = 1; j <= n; j++) {
			if (cc[j] == 0) {
				you_sum = do_sum(you_sum, a[j-1]);
			} else {
				my_sum = do_sum(my_sum, a[j-1]);
				cur_ans += a[j-1];
			}
		}
		if (my_sum == you_sum && cur_ans != all_sum) {
			ans = max(ans, cur_ans);
		}
	}
	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int test_count = 0;
    cin >> test_count;

    for (int test_index = 1; test_index <= test_count; test_index++) {
		cin >> n;
		memset(a, 0, MAX);
		int sum = 0;
		all_sum = 0;
		for (int i = 0; i < n; i++) {
			cin >> a[i];
			sum = do_sum(sum, a[i]);
			all_sum += a[i];
		}

		sort(&a[0], &a[n-1]);

		int ans_sum = -1;
		if (n < 16) {
			ans_sum = rec();
		} else {
			memset(f, 0, MAX);
			int max_sum = 0;
			for (int i = 0; i < n; i++) {
				int tmp_max = a[i];
				for (int j = max_sum; j >= 0; j--) {
					if (f[j] != 0) {
						int q = do_sum(j, a[i]);
						f[q] = max(f[q], f[j] + a[i] - ((j > q)?a[i]:0));
						if (f[q] != all_sum) {
							int sec_sum = do_min(sum, q);
							if (sec_sum == q) {
								ans_sum = max(ans_sum, f[q]);
							}
							tmp_max = max(q, tmp_max);
						}
					}
				}
				f[a[i]] = max(f[a[i]], a[i]);
				if (f[a[i]] != all_sum) {
					int sec_sum = do_min(sum, a[i]);
					if (sec_sum == a[i]) {
						ans_sum = max(ans_sum, f[a[i]]);
					}
					tmp_max = max(a[i], tmp_max);
				}
				max_sum = max(max_sum, tmp_max);
			}
		}

        cout << "Case #" << test_index << ": ";
		if (ans_sum == -1)
			cout << "NO";
		else
			cout << ans_sum;
		cout << endl;
    }

	return 0;
}
