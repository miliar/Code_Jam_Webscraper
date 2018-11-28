#include <stdio.h>
#include <string.h>


int main(){
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	int tc,i=0;
	int R,N,k,tot_pass,q,gross_tot;
	fscanf(fp, "%d", &tc);
	while(i<tc)
	{
		i++;
		q=0;
		gross_tot=0;
		fscanf(fp, "%d %d %d", &R,&k,&N);
		int *groups = new int[N];
		for(int j=0;j<N;j++)
			fscanf(fp, "%d", &groups[j]);
		for(int r=0;r<R;r++)
		{
			tot_pass=0;

			for(int l=0;l<N;l++)
			{
				tot_pass+=groups[q];
				if(tot_pass>k)
					{
						tot_pass-=groups[q];
						break;
					}
				q++;
				if(q == N) q=0;
			}
			gross_tot+=tot_pass;
		}
		fprintf(ofp, "Case #%d: %d\n",i, gross_tot);
		delete [] groups;
	}
	return 0;
	}