#include <stdio.h>

int abs(int n){
	if (n >= 0) return n;
	else return -n;
}

int main(){
	FILE* input;
	FILE* output;
	input = fopen("A-large.in", "r");
	output = fopen("A-large.out", "w+");
	int t;
	fscanf(input, "%d", &t);
	for(int c = 0; c < t; c++){
		int n;
		fscanf(input, "%d", &n);
		int o[n], b[n], po = 0, pb = 0;
		bool iso[n];
		char temp;
		int tenp;
		for(int i = 0; i < n; i++){
			fscanf(input, " %c", &temp);
			fscanf(input, "%d", &tenp);
			iso[i] = temp == 'O';
			if (iso[i]){
				o[po++] = tenp;
			}else{
				b[pb++] = tenp;
			}
		}
		int op = 0, bp = 0, co = 1, cb = 1, time = 0, opathd, bpathd;
		for(int i = 0; i < n; i++){
			if (iso[i]){
				if (pb == 0){
					bpathd = cb;
				}else bpathd = b[bp] - cb;
				opathd = o[op] - co;
				if (abs(opathd) + 1 >= abs(bpathd)){
					cb += bpathd;
				}else{
					if (bpathd > 0){
						cb += abs(opathd) + 1;
					}else{
						cb -= abs(opathd) + 1;
					}
				}
				time += abs(opathd) + 1;
				co = o[op++];
			}else{
				if (po == 0){
					opathd = co;
				}else opathd = o[op] - co;
				bpathd = b[bp] - cb;
				if (abs(bpathd) + 1 >= abs(opathd)){
					co += opathd;
				}else{
					if (opathd > 0){
						co += abs(bpathd) + 1;
					}else{
						co -= abs(bpathd) + 1;
					}
				}
				time += abs(bpathd) + 1;
				cb = b[bp++];
			}
		}
		fprintf(output, "Case #%d: %d\n", c + 1, time);
	}
	fclose(input);
	fclose(output);
	return 0;
}		
