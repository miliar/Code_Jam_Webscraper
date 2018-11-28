#include <cstdio>
#include <algorithm>

using namespace std;

void solve()
{
	int p[2] = {1, 1}, ft[2]={}, pr = 0;
	int n, r = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		char rb; int np;
		scanf(" %c%d", &rb, &np);

		int cr = (rb == 'O') ? 0 : 1;
		int rt = abs(np - p[cr]) + 1;
		
		p[cr] = np;

		int uft = min(ft[cr], rt - 1);
		r += rt - uft;
		ft[1-cr] += rt - uft;
		ft[cr] = 0;

		pr = cr;
	}
	printf("%d", r);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
		printf("\n");
	}
	return 0;
}