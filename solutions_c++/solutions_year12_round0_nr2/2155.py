#include <cstdio>
#include <vector>

using namespace std;

int n, s, p;
int b0;
int b1;
int b2;

int solveCase() {
	scanf("%d%d%d", &n, &s, &p);
	b0 = b1 = b2 = 0;

	while (n--) {
		int val;
		scanf("%d", &val);

		if (val == 30)
			++b1;
		else if (val > 30 || val < 0)
			++val;
		else if (val == 29)
			++b1;
		else if (val == 0) {
			if (p == 0)
				++b1;
		}
		else if (val == 1) {
			if (p == 1)
				++b1;
		}
		else if (val == 2) {
			if (p <= 1)
				++b0;
			else if (p <= 2)
				++b2;
		}
		else if (val % 3 == 0) {
			bool norm = false, spec = false;

			if (val/3 >= p)
				norm = true;
			if (val/3 + 1 >= p)
				spec = true;

			if (norm && spec)
				++b0;
			else if (norm)
				++b1;
			else if (spec)
				++b2;
		}
		else if (val % 3 == 1) {
			if (val/3 + 1 >= p)
				++b0;
		}
		else if (val % 3 == 2) {
			if (val/3 + 1 >= p)
				++b0;
			else if (val/3 + 2 >= p)
				++b2;
		}
	}

	int res = 0;
	res += (b2 < s ? b2 : s);
	s -= res;
	res += b1;
	res += b0;

	return res;
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; ++i)
		printf("Case #%d: %d\n", i, solveCase());

	return 0;
}
