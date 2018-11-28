#include <stdio.h>
FILE *in=fopen("A-large.in","r");
FILE *out=fopen("output.txt","w");

int T;
int n,k;
int math[31];

int main(){
	int i;
	fscanf(in,"%d",&T);
	math[0]=1;
	for(i=1;i<=30;i++) math[i]=math[i-1]*2;
	for(i=0;i<T;i++){
		fscanf(in,"%d%d",&n,&k);
		fprintf(out,"Case #%d: ",i+1);
		if((k+1)%math[n]==0) fprintf(out,"ON\n");
		else fprintf(out,"OFF\n");
	}
	return 0;
}
