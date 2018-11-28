#include <stdio.h>

int abs(int n){
	if (n >= 0) return n;
	else return -n;
}

int main(){
	FILE* input;
	FILE* output;
	input = fopen("D.in", "r");
	output = fopen("D.out", "w+");
	int t;
	fscanf(input, "%d", &t);
	for(int c = 0; c < t; c++){
		int n;
		fscanf(input, "%d", &n);
		int l[n+1];
		bool v[n+1];
		for(int i = 1; i <= n; i++){
			fscanf(input, "%d", &l[i]);
			v[i] = false;
		}
		int p = 0;
		for(int i = 1; i <= n; i++){
			if (!v[i]){
				int temp = i, m = 0;
				while(!v[temp]){
					v[temp] = true;
					temp = l[temp];
					m++;
				}
				p += m == 1 ? 0 : m;
			}
		}
		fprintf(output, "Case #%d: %.6f\n", c + 1, p * 1.0);
	}
	fclose(input);
	fclose(output);
	return 0;
}		
