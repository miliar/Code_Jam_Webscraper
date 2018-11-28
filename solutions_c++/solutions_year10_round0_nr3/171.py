#include <stdio.h>
#include <string.h>

typedef long long LL;

int tc, ntc;
LL R, K;
int n;
LL ar[2000];

int nex[2000];
LL am[2000];

void gen_next()
{
	int i, j;
	for (i=0; i<n; i++)
	{
		LL tot = 0;
		for (j=i;;j=(j+1)%n)
		{
			if (tot + ar[j] > K) break;
			tot += ar[j];
		}
		nex[i] = j;
		am[i] = tot;
	}
}

int pos[2000];

LL doit()
{
	LL sum = 0;
	int i;
	for (i=0; i<n; i++) sum += ar[i];
	if (sum <= K) return sum * R;

	gen_next();

	memset(pos, -1, sizeof(pos));

	int cur = 0;
	int it;
	LL res = 0;
	for (it=0; it<R; it++)
	{
		if (pos[cur] != -1) break;
		pos[cur] = it;

		res += am[cur];
		cur = nex[cur];
	}

	if (it == R) return res;
	int period = it - pos[cur];
	
	//printf("%d %d %I64d\n", it, period, res);

	LL sum_cyc = 0;
	int zcur = cur;
	for (i=pos[cur]; i<it; i++, zcur = nex[zcur]) sum_cyc += am[zcur];

	LL ncyc = (R-it) / period;
	res += ncyc * sum_cyc;

	//printf("%I64d %I64d %I64d\n", ncyc, sum_cyc, res);

	LL rem = R - it - ncyc*period;
	for (i=0; i<rem; i++)
	{
		res += am[cur];
		cur = nex[cur];
	}

	return res;
}

int main()
{
	FILE* fi = fopen("C-large.in", "r");
	FILE* fo = fopen("C-large.out", "w");

	fscanf(fi, "%d", &ntc);
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%I64d %I64d %d", &R, &K, &n);
		int i;
		for (i=0; i<n; i++)
			fscanf(fi, "%I64d", &ar[i]);

		LL res = doit();
		fprintf(fo, "Case #%d: %I64d\n", tc, res);
		printf("Case #%d: %I64d\n", tc, res);
	}

	return 0;
}