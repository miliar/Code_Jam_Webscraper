#include <stdio.h>

int T,N,M;
char P[51][51];

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

bool chk(int a,int b){
	int k;
	int dira[4]={0,1,0,1};
	int dirb[4]={0,1,1,0};
	for(k=0;k<4;k++){
		if(dira[k]+a>=N||dirb[k]+b>=M||P[dira[k]+a][dirb[k]+b]!='#')return false;
		if(k<2)P[dira[k]+a][dirb[k]+b]='/';
		else P[dira[k]+a][dirb[k]+b]='\\';
	}return true;
}

int main(void){
	int t;
	int i,j;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++){
		fscanf(in,"%d%d",&N,&M);
		for(i=0;i<N;i++){
			fscanf(in,"%s",&P[i]);
		}
		for(i=0;i<N;i++){
			for(j=0;j<M;j++){
				if(P[i][j]=='#'){
					if(!chk(i,j))break;
				}
			}
			if(j!=M)break;
		}
		fprintf(out,"Case #%d:\n",t);
		if(i==N){
			for(i=0;i<N;i++){
				fprintf(out,"%s\n",P[i]);
			}
		}
		else{
			fprintf(out,"Impossible\n");
		}
	}
	return 0;
}