#include <stdio.h>
#include <memory.h>
#include <conio.h>
#include<string.h>
int main(){
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	unsigned long T,K,R,N; 
	int g[100];
	fscanf(fp,"%u",&T);
	for(int i=1;i<=T;i++){
		fscanf(fp,"%u%u%u",&R,&K,&N);
		for(int j=0;j<N;j++)
			fscanf(fp,"%d",&g[j]);
		fprintf(ofp,"Case #%d: ",i);
		int k=0,mo=0,p,t;
		for(int j=0;j<R;j++){
			p=0,t=0;
			do{
				p+=g[k];
				k++;
				t++;
				if(k==N)
					k=0;
			}while((p+g[k])<=K&&t<N);
			mo+=p;
		}
		fprintf(ofp,"%u\n",mo);
	}
	return 0;
}
