#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(void){
	int T, N, S, p;
	int j;
	
	FILE *in = fopen("in", "r");
	FILE *out = fopen("out", "w");
	
	fscanf(in, "%d", &T);
	
	for(int i=0; i<T; i++){
		int t[105];
		int res = 0;
		
		fscanf(in, "%d %d %d", &N, &S, &p);
		
		memset(t, 0, sizeof(t));
		
		for(j=0; j<N; j++){
			fscanf(in, "%d", t+j);
		}
		
		sort(t, t+N);
		
		if(p>0){
			for(j=N-1; j>=0 && t[j]>=2; j--){
				if((t[j]+2)/p/3){
					res++;
				}else{
					break;
				}
			}
			
			for(int k=0; k<S && j-k>=0 && t[j-k] >= 2; k++){
				if((t[j-k]+4)/p/3){
					res++;
				}else{
					break;
				}
			}
		}else{
			res = N;
		}

		
		fprintf(out, "Case #%d: %d\n", i+1, res);
	}
	
	return 0;
}
