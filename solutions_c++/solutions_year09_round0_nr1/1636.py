
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef long long LL;
typedef unsigned long long ULL;

int main() {
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);

	char words[D][L+1];
	for(int d=0; d<D; d++) {
		scanf("%s",words[d]);
	}

	char exp[L*100];
	for( int n=0; n<N; n++ ) {
		scanf("%s",exp);

		int wc = 0;
		for(int d=0; d<D; d++) {
			int ei=0;
			int l=0;
			for(; l<L && exp[ei]!=0; l++) {
				if(exp[ei]=='(') {
					int eq=0;
					while(exp[++ei]!=')') {
						if(exp[ei]==words[d][l]) {
							eq=1;
						}
					}
					if(!eq) {
						break;
					}
				} else {
					if(exp[ei]!=words[d][l]){
						break;
					}
				}
				ei++;
			}
			if(l==L){
				wc++;
			}
		}

		printf("Case #%d: %d\n",n+1,wc);
	}

	return 0;
}

