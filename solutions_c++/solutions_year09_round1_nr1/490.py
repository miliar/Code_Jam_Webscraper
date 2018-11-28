#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>

using namespace std;

static inline int
happy(int n, int b)
{
	int r = 0;
	while (n) {
		int t = n % b;
		r += t * t;
		n /= b;
	}
	return r;
}

static inline bool
ok(int n, int b)
{
	set<int> in;
	in.insert(n);
	while (1) {
		n = happy(n, b);
		if (n == 1)
			return true;
		if (in.insert(n).second == false)
			break;
	}
	return false;
}

static int
get()
{
	static char line[80];
	static int base[10];
	fgets(line, sizeof(line), stdin);
	int n = 0;
	for (char *p = strtok(line, " \n"); p; p = strtok(NULL, " \n"))
		base[n++] = atoi(p);
	for (int i = 2; ; i++) {
		int j;
		for (j = 0; j < n; j++)
			if (!ok(i, base[j]))
				break;
		if (j == n)
			return i;
	}
	return -1;
}

int
main()
{
	int t;
	scanf("%d ", &t);
	for (int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, get());
	return 0;
}
