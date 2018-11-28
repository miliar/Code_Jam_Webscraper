#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int t[3];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int T,N;
	int res,dif[2];
	int m,n,div;
	fscanf(fp,"%d",&T);
	for ( int num = 1; num <= T; num++){
		fscanf(fp,"%d",&N);
		for(int i = 0; i < N; i++)
			fscanf(fp,"%d", &t[i]);
		if(N == 2){
			dif[0] = abs(t[1]-t[0]);
			if(t[0] > t[1])
				t[0] = t[1];
			if(t[0]%dif[0] == 0)
				res = 0;
			else 
				res = dif[0]-t[0]%dif[0];
		}
		else{
			dif[0] = abs(t[1]-t[0]);
			dif[1] = abs(t[2]-t[1]);
			m = dif[0]; 
			n = dif[1];
			for (;n;m=n,n=div)
				div = m%n;
			if (t[0] > t[2])
				t[0] = t[2];
			if(t[0]%m == 0)
				res = 0;
			else
				res = m - t[0]%m;
		}			
		fprintf(ofp,"Case #%d: %d\n",num,res);
	}
	return 0;
}
