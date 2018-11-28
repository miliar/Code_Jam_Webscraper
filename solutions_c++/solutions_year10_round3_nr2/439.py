#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++)
	{
		int a, b, res = 0;
		long long c;
		scanf("%d %d %lld", &a, &b, &c);
		while (a < b / c || a == b / c && b % c) {
			c *= c;
			res++;
		}
		printf("Case #%d: %d\n", itest, res);
	}
	return 0;
}