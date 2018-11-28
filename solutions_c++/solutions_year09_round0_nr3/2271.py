#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int N;
char Inp[1000];
int len;
int D[1000][20];
char Str[30]="awelcome to code jam";
int len2;

int main(){
	int i, j, k;

	FILE *fin = fopen("c-large.in","r");
	FILE *fout = fopen("c-large.out","w");

	fscanf(fin,"%d\n",&N);

	len2=strlen(Str);

	for(k=1;k<=N;k++){
		fgets(Inp+1,700,fin);
		len=strlen(Inp+1);
		for(i=0;i<=len;i++){
			for(j=0;j<len2;j++){
				D[i][j]=0;
			}
		}

		for(i=0;i<=len;i++)
			D[i][0]=1;

		for(i=1;i<=len;i++){
			for(j=1;j<len2;j++){
				D[i][j]=D[i-1][j];
				if(Inp[i]==Str[j])
					D[i][j]=(D[i][j]+D[i-1][j-1])%10000;
			}
		}

		fprintf(fout,"Case #%d: ",k);
		if(D[len][len2-1]<10){
			fprintf(fout,"000%d\n",D[len][len2-1]);
		}else if(D[len][len2-1]<100){
			fprintf(fout,"00%d\n",D[len][len2-1]);
		}else if(D[len][len2-1]<1000){
			fprintf(fout,"0%d\n",D[len][len2-1]);
		}else{
			fprintf(fout,"%d\n",D[len][len2-1]);
		}
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
