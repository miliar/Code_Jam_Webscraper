#include <cstdio>
#include <cstring>


int nt, n;

int a[1000], b[1000];

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d", &n);
		for(int i = 0; i < n; i++) scanf("%d %d", &a[i], &b[i]);

		int res = 0;

		for(int i = 0; i < n; i++)
		for(int j = i + 1; j < n; j++) if ((a[i] < a[j]) ^ (b[i] < b[j])) res++;

		printf("%d\n", res);
	}

	return 0;	
}