// prelim_c.cpp : Defines the entry point for the console application.
//

#include<stdio.h>
#include<memory.h>
#include<string.h>

int grp[10000000];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int tc;
	int k, r, n;
	int i, j, a, b, counter;
	int p;
	unsigned __int64 ans;

	fscanf(fp, "%d", &tc);

	for(i=1; i<=tc; i++){

		fscanf(fp, "%d %d %d", &r, &k, &n);
		for(j=1; j<=n; j++){
			fscanf(fp, "%d", &grp[j]);
		}
		ans = 0;
		a = 1;
		for(j=1; j<=r; j++){
			p = 0;
			counter = 0;
			while(p <= k && counter != n+1){
				p = p + grp[a];
				a++;
				if(a == n+1) a=1;
				counter++;
			}
			a--;
			if(a == 0) a=n;
			p = p - grp[a];
			ans = ans + p;
		}
		fprintf(ofp, "Case #%d: %d\n", i, ans);

	}

	return 0;
}

