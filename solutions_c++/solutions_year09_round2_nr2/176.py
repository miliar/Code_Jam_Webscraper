#include <cstdio>
#include <algorithm>
using namespace std;

#define For(i,n) for (int i = 0; i < n; ++i)

int T, n, t;
char s[256];

int main() {
	scanf("%d", &T);
	For(r,T) {
		printf("Case #%d: ", r + 1);
		s[0] = '0'; scanf("%s", s + 1);
		n = -1; while (s[++n]);
		t = n; while (s[t] <= s[t - 1]) --t; --t;
		next_permutation(s + t, s + n);
		if (s[0]^'0') putchar(s[0]);
		For(i,n-1) putchar(s[i + 1]); puts("");
	}
	return 0;
}
