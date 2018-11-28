#include <stdio.h>
#include <iostream>
using namespace std;

#define FOR(i,n) for(i=0; i<(n); ++i)

int main()
{
	FILE *fi = fopen("a.txt", "rt");
	FILE *fo = fopen("a.out", "wt");

	int t,tt;
	int A[100];
	int B[100];

	fscanf(fi, "%d", &tt);
	FOR(t,tt)
	{
		int n,i,j,k, res = 0;
		fscanf(fi, "%d", &n);
		FOR(i,n)
		{
			fscanf(fi, "%d", &A[i]);
		}
		FOR(j, 1<<n)
		{
			int s1=0, s2=0;
			int sx1=0, sx2=0;
			FOR(k,n)
			{
				if (j & (1<<k))
				{
					s1 += A[k];
					sx1 ^= A[k];
				}
				else
				{
					s2 += A[k];
					sx2 ^= A[k];
				}
			}
			if (sx1 == sx2 && s1 != 0 && s2 != 0)
			{
				if (s1 > res) res = s1;
				if (s2 > res) res = s2;
			}
		}
		fprintf(fo, "Case #%d: ", t+1);
		if (res == 0) fprintf(fo, "NO\n");
		else fprintf(fo, "%d\n", res);
	}

	fclose(fo);
	fclose(fi);
	return 0;
}