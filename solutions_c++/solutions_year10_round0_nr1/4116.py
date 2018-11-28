#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	FILE* in = fopen("A-large.in", "r");
	FILE* out = fopen("A-large.txt", "wb");
	int ts;
	int n, k;
	fscanf(in, "%d", &ts);
	for(int t = 0; t<ts; t++){
		fscanf(in, "%d %d", &n, &k);
		if(k < (1<<n)-1)
			fprintf(out, "Case #%d: OFF\n", t+1);
		else{		
			bool zero = false;
			for(int i = 0; i<n; i++){
				if(k%2 == 0)
				{
					zero = true;
					break;
				}
				k /= 2;
			}

			if(zero)
				fprintf(out, "Case #%d: OFF\n", t+1);
			else
				fprintf(out, "Case #%d: ON\n", t+1);
		}
	}
	fclose(in);
	fclose(out);
}
