#include <stdio.h>
#include <stdlib.h>

#define INFILE "C-small-attempt0.in"
#define OUTFILE "output.txt"

int main(){
	FILE *ifp,*ofp;
	int i,j,ii,jj;
	int front,rear;
	int rider,income,check_sum;
	// from input file
	int T,R,k,N;
	int *g;

	if((ifp=fopen(INFILE,"r"))==NULL){
		fprintf(stderr,"infile error!\n");
		exit(EXIT_FAILURE);
	}
	if((ofp=fopen(OUTFILE,"w"))==NULL){
		fprintf(stderr,"outfile error!\n");
		exit(EXIT_FAILURE);
	}

	
	fscanf(ifp,"%d",&T);
	printf("the number of case: %d\n",T);
	for(i=1;i<=T;i++){
		// read
		fscanf(ifp,"%d %d %d",&R,&k,&N);
		printf("%d %d %d\n",R,k,N);
		g = (int *)calloc(N+1,sizeof(int));
		for(j=1;j<=N;j++){
			fscanf(ifp,"%d",&g[j]);
			printf("%d ",g[j]);
		}
		printf("\n");

		// initialize
		front = 1;
		rear = N;
		income = 0;

		// ˆ—
		for(j=1;j<=R;j++){
			// check
			check_sum=0;
			for(ii=1;ii<=N;ii++){
				check_sum += g[ii];
			}
			if(check_sum<=k){
				income = check_sum*R;
				break;
			}

			//–{”Ô
			rider=0;
			do{
				rider += g[front];
				if(front==N){
					front = 1;
				}else{
					front++;
				}
			}while(rider<=k && front-1!=rear);
			if(front==1){
				front = N;
			}else{
				front--;
			}
			rider -= g[front];
			income += rider;
			if(front==1){
				rear = N;
			}else{
				rear = front - 1;
			}
		}
		fprintf(ofp,"Case #%d: %d\n",i,income);

		free(g);
	}

	fclose(ifp);
	fclose(ofp);

	return 0;
}