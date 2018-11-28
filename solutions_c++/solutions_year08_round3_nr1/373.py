#include <stdio.h>
#include <iostream.h>
#include <stdlib.h>

int N;
int P, K, L;
int freq[1010];
int keys[101][1010];

int num;

int cmp(const void *a, const void *b)
{
	return *(int *)b - *(int *)a;
}

long long Solve()
{
	long long res = 0;
	
	if(L / K > P)
	{
		return -1;
	}
	if(L / K == P && L % K != 0)
		return -1;
	
	int fact;
	
	for(int i = 0; i < L; i++)
	{
		fact = i / K + 1;
		
		res += (fact * freq[i]);
	}
	
	return res;
}

int main()
{
	FILE *in;
	FILE *out;
	in = fopen("A-large.in", "r");
	out = fopen("result.txt", "wt");
	
	fscanf(in, "%d", &N);
	
	for(num = 1; num <= N; num++)
	{
		fscanf(in,"%d%d%d", &P, &K, &L);
		
		for(int i = 0; i < L; i++)
		{
			fscanf(in,"%d", &freq[i]);
		}
		
		qsort(freq, L, sizeof(int), cmp);
		
		long long ans = Solve();
		
		if(ans != -1)
		{
			fprintf(out, "Case #%d: %I64d\n", num, ans);
		}
		else
		{
			fprintf(out, "Case #%d: Impossible\n", num);
		}
	}
}