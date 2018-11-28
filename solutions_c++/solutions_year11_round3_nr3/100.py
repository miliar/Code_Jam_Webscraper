#include <stdio.h>

int T;
int L,N,H;
int P[100];

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int gcd(int a,int b){
	if(a%b==0)return b;
	return gcd(b,a%b);
}

int main(void){
	int t,i,j;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++){
		fscanf(in,"%d%d%d",&N,&L,&H);
		for(i=0;i<N;i++){
			fscanf(in,"%d",&P[i]);
		}
		for(i=L;i<=H;i++){
			for(j=0;j<N;j++){
				if(P[j]%i!=0 && i%P[j]!=0)break;
			}
			if(j==N)break;
		}
		fprintf(out,"Case #%d: ",t);
		if(i==H+1)fprintf(out,"NO\n");
		else fprintf(out,"%d\n",i);
	}
	return 0;
}