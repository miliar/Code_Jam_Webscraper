#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int g[1000];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int T,R,N,k;
	int total,sum;
	int start,count,pos;
	int flag;
	fscanf(fp,"%d",&T);
	for(int t = 1; t <= T; t++){
		fscanf(fp,"%d %d %d",&R,&k,&N);
		for(int i = 0; i < N; i++)
			fscanf(fp,"%d", &g[i]);
		total = 0;
		start = 0;
		for ( int i = 0; i < R; i++){
			sum = 0;
			pos = start;
			flag = 1;
			count = 1;
			while (flag){
				if(pos == N)
					pos = 0;
				if((sum+g[pos]) <= k && count <= N){
					sum += g[pos];
					pos++;
					count++;
				}
				else{
					flag = 0;
					start = pos;
				}
			}
			total += sum;
		}
		fprintf(ofp,"Case #%d: %d\n",t,total);
	}

	return 0;
}
