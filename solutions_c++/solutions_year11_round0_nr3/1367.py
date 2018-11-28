#include <stdio.h>

int abs(int n){
	if (n >= 0) return n;
	else return -n;
}

int main(){
	FILE* input;
	FILE* output;
	input = fopen("C.in", "r");
	output = fopen("C.out", "w+");
	int t;
	fscanf(input, "%d", &t);
	for(int c = 0; c < t; c++){
		int n;
		fscanf(input, "%d", &n);
		int x = 0, min = 9000000, sum = 0, temp;
		for(int i = 0; i < n; i++){
			fscanf(input, "%d", &temp);
			sum += temp;
			x ^= temp;
			if (temp < min){
				min = temp;
			}
		}
		if (x){
			fprintf(output, "Case #%d: NO\n", c + 1);
		}else{
			fprintf(output, "Case #%d: %d\n", c + 1, sum - min);
		}
	}	
	fclose(input);
	fclose(output);
	return 0;
}		
