#include<stdio.h>

int n;
int candy[1000];

int main(void){
	int T;
	int xr, min, sum;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(int i=0;i<T;i++){
		xr = 0; min = 99999999; sum = 0;
		fscanf(fin,"%d",&n);
		for(int j=0;j<n;j++){
			fscanf(fin,"%d",&candy[j]);
			xr = xr ^ candy[j];
			if(candy[j] < min) min = candy[j];
			sum += candy[j];
		}
		fprintf(fout,"Case #%d: ",i+1);
		if(xr == 0){
			fprintf(fout,"%d\n", sum - min);
		} else{
			fprintf(fout,"NO\n");
		}
	}
	fcloseall();
	return 0;
}