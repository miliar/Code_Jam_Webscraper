#include <stdio.h>

int main(){
	FILE* input, *output;
	input = fopen("a.in", "r");
	output = fopen("a.out", "w+");
	
	int t;
	fscanf(input, "%d", &t);
	for(int c = 0; c < t; c++){
		int n, m, nb = 0;
		fscanf(input, "%d", &n);
		fscanf(input, "%d\n", &m);
		char table[n][m], temp;
		bool poss = true;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				fscanf(input, "%c", &table[i][j]);
				if (table[i][j] == '#') nb++;
			}
			fscanf(input, "%c", &temp);
		}
		for(int i = 0; i < n - 1 && poss; i++){
			for(int j = 0; j < m - 1 && poss; j++){
				if (table[i][j] == '#'){
					if (table[i+1][j] == '#' && table[i][j+1] == '#' && table[i+1][j+1] == '#'){
						table[i][j] = '/';
						table[i+1][j] = '\\';
						table[i][j+1] = '\\';
						table[i+1][j+1] = '/';
						nb -= 4;
					}
				}
			}
		}
		fprintf(output, "Case #%d:\n", c + 1);
		if (!nb){
			for(int i = 0; i < n; i++){
				for(int j = 0; j < m; j++){
					fprintf(output, "%c", table[i][j]);
				}
				fprintf(output, "\n");
			}
		}else fprintf(output, "Impossible\n");
	}
	fclose(input);
	fclose(output);
	return 0;
}
