#include <stdio.h>
#include <memory.h>
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");

int T,n,no;
int data[1001];

int main(){
	int i,j,k,min,sum;
	fscanf(in,"%d",&T);
	for(k=0;k<T;k++){
		fscanf(in,"%d",&n);
		min=0x7fffffff;no=0;sum=0;
		for(i=0;i<n;i++){
			fscanf(in,"%d",&data[i]);
			min=min>data[i]?data[i]:min;
			sum+=data[i];
			no=no^data[i];
		}
		if(no!=0){
			fprintf(out,"Case #%d: NO\n",k+1);
			continue;
		}
		fprintf(out,"Case #%d: %d\n",k+1,sum-min);
	}
	return 0;
}
