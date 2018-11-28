#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 1000005

int N, LEFT;
int aib[MAXN], sol[MAXN];

inline void add( int poz, int val )
{
	for (; poz <= N; poz += (poz ^ (poz - 1)) & poz)
		aib[poz] += val;
}

inline int query( int poz )
{
	int rez = 0;
	for (; poz; poz &= (poz - 1))
		rez += aib[poz];
	return rez;
}

inline int getPoz( int start, int nr )
{
	if (nr - 1 > LEFT)
		nr = (nr - 1) % LEFT + 1;

	int next = query(N) - query(start);
	if (nr > next)
	{
		nr -= next;
		start = 0;
	}

	int poz, step;
	for (step = (1 << 20), poz = start; step; step >>= 1)
		if (poz + step <= N && query(poz + step) - query(start) < nr)
			poz += step;
	return poz + 1;
}

int main()
{
//	freopen("C.in", "rt", stdin);
//	freopen("C.out", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		memset( aib, 0, sizeof(aib) );
		for (int i = 1; i <= N; i++)
			add(i, 1);
		LEFT = N;
		for (int i = 1, last = 0; i <= N; i++)
		{
			last = getPoz(last, i);
			sol[last] = i;
			add(last, -1);
			LEFT--;
		}
		
		printf("Case #%d:", t);
		int K;
		scanf("%d", &K);
		for (int i = 0; i < K; i++)
		{
			int poz;
			scanf("%d", &poz);
			printf(" %d", sol[poz]);
		}
		printf("\n");
	}

	return 0;
}


