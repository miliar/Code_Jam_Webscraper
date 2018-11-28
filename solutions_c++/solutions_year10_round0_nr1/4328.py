#include <stdio.h>
#include <memory.h>
#include <conio.h>
#include<string.h>
int main(){
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".txt"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	unsigned int T=0,N=0;
	unsigned long K=0,k=0;
	bool s[32];
	if(fp==0){
		printf("file cant be opened");
	}
	else{
		fscanf(fp,"%u",&T);
		for(int i=1;i<=T;i++){
			fscanf(fp,"%u%u",&N,&K);
			fprintf(ofp,"Case #%d: ",i);
			memset(s,false,32);
			unsigned int j;
			for(k=0;k<K;k++){
				j=0;
				while(s[j]&&j<N){
					s[j]=!s[j];
					j++;
				}
				if(j!=N)
					s[j]=!s[j];
			}
			j=0;
			while(s[j]&&j<N)
				j++;
			if(j==N)
				fprintf(ofp,"ON\n");
			else
				fprintf(ofp,"OFF\n");
		}
	}
	return 0;
}