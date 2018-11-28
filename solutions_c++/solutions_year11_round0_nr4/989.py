#include "cstdio"
#include "vector"

using namespace std;

int main(){
	
	int t, n, x;
	float sum;
	FILE *input = fopen ("D-large.in","r");
	FILE *output = fopen ("outlarge","w");

	fscanf(input,"%d",&t);
	for (int i=1; i<=t; i++){	

		sum=0;
		fscanf(input,"%d",&n);
		for (int j=1; j<=n; j++){	
			fscanf(input,"%d",&x);
			if(x!=j) sum++;
		}

		fprintf(output,"Case #%d: %.6f\n",i,sum);
	}
	return 0;
}