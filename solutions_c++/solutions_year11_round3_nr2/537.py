
#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>

using namespace std;

typedef long long Int;
typedef long double real;
Int l, t, n, c, a[1024];
int has_booster[1024];
real result;

#define D if(0)

void work(int left, int pos) {
	if (left == 0 || pos >= n) {
		// calc
		if (left != 0) return;
		real time = 0;
		for (int i = 0; i < n; i++) {
			D printf("%s", has_booster[i] ? "#" : ".");
			if (has_booster[i]) {
				// check t
				if (t <= time) {
					// full range boost
					time += a[i % c];
				} else if (t <= time + a[i % c] * 2) {
					// half range boost
					real x = (t - time);
					time += x + (a[i % c] - 0.5 * x);
				} else {
					// no boost
					time += a[i % c] * 2;
				}
			} else {
				time += a[i % c] * 2;
			}
			// D printf(" t:%.1Lf ", time);
		}
		D printf("  time = %.2Lf\n", time);
		if (time < result || result < 0) result = time;
	} else {
		if (left > 0) {
			has_booster[pos] = 1;
			work (left - 1, pos + 1);
			has_booster[pos] = 0;
		}
		work (left, pos + 1);
	}
}

int main(int argc, char const* argv[])
{
	int case_count;
	scanf("%d", &case_count);
	for (int case_index = 0; case_index < case_count; case_index++) {
		printf("Case #%d: ", case_index + 1);
		scanf("%lld%lld%lld%lld", &l, &t, &n, &c);
		for (int i = 0; i < c; i++) {
			scanf("%lld", a+i);
		}

		// choose two
		memset(has_booster, 0, sizeof(has_booster));
		result = -1;
		int work_index = 0;
		if (n - c * l - 1 > 0) work_index = n - c * l;
		work (l, work_index);

		printf("%d\n", (int)roundl(result));
	}
	
	return 0;
}
