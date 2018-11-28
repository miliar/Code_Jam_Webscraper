#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main() {
	FILE *in = fopen("C.in","r");
	FILE *out = fopen("C.out","w");
	int N,i,j,k,len;
	fscanf(in,"%d",&N);
	char buff[512];
	int d[20];
	char *str="welcome to code jam";
	for(i=0;i<N;i++) {
		for(j=0;j<20;j++)
			d[j]=0;
		d[0]=1;
		fscanf(in,"\n%[^\n]",buff);
		len=strlen(buff);
		for(j=0;j<len;j++) {
			for(k=0;k<19;k++) {
				if(buff[j]==str[k]) 
					d[k+1]=(d[k]+d[k+1])%10000;
			}
		}
		for(j=0;j<20;j++) {
			printf("%d ",d[j]);
		}
		printf("\n");
		fprintf(out,"Case #%d: %04d\n",i+1,d[19]);
	}
	fclose(in);
	fclose(out);
}