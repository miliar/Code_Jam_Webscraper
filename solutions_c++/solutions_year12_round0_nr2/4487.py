#include <stdio.h>
#include <math.h>
int main()
{
	FILE *fin, *fout;
	fin = fopen("B-large.in", "r");
	fout = fopen("out.txt","w");
	int T, N, S, P;
	int i, j;
	int goo[100];
	int ns, hs, ans;
	int temp;
	fscanf(fin, "%d", &T);
	for (i = 0; i < T; i++)
	{
		fscanf(fin, "%d %d %d", &N, &S, &P);
		ns = 0;
		hs = 0;
		for (j = 0; j < N; j++)
		{
			fscanf(fin, "%d", &goo[j]);
			temp = goo[j] - P;
			if (temp >= 0){
			if (temp >= 2 * (P - 1)) ns += 1;
			else if (temp >= 2 * (P - 2)) hs += 1;
			}
		}
		if (hs <= S) ans = ns + hs;
		else ans = ns + S;
		fprintf(fout, "Case #%d: %d\n", i + 1, ans); 
	}

	fclose(fin);
	fclose(fout);
	return 0;
}