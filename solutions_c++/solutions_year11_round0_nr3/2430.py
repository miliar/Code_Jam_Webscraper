#include <stdio.h>

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int T,N,Sum,min;

int main(void){
	int t,im,num,i;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++){
		fscanf(in,"%d",&N);
		im=0,Sum=0;
		for(i=0;i<N;i++){
			fscanf(in,"%d",&num);
			im=im^num;
			Sum+=num;
			if(i==0)min=num;
			else if(min>num)min=num;
		}
		fprintf(out,"Case #%d: ",t);
		if(im!=0)fprintf(out,"NO\n");
		else fprintf(out,"%d\n",Sum-min);
	}
	return 0;
}