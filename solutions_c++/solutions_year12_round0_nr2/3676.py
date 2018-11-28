#include <stdio.h>
#include <string.h>

int main(void)
{
	int T_;
	scanf("%d", &T_);
	for (int i_ = 1; i_ <= T_; ++i_) {
		int N, S, p;
		scanf("%d %d %d", &N, &S, &p);
		int s = 0;
		int ans = 0;
		for (int i = 0; i < N; ++i) {
			int t;
			scanf("%d", &t);

			int m = t / 3;
			int r = t - 3*m;
			switch (r) {
			case 0:
				if (m >= p) {
					++ans;
				} else if (m + 1 >= p && s < S && 3 <= t) {
					++ans;
					++s;
				}
				break;
			case 1:
				if (m + 1 >= p) {
					++ans;
				}
				break;
			case 2:
				if (m + 1 >= p) {
					++ans;
				} else if (m + 2 >= p && s < S) {
					++ans;
					++s;
				}
				break;
			}
		}
		printf("Case #%d: %d\n", i_, ans);
	}
	return 0;
}
