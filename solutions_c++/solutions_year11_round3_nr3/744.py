#include <stdio.h>

int main(){
	FILE* input, *output;
	input = fopen("c.in", "r");
	output = fopen("c.out", "w+");
	
	int t;
	fscanf(input, "%d", &t);
	for(int c = 0; c < t; c++){
		int n;
		long long l;
		long long h;
		fscanf(input, "%d", &n);
		fscanf(input, "%I64d", &l);
		fscanf(input, "%I64d", &h);
		long long p[n], ans;
		for(int i = 0; i < n; i++){
			fscanf(input, "%I64d", &p[i]);
		}
		bool check;
		for(long long i = l; i <= h; i++){
			check = true;
			for(int j = 0; j < n; j++){
				if (p[j] % i && i % p[j]){
					check = false;
					break;
				}
			}
			if (check){
				ans = i;
				break;
			}
		}
		fprintf(output, "Case #%d: ", c + 1);
		if (!check){
			fprintf(output, "NO\n");
		}else fprintf(output, "%d\n", ans);
	}
	
	fclose(input);
	fclose(output);
	return 0;
}
