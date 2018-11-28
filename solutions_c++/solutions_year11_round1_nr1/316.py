#include <climits>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define foreach(iter, cont) \
	for (typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)

bool solve ()
{
	long long n;
	int pd, pg;
	scanf("%lld %d %d", &n, &pd, &pg);
	if (pg == 100 && pd != 100)
		return false;
	if (pg == 0 && pd != 0)
		return false;
	if (pg == 0 && pd == 0)
		return true;
/*	for (int d = 1; d <= n; ++d) {
		if ((d * pd % 100) == 0)
			return true;
	}*/
	int two = 2, five = 2;
	while (pd && two && (pd % 2) == 0) {
		pd /= 2;
		two--;
	}
	while (pd && five && (pd % 5) == 0) {
		pd /= 5;
		five--;
	}
	if ((pow(2, two) * pow(5, five)) <= n)
		return true;

	return false;
}

int main ()
{
	int T;
	scanf ("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf ("Case #%d: %s\n", i, solve() ? "Possible" : "Broken");
	}
	return 0;
}
