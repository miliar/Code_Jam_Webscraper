#include <cstdio>
#include <algorithm>

using namespace std;

enum {SIZE = 804};

typedef long long ll_t;

static ll_t	x[SIZE], y[SIZE], sum;

static inline bool
run(int n)
{
	bool ret = false;
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++) {
			ll_t old = x[i] * y[i] + x[j] * y[j],
			     now = x[i] * y[j] + x[j] * y[i];
			if (now < old) {
				swap(y[i], y[j]);
				sum = sum - old + now;
				ret = true;
			}
		}
	return (ret);
}

static void
doit()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%lld", &x[i]);
	sum = 0;
	for (int i = 0; i < n; i++) {
		scanf("%lld", &y[i]);
		sum += x[i] * y[i];
	}
	while (run(n))
		;
	printf("%lld\n", sum);
}

int
main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		doit();
	}
}
