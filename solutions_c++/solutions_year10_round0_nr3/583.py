#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=1; tt<=ts; ++tt) {

		int r, k, n;
		scanf ("%d%d%d", &r, &k, &n);
		vector<int> a (n);
		for (int i=0; i<n; ++i)
			scanf ("%d", &a[i]);

		vector<int> p (n),
			psum (n);
		for (int i=0, cnt=0, csum=0; i<n; ++i) {
			while (cnt < n && csum + a[(i+cnt)%n] <= k)
				csum += a[(i+cnt++)%n];
			
			p[i] = (i + cnt) % n;
			psum[i] = csum;
			
			csum -= a[i];
			--cnt;
		}

		int cycle_begin,  cycle_sz,  predp_sz;
		long long cycle_sum,  predp_sum;
		vector<int> u (n, -1);
		vector<long long> sum (n);
		long long csum = 0;
		for (int i=0, len=0; ; ++len) {
			if (u[i] != -1) {
				cycle_begin = i;
				cycle_sz = len - u[i];
				predp_sz = u[i];
				cycle_sum = csum - sum[i];
				predp_sum = sum[i];
				break;
			}
			u[i] = len;
			sum[i] = csum;
			csum += psum[i];
			i = p[i];
		}

		long long ans = 0;
		int pos = 0;
		if (predp_sz <= r) {
			ans += predp_sum;
			r -= predp_sz;
			
			int cnt = r / cycle_sz;
			ans += cnt * cycle_sum;
			r -= cnt * cycle_sz;

			pos = cycle_begin;
		}
		for (; r; --r) {
			ans += psum[pos];
			pos = p[pos];
		}

		printf ("Case #%d: %I64d\n", tt, ans);
	}


}

