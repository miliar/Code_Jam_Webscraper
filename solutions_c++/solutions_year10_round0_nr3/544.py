// GCJ 2010 Qual 
// 3. Theme Park

// May 8, 2010
// Jongwook Choi

#include <stdio.h>

int R, k, n;
int a[1001];
int nhead[1001];
long long nsum[1001];

long long go()
{
	for(int i=0; i<n; ++i)
	{
		long long s = a[i];
		nhead[i] = i;
		for(int j=(i+1)%n; j!=i; j=(j+1)%n)
		{
			if(s + a[j] > k)
			{
				nhead[i] = j;
				break;
			}
			s += a[j];
		}
		nsum[i] = s;
	}

	long long res = 0;
	int i = 0;
	while(R-- > 0)
	{
		res += nsum[i];
		i = nhead[i];
	}
	return res;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T, kase = 0;
	scanf("%d", &T);

	while(T-- > 0)
	{
		fprintf(stderr, "%d\n", T);
		scanf("%d %d %d", &R, &k, &n);
		for(int i=0; i<n; ++i) scanf("%d", a+i);
		printf("Case #%d: %lld\n", ++kase, go());
	}
	return 0;
}