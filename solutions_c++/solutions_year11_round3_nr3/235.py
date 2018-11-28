#include<stdio.h>

int n,low,high;
int arr[10000];

int main(void){
	int t, T;
	int i, j;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");

	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++){
		fprintf(fout, "Case #%d: ", t);
		fscanf(fin,"%d %d %d",&n,&low,&high);
		for(i=0;i<n;i++){
			fscanf(fin,"%d",&arr[i]);
		}
		for(i=low;i<=high;i++){
			for(j=0;j<n;j++){
				if( i % arr[j] == 0 || arr[j] % i == 0 ){
				} else{
					break;
				}
			}
			if(j == n){
				break;
			}
		}
		if(i == high + 1){
			fprintf(fout, "NO\n");
		} else{
			fprintf(fout, "%d\n",i);
		}
	}
	fcloseall();
}