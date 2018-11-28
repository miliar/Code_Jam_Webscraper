#include <stdio.h>
#include <queue>

using namespace std;

class Build {
	public:
		long long int len, num;
		Build(long long int len, long long int num) : len(len), num(num) {
		}
};

bool operator< (const Build& a, const Build& b) {
	return a.len < b.len;
}

int main() {

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		long long int L, st, N, C;
		scanf("%lld%lld%lld%lld", &L, &st, &N, &C);
		long long int a[1000];
		long long int period = 0;
		for (int i = 0; i < C; i++) {
			scanf("%lld", &a[i]);
			period += a[i];
		}

		priority_queue<Build> builds;

		long long int npd = N / C;
		long long int nph = N % C;

		long long int startpd = (st / 2) / period;
		long long int startph = (st / 2) % period;
		long long int total = 0;
		for (int i = 0; i < C; i++) {
			int num = 0;
			if (total < startph && total + a[i] < startph) {
				num = npd - startpd - 1;
			} else if (total > startph && total + a[i] > startph) {
				num = npd - startpd;
			} else {
				num = npd - startpd - 1;
				builds.push(Build(total + a[i] - startph, 1));
			}

			if (i < nph) {
				num++;
			}

			if (num > 0) {
				builds.push(Build(a[i], num));
			}

			total += a[i];
		}

		long long int time = 2 * npd * period;
		for (int i = 0; i < nph; i++) {
			time += 2 * a[i];
		}

		while (!builds.empty() && L > 0) {
			if (builds.empty()) {
				break;
			}
			Build build = builds.top();
			builds.pop();

			if (build.num <= L) {
				L -= build.num;
				time -= build.num * build.len;
			} else {
				time -= L * build.len;
				break;
			}
		}

		printf("Case #%d: %lld\n", t, time);
	}
}
