#include <stdio.h>



#define RMAX 1000000000
#define KMAX 1000000000
#define NMAX 100000
#define GMAX 1000000000


long long  gSizes[NMAX];
long long  gTo[NMAX];
long long  g[NMAX];
long long N,K,R;

void calculate(long long i){
	long long  iAnt = (i-1+N)%N;

	gSizes[i] = gSizes[iAnt]-g[iAnt];
	long long  indicat = 0;
	long long  h = (gTo[iAnt]+1)%N;

	if(gTo[iAnt] == iAnt) {	
		indicat = 1;
		gSizes[i]+=g[i];
		gTo[i] = i;
		h = (h+1)%N;
	}else gTo[i] = gTo[iAnt];
	
//	printf("gSZ[%d] = %d  \n",i,gSizes[i]);
	//int h;
	long long  count;
	//h = (gTo[iAnt]+1)%N;
	
	for(count = 0;(i-h)%N!=0 && gSizes[i]+g[h]<=K;h = (h+1)%N,count++){
//		indicat = 0;
//		if(h == i) {
//			continue;
//		}
		gSizes[i]+=g[h];
		gTo[i] = h;

//		printf("i: %d, h:%d  gsz:%d\n",i,h,gSizes[i]);
	}
}

int main(){
	long long  n;
	scanf("%Ld",&n);

	for(long long  i =1;i<=n;i++){
		scanf("%Ld %Ld %Ld",&R, &K, &N);

//		printf("\t\tAvaliating case %d:\n  %d %d %d\n",i,R,K,N);
		for(long long  j = 0;j<N;j++){
			scanf("%Ld",&g[j]);
//			printf("%d ",g[j]);
		}
//		printf("\n");
		for(long long  j = 0;j<NMAX;j++) gSizes[j] = 0;
		gTo[N-1] = N-1;
		gSizes[N-1] = g[N-1];
		for(long long  j = 0;j<N;j++) calculate(j);

//		for(int j=0;j<N;j++){
//			printf("\t%d: gSize = %d, gTo = %d\n",j,gSizes[j],gTo[j]);
//		}
	long long  sum = 0;
	long long  act = 0;
		for(long long  j=0;j<R;j++){
			sum+=gSizes[act];
			act = (gTo[act]+1)%N;
		}
		
//		printf("\n");


		printf("Case #%Ld: %Ld\n",i,sum);

		
	}

	return 0;
}



