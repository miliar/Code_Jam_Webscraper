#include <stdio.h>

int main(){
	FILE* input;
	FILE* output;
	input = fopen("a.in", "r");
	output = fopen("a.out", "w+");
	int t;
	fscanf(input, "%d", &t);
	for(int c = 0; c < t; c++){
		int n;
		fscanf(input, "%d", &n);
		char table[n][n];
		int win[n], aga[n];
		for(int i = 0; i < n; i++){
			win[i] = 0;
			aga[i] = n;
			fscanf(input, "%s\n", table[i]);
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if (table[i][j] == '1'){
					win[i]++;
				}else if (table[i][j] == '.'){
					aga[i]--;
				}
			}
		}
		double wp[n], owp[n], oowp[n];
		for(int i = 0; i < n; i++){
			wp[i] = win[i] * 1.0 / aga[i];
		}
		for(int i = 0; i < n; i++){
			owp[i] = 0;
			for(int j = 0; j < n; j++){
				if (table[i][j] != '.'){
					owp[i] += (win[j] - (table[j][i] == '1')) * 1.0 / (aga[j] - 1);
				}
			}
			owp[i] /= aga[i] * 1.0;
		}
		for(int i = 0; i < n; i++){
			oowp[i] = 0;
			for(int j = 0; j < n; j++){
				if (table[i][j] != '.'){
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= aga[i] * 1.0;
		}
		fprintf(output, "Case #%d:\n", c + 1);
		for(int i = 0; i < n; i++){
			fprintf(output, "%.10f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	fclose(input);
	fclose(output);
	return 0;
}
