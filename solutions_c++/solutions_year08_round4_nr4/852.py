#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

enum {SIZE = 1004};

static char from[SIZE], to[SIZE];
static int  idx[6];

static inline void
perm(char *f, char *t, int n)
{
	for (int i = 0; i < n; i++)
		t[i] = f[idx[i]];
}

static inline int
rle(char *p, int n)
{
	int ret = 1;
	for (int i = 1; i < n; i++)
		if (p[i] != p[i - 1])
			ret++;
	return (ret);
}

static void
doit()
{
	int k;
	scanf("%d%s", &k, from);
	for (int i = 0; i < k; i++)
		idx[i] = i;
	int s = strlen(from), ans = s;
	do {
		for (int i = 0; i < s; i += k)
			perm(from + i, to + i, k);
		int now = rle(to, s);
		if (now < ans)
			ans = now;
	} while (next_permutation(idx, idx + k));
	printf("%d\n", ans);
}

int
main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		doit();
	}
	return (0);
}
