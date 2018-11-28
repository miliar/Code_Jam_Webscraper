#include <stdio.h>

int gcd(int a, int b){
	if (b){
		return gcd(b, a%b);
	}else return a;
}

int main(){
	FILE* input;
	FILE* output;
	input = fopen("A.in", "r");
	output = fopen("A.out", "w+");
	int t;
	fscanf(input, "%d", &t);
	for(int c = 0; c < t; c++){
		int n, d, g;
		fscanf(input, "%d", &n);
		fscanf(input, "%d", &d);
		fscanf(input, "%d", &g);
		fprintf(output, "Case #%d: ", c + 1);
		if (d == 100 && g == 100){
			fprintf(output, "Possible\n");
		}else if (d != 0 && g == 0){
			fprintf(output, "Broken\n");
		}else if ((d / gcd(100, d)) <= n && (100 / gcd(100, d)) <= n && g < 100){
			fprintf(output, "Possible\n");
		}else fprintf(output, "Broken\n");
	}
	
	fclose(input);
	fclose(output);
	return 0;
}
