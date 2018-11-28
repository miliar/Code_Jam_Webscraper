#include <cstdio>
const int LIM = 100;
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 0; cas < t; cas++)
	{
		int freq[LIM]; // frequencies
		int n, l, h;
		scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; i++)
			scanf("%d", &freq[i]);
		int frq;
		for (frq = l; frq <= h; frq++)
		{
			int i;
			for (i = 0; i < n && (frq % freq[i] == 0 || freq[i] % frq == 0); i++);
			if (i >= n)
				break;
		}
		printf("Case #%d: ", cas + 1);
		if (frq <= h)
			printf("%d\n", frq);
		else
			printf("NO\n");
	}
	return 0;
}