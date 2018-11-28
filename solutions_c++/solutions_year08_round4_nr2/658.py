#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	int icase, ncase;
	int N, M, A;
	int ok;
	int i, j, k, l, m;
	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		scanf("%d%d%d", &N, &M, &A);
		ok = 0;
		for(i=0; i<=N; ++i){
			for(j=0; j<=N; ++j){
				for(k=0; k<=M; ++k){
					for(l=0; l<=N; ++l){
						for(m=0; m<=M; ++m){
							if(i*k+j*m-k*l-i*m == A){
								ok = 1;
								goto OUT;
							}
						}
					}
				}	
			}
		}
OUT:
		printf("Case #%d: ", icase+1);
		if(ok)
			printf("%d %d %d %d %d %d\n", i, 0, j, k, l, m);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
