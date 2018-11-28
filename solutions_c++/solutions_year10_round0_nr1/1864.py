#include <iostream>
#include <algorithm>

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define FOR(i, l, r) for (int i = (l); i <= (r); ++i)
#define ROF(i, r, l) for (int i = (r); i >= (l); --i)

using namespace std;

int T, n, K;
int f[100];

int main()
{
	scanf("%d", &T);
	FOR(testcase, 1, T) {
		scanf("%d%d", &n, &K);
		printf("Case #%d: ", testcase);
		FOR(i, 1, n)
			f[i] = f[i - 1] * 2 + 1;
		if ((K & f[n]) != f[n]) puts("OFF");
		else puts("ON");
	}
}
