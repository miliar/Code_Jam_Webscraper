#include <stdio.h>

int T,N;
int Ans;

FILE *in = fopen("input.txt","r");//stdin;
FILE *out = fopen("output.txt","w");

struct OTL{
	char h;
	int btt;
};
OTL P[100];

int abs(int a){
	return (a<0)?-a:a;
}

int main(void){
	int a,b,i,j,t;
	char im[5];

	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++){
		fscanf(in,"%d",&N);
		a=1,b=1;Ans=0;
		for(i=0;i<N;i++){
			fscanf(in,"%s%d",&im,&P[i].btt);
			P[i].h=im[0];
		}
		for(i=0;i<N;i++){
			if(P[i].h=='O'){
				for(j=i+1;j<N;j++){
					if(P[j].h=='B')break;
				}
				Ans+=abs(a-P[i].btt)+1;
				if(j!=N){
					if(b>P[j].btt){
						b=b-abs(a-P[i].btt)-1;
						if(b<P[j].btt)b=P[j].btt;
					}
					else{
						b=b+abs(a-P[i].btt)+1;
						if(b>P[j].btt)b=P[j].btt;
					}
				}
				a=P[i].btt;
			}
			else{
				for(j=i+1;j<N;j++){
					if(P[j].h=='O')break;
				}
				Ans+=abs(b-P[i].btt)+1;
				if(j!=N){
					if(a>P[j].btt){
						a=a-abs(b-P[i].btt)-1;
						if(a<P[j].btt)a=P[j].btt;
					}
					else{
						a=a+abs(b-P[i].btt)+1;
						if(a>P[j].btt)a=P[j].btt;
					}
				}
				b=P[i].btt;
			}
		}
		fprintf(out,"Case #%d: %d\n",t,Ans);
	}
	return 0;
}