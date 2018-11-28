#include <cstdio>
#include <algorithm>

using namespace std;

int vet[1001];

int main()
{
	int n, c;
	scanf("%d", &n);
	
	for (int q = 1; q <= n; ++q)
	{
		scanf("%d", &c);
		for (int i = 0; i < c; ++i)
			scanf("%d", &vet[i]);
		sort(vet, vet+c);
		int r = vet[0];
		for (int i = 1; i < c; ++i)
			r ^= vet[i];
		printf("Case #%d: ", q);
		if (r)
			printf("NO\n");
		else
		{
			r = 0;
			for (int i = 1; i < c; ++i)
				r += vet[i];
			printf("%d\n", r);
		}
	}
	
	return 0;
}

