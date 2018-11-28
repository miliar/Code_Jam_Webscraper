#include "cstdio"

int main(){
	int t, n, min, x_sum, sum, x;
	FILE *input = fopen ("C-large.in","r");
	FILE *output = fopen ("outlarge","w");	
	
	fscanf(input,"%d",&t);
	for (int i=1; i<=t; i++){	
		
		fscanf(input,"%d",&n);
		sum=0;
		x_sum=0;
		min=100000000;

		for (int j=1; j<=n; j++){	
			fscanf(input,"%d",&x);
			if(x<min) min=x;
			x_sum ^= x;
			sum +=x;
		}

		sum-=min;
		if(x_sum != 0) fprintf(output,"Case #%d: NO\n",i);
		else fprintf(output,"Case #%d: %d\n",i,sum);
	}
	return 0;
}