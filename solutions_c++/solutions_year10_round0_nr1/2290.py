#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int T, N, K;
	int res;
	fscanf(fp,"%d", &T);
	for(int t = 1; t <= T; t++ ){
		fscanf(fp,"%d %d\n", &N, &K);
		res = (K+1) % (int)(pow(2,N));
		if(!res)
			fprintf(ofp,"Case #%d: ON\n",t);

		else
			fprintf(ofp,"Case #%d: OFF\n",t);
	}

	return 0;
}
