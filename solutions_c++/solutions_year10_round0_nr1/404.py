#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define Size(a) ((int)a.size())

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);
		int n, k;
		scanf("%d %d", &n, &k);
		int p = (1 << n), r = p - 1;
		if (k < r || (k - r) % p) {
			printf("OFF\n");
		} else {
			printf("ON\n");
		}
	}
	return 0;
}