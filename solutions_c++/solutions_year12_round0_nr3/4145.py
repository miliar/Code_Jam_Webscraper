#include <cstdio>
#include <iostream>

using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)

int s[2000000 + 55];
int deg10[8];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, i, a, b, j, ans, ok, l;

	deg10[0] = 1;
	for (i = 1; i < 8; ++i)
		deg10[i] = deg10[i - 1] * 10;

	scanf("%d", &t);
	forn(i, t) {
		scanf("%d %d", &a, &b);
		ans = 0;
		for (j = a; j <= b; ++j) {
			ok = 0;
			int total, tmp = j, sum = 0, total2;
			while (tmp) ++sum, tmp /= 10;
			for (l = 1; l <= sum - 1; ++l) {
				int left = j / deg10[l], right = (j % deg10[l]);
				if (left == 0)
					break;
				total2 = 0, tmp = right;
				while (tmp) ++total2, tmp /= 10;
				if (total2 != l)
					continue;
				total = 0, tmp = left;
				while (tmp) ++total, tmp /= 10;
				if (total + l != sum)
					continue;
				int x = left + right*deg10[total];
				if (x >= a && x <= b && j < x) {
					//if (i == 3)
					//cout << j << "  " << x << endl;
					++ans;
				}
			}
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}

	return 0;
}