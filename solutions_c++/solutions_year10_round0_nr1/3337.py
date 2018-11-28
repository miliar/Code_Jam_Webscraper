#include <cstdio>
#include <cstdlib>

using namespace std;
int main(){
	//int pw2[31] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824};
	int pw2[31];
	pw2[0] = 1;
	for(int i = 1; i < 31; i++){
		pw2[i] = pw2[i-1] << 1;
	}
	FILE *file = fopen("large.txt", "r"), *out = fopen("lout.txt", "w");
	int c = 0, cases = 0;
	fscanf(file, "%d", &cases);
	while(c++ < cases){
		int n = 0, k = 0;
		fscanf(file, "%d %d", &n, &k);
		if(k > 0){
			int lim = 0;
			for(int i = 0; i < n; i++) lim += pw2[i];
			//printf("%d\n", lim);
			bool go = false;
			for(int i = lim+1; i-1 <= k; i+=lim+1){
				go = (i-1 == k)? true: false;
			}
			if(go){
				fprintf(out, "Case #%d: ON\n", c);				
			}else{
				fprintf(out, "Case #%d: OFF\n", c);
			}
		}else{
			fprintf(out, "Case #%d: OFF\n", c);
		}
	}
	return 0;
}