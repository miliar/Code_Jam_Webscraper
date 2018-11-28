#include<stdio.h>

int main(void){
	int N, K, T;
	int cnt;
	FILE * input =  fopen("A-large.in", "r");
	FILE * output = fopen("A-large.out", "w");
	fscanf(input, "%d", &T);
	cnt = T;
	while(cnt--){
		int onValue;
		fscanf(input, "%d", &N);
		fscanf(input, "%d", &K);
		onValue = (1<<N) - 1;
		K = K % (onValue+1);

		//ouput
		fprintf(output, "Case #%d: ", T-cnt);
		if( K == onValue ){
			fprintf(output, "ON\n");
		}
		else{
			fprintf(output, "OFF\n");
		}
	}
	return 0;
}
