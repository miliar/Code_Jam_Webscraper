#include<stdio.h>
#include<string.h>
#include<stdlib.h>

FILE *fs = fopen("input.txt","rt");
FILE *fp = fopen("output.txt","wt");

char base[20];
char test[501];

int dy[501][20];
int n,len;
int sol;

int main()
{
	int i,j,k,l;
	
	strcpy(base,"welcome to code jam");
	fscanf(fs,"%d\n",&n);
	for(i=1;i<=n;i++){
		for(j=0;j<=500;j++) test[j]=0;
		fgets(test,500,fs);
		for(j=0;;j++) if(test[j] == '\n' || test[j]==0) break;
		len = j;

		for(j=0;j<len;j++){
			for(k=0;k<=18;k++) dy[j][k] = 0;
			if(test[j] == 'w') dy[j][0] = 1;
		}

		for(j=0;j<len;j++){
			for(k=0;k<j;k++){
				for(l=0;l<=17;l++){
					if(test[k] == base[l] && test[j] == base[l+1]){
						dy[j][l+1] += dy[k][l];
						dy[j][l+1] %= 10000;												
					}
				}			
			}
		}

		sol = 0;
		for(j=0;j<len;j++){
			sol += dy[j][18];
			sol %= 10000;
		}
		fprintf(fp,"Case #%d: ",i);
		if(sol / 1000 == 0) fprintf(fp,"0");
		if(sol / 100 == 0) fprintf(fp,"0");
		if(sol / 10 == 0) fprintf(fp,"0");
		fprintf(fp,"%d\n",sol);
	}
	return 0;
}
