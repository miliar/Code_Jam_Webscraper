#include<stdio.h>
int main(){
	int t,n,data[1001],sum,c,sum2,min;
	FILE *fo=fopen("c.in","r");
	FILE *fp=fopen("c.out","w");
	fscanf(fo,"%d",&t);
	for(int casen=1;casen<=t;casen++){
		fscanf(fo,"%d",&n);
		sum=0;
		sum2=0;
		min=10000000;
		for(int i=0;i<n;i++){
			fscanf(fo,"%d",&data[i]);
			sum= (sum|data[i])-(sum&data[i]);
			sum2+=data[i];
			if(min>data[i]) min=data[i];

		}
		if(sum!=0){
			fprintf(fp,"Case #%d: NO\n",casen);
		}
		else{
			fprintf(fp,"Case #%d: %d\n",casen,sum2-min);
		}
	}

	
}