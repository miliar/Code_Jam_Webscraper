#include <stdio.h>
#include <conio.h>

int ans[200];

int main()
{
	FILE *fin = fopen("C-large.in", "rt");
	FILE *fout = fopen("C-large.out", "wt");

	int T;
	fscanf(fin, "%d", &T);
	for (int c = 0; c < T; c++)
	{
		int K, n;
		fscanf(fin, "%d %d", &K, &n);

		for (int i = 0; i < n; i++)
		{
			int index;
			fscanf(fin, "%d", &index);

			index--;
			for (int j = 1; j < K; j++)
			{
				if (index < j) break;
				int modder = K - j;

				index -= j;
				index += modder - j%modder;
				index %= modder;
				index += j;
			}

			ans[i] = index + 1;
		}

		fprintf(fout, "Case #%d: ", c+1);
		for (int i = 0; i < n; i++)
		{
			fprintf(fout, "%d ", ans[i]);
		}
		fprintf(fout, "\n");
	}
	//getch();

	fclose(fin);
	fclose(fout);
}