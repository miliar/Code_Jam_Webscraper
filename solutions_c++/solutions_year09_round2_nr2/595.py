#include <cstdio>
#include <algorithm>
using namespace std;
char st[1000];
int test;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%s", st + 1);
		st[0] = '0';
		next_permutation(st, st + strlen(st));
		if (st[0] != '0') printf("Case #%d: %s\n", tt, st);
		else printf("Case #%d: %s\n", tt, st + 1);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}