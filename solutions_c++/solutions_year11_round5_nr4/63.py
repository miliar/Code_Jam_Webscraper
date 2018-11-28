#include <cstdio>
#include <cmath>
using namespace std;

int T;
char s[256];

void exh(int l) {
	if (!s[l]) {
		long long x, y;
		x = 0;
		for (int i = 0; s[i]; ++i)
			x = 2*x + (s[i] - '0');
		y = sqrt(x) - 1;
		if (y < 0) y = 0;
		while (y*y < x) ++y;
		if (y*y == x)
			printf(" %s\n", s);
	} else {
		if (s[l] == '?') {
			s[l] = '0';
			exh(l + 1);
			s[l] = '1';
			exh(l + 1);
			s[l] = '?';
			return;
		}
		exh(l + 1);
	}
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d:", r);
		scanf("%s", s);
		exh(0);
	}
	return 0;
}
