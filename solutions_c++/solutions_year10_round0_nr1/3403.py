#include <stdio.h>
#include <stdlib.h>

// macro
#define IN_FILENAME "A-large.in"
#define OUT_FILENAME "output.txt"

// function prototype
void success(int n,FILE *fp);
void failed(int n,FILE *fp);

/////////
// main
/////////
int main(){
	FILE *ifp,*ofp;
	int t,k;
	int i;
	// input from in_file
	int T;
	int N,K;


	if((ifp=fopen(IN_FILENAME,"r"))==NULL){
		fprintf(stderr,"infile error!\n");
		exit(EXIT_FAILURE);
	}
	if((ofp=fopen(OUT_FILENAME,"w"))==NULL){
		fprintf(stderr,"outfile error!\n");
		exit(EXIT_FAILURE);
	}

	fscanf(ifp,"%d",&T);
	printf("the number of case: %d\n\n",T);

	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		fscanf(ifp, "%d %d",&N,&K);
		printf("%d %d\n",N,K);
		// Kmax=10^8は2進数で27桁 -> only if the number of chain is less than 26
		if(N>27){
			failed(t,ofp);
		}else{
			k=K;
			for(i=0;i<N;i++){
				if(k%2==1){ // 奇数だったら最下位ビットが1
					k = k >> 1;
				}else{
					break;
				}
			}
			if(i==N){
				success(t,ofp);
			}else{
				failed(t,ofp);
			}
		}
	}

	fclose(ifp);
	fclose(ofp);
	return 0;
}


// other function
void success(int n, FILE *fp){
	fprintf(fp,"Case #%d: ON\n",n);
	printf("Case #%d: ON\n",n);
}

void failed(int n, FILE *fp){
	fprintf(fp,"Case #%d: OFF\n",n);
	printf("Case #%d: OFF\n",n);
}