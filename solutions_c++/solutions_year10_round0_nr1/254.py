#include <cstdio>

using namespace std;

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		int p, q;
		scanf("%d %d", &p, &q);
		int r = (1 << p) - 1;
		q = q & r;
		printf("Case #%d: %s\n", ti, (q == r) ? "ON" : "OFF");
	}
	return 0;
}
