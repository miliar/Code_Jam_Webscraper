#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int A, B;
double P[104], R[104];

void ops(int x, double prod, int min){
	if(x == A){//printf("$ %d $#%lf |",min, prod);
		int i, n=0;
		n=B-A+1;
		if(min!=-1)
			n+=B+1;
		R[0]+= n*prod;//printf(" %d |",n);
		for(i=1; i<=x; i++){
			n= B-A+(i*2)+1;
			if(min!=-1){
				if(min<(A-i))
					n+=B+1;
			}//printf(" %d |",n);
			R[i]+= n*prod;
		}
		n=B+2;//printf(" %d#\n",n);
		R[i]+= n*prod;
		return;
	}
	ops(x+1, prod*P[x], min);
	ops(x+1, prod*(1-P[x]), (min==-1)? x:min);
}

int main(){
	int T,i, j;
	double min;
	scanf("%d", &T);
	for(i=1; i<=T; i++){
		scanf("%d %d", &A, &B);
		for(j=0; j<A; j++)
			scanf("%lf", &P[j]);
		memset(R, 0, sizeof(R));
		ops(0, 1, -1);
		min=(1<<30);
		for(j=0; j<=A+1; j++){//printf("|%d --> %lf|\n", j, R[j]);
			min= (R[j]<min)? R[j]:min;
		}
		printf("Case #%d: %lf\n",i,min);
	}
	return 0;
}
