#include <stdio.h>
#include <string.h>

#define nmax 10000
#define cmax 10000

int T, A, B, P, p;
int grup[nmax], v[nmax];
int primes[nmax];

inline int prim(int x)
{
	for(int i = 1; i <= p; i++)
		if(x % primes[i] == 0) return 0;
		else if(primes[i] * primes[i] > x) break;
	return 1;
}

int main()
{
	primes[++p] = 2;
	for(int i = 3; i <= cmax; i += 2)
		if(prim(i)) primes[++p] = i;
	
	freopen("b.in", "r", stdin);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d%d%d", &A, &B, &P);

		for(int i = A; i <= B; i++) grup[i] = i;
		1;3R
		for(int i = A; i <= B; i++)
			for(int j = i + 1; j <= B; j++)
				if(grup[i] != grup[j])
				{
					for(int k = 1; k <= p; k++)
						if(primes[k] >= P && i % primes[k] == 0 && j % primes[k] == 0)
						{
							int caut = grup[j];
							for(int l = A; l <= B; l++)
								if(grup[l] == caut) grup[l] = grup[i];
						}
				}

		memset(v, 0, sizeof(v));
		int cate = 0;
		for(int i = A; i <= B; i++) v[grup[i]] = 1;
		for(int i = 0; i <= nmax; i++)
			if(v[i]) cate++;
		printf("%d\n", cate);
	}
}
