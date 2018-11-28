#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int vet[1001];
int cop[1001];

int main()
{
	int n, c;
	scanf("%d", &n);
	
	for (int q = 1; q <= n; ++q)
	{
		scanf("%d", &c);
		for (int i = 0; i < c; ++i)
			scanf("%d", &vet[i]);
		memcpy(cop, vet, sizeof vet);
		sort(cop, cop+c);
		int res = 0;
		// best
		for (int i = 0; i < c; ++i)
		{
			if (cop[i] == vet[i])
				continue;
			++res;
		}
		printf("Case #%d: %d.000000\n", q, res);
	}
	
	return 0;
}

