#include <stdio.h>
#include <string.h>
#include <assert.h>

int L, D, N, P[20][300];
char W[6000][20], s[1000000];

int main(){
	scanf("%d %d %d",&L,&D,&N);
	for (int i=0; i<D; i++) scanf("%s",W[i]);
	for (int i=0; i<N; i++){
		scanf("%s",s);
		memset(P,0,sizeof(P));
		for (int j=0,k=0,o=0; s[j]; j++){
			switch (s[j]){
				case '(': assert(!o); o = 1; break;
				case ')': assert(o); o = 0; k++; break;
				default : P[k][(int)s[j]] = 1; if (!o) k++;
			}
		}
		int K = 0;
		for (int j=0; j<D; j++){
			for (int k=0; W[j][k]; k++)
				if (!P[k][(int)W[j][k]]) goto skip;
			K++;
			skip:;
		}
		printf("Case #%d: %d\n",i+1,K);
	}
}
