#include <stdio.h>
#include <math.h>
#include <string.h>

long R;
long K;
long N;
long g[50];
int m;
long add=0;
long sum = 0;
#define min(a,b) ((a <=b)?a:b)


int main()
{

//char filename[32];
char infile[32], outfile[32];
//scanf("%s", filename);
//scrcpy(filename,"C-small-attempt0");
//sprintf(filename,"%s", "C-small-attempt0");

strcpy(infile, "C-small-attempt2"); strcpy(outfile,"C-small-attempt2");
strcat(infile, ".in"); strcat(outfile, ".out");
FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

fscanf(fp, "%d", &m);



for(int i=1;i<=m; i++){
	sum = 0;
	int counter = 1;
	int p=0;
	long sum2=0;
	fscanf(fp,"%d %d %d",&R,&K,&N);
	for (int j=0;j<N;++j){
		fscanf(fp,"%d",&g[j]);
	}
	for (int t=0;t<N;++t){
		sum2=sum2+g[t];
	}

	while (counter <= R){
		
		while((add+g[p]) <= K){
			add = add + g[p];
			p=p+1;
			if (p>N-1){
				p = p-N;
			}
		}
		counter ++;
		sum += add;
		add = 0;
	}
	fprintf(ofp, "Case #%d: %ld\n", i, min(sum2*R,sum));
}
return 0;
}


















