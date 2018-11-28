#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct __snapper{
	int power;
	int state;
	int next; // flag which indicates turn on or off the snapper at the end of snapping
}snapper;

void snap(snapper *sp,int n_sp){
	int i;

	// for debugging
//	for(i=0;i<n_sp;i++)printf("%d ",sp[i].state);printf("\n");

	// change state
	for(i=0;i<n_sp;i++)
		if(sp[i].power) sp[i].state = sp[i].state ? 0 :	1;

	// reconsist power flag
	for(i=0;i<n_sp;i++){
		if(i==0){
				sp[0].power = 1;
				continue;
		}
		if(sp[i-1].power && sp[i-1].state){
			sp[i].power = 1;
		}else{
			sp[i].power = 0;
			break;
		}
	}
	for(i++;i<n_sp;i++) sp[i].power = 0;

	// for debugging
//	for(i=0;i<n_sp;i++)printf("%d ",sp[i].state);printf("\n");
}

int main(int a, char** b){
	char linebuff[256];
	int i,T,N;
	long long int j,K;
	fgets(linebuff,256,stdin);
	sscanf(linebuff,"%d",&T);
//	printf("T = %d\n",T);
	for(i=0;i<T;i++){
		fgets(linebuff,256,stdin);
		sscanf(linebuff,"%d %lld",&N,&K);
//		printf("N = %d K = %lld\n",N,K);
		snapper *psp = (snapper *)malloc(sizeof(snapper)* N);
		memset(psp,0,sizeof(snapper)* N);
		psp[0].power = 1;

		for(j=0;j<K;j++)
			snap(psp,N);
//		printf("psp[%d].state = %d, power = %d\n",N-1,psp[N-1].state, psp[N-1].power);
		printf("Case #%d: %s\n",i+1,(psp[N-1].state && psp[N-1].power)?"ON":"OFF");
		free(psp);
	}
	return 0;
}