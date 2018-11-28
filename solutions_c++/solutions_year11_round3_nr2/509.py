#include <stdio.h>


int main()
{
	int a[2000];
	int b[2000];

	int ca;
	int cnt=0;
	FILE *fin = fopen("in.in", "r");
	FILE *fout = fopen("out.out", "w");
	fscanf(fin,"%d", &ca);
	while (ca--)
	{
		int L,t,N,C; 
		fscanf(fin, "%d %d %d %d", &L, &t, &N, &C);

		for (int i=0; i<C; i++)
			fscanf(fin, "%d", &a[i]);

		int n = 0;
		for (int i=0; i<=C; i++)
			b[i] = 0;

		int ans = 0;

		// 부스터 안 쓰고 최대값
		for (int i=0; i<N; i++)
		{
			ans += a[n] * 2;	
			b[n]++;
			n = (n + 1) % C;
		}

		n = 0;
		for (int i=0; i<N; i++)
		{
			b[n]--;

			if (t - a[n] * 2> 0)
			{
				t = t - a[n] * 2;
			}
			else
			{
				a[C] = a[n] - t / 2;
				b[C] = 1;
				break;
			}
			n = (n + 1) % C;
		}

		for (int i=0; i<=C; i++)
		for (int j=i+1; j<=C; j++)
		{
			if (a[i] < a[j])
			{
				a[i] += a[j];
				a[j] = a[i] - a[j];
				a[i] = a[i] - a[j];

				b[i] += b[j];
				b[j] = b[i] - b[j];
				b[i] = b[i] - b[j];
			}
		}

		n = 0;
		for (int i=0; i<L; i++)
		{
			while (b[n] == 0 && n <= C) n++;
			if (n > C) break;
			ans -= a[n];
			b[n]--;
		}
		fprintf(fout, "Case #%d: %d\n", ++cnt, ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}