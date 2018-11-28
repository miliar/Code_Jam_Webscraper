#include <stdio.h>
#include <algorithm>

#define nmax 1005

using namespace std;

int k, p, l, T;
int a[nmax];

int main()
{
	freopen("a.in", "r", stdin);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d%d%d", &p, &k, &l);
		for(int i = 1; i <= l; i++) scanf("%d", &a[i]);
		sort(a + 1, a + l + 1);
		reverse(a + 1, a + l + 1);

		long long tot = 0;
		for(int i = 1; i <= l; i++)
		{
			int which = (i - 1) / k + 1;
			tot += a[i] * which;
		}
		printf("Case #%d: %Ld\n", t, tot);
	}
}
