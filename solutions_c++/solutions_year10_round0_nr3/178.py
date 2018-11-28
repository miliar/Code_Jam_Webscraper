#include<stdio.h>
#define fast

int D[2005], tmpD[2005];
long long C[2005], tmpC[2005];
long long G[2005];

int main(void)
{
	int T, cs;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		int R, k, N, i, j;
		scanf("%d%d%d",&R,&k,&N);
		for(i=0;i<N;i++){
			scanf("%I64d",&G[i]);
			D[i] = C[i] = 0;
			G[i+N] = G[i];
		}
		long long s = 0;
		for(i=j=0;i<N;i++){
			while(j<N+i && s + G[j] <= (long long)k)
				s += G[j++];
			D[i] = j%N;
			C[i] = s;
			s -= G[i];
		}
		int pos = 0;
		long long tcst = 0LL;
		while(R > 0){
#ifdef fast
			if(R%2){
				tcst += C[pos];
				pos = D[pos];
			}
			for(i=0;i<N;i++){
				tmpC[i] = C[i] + C[D[i]];
				tmpD[i] = D[D[i]];
			}
			for(i=0;i<N;i++){
				C[i] = tmpC[i];
				D[i] = tmpD[i];
			}
			R/=2;
#else
			tcst += C[pos];
			pos = D[pos];
			R--;
#endif
		}
		printf("Case #%d: %I64d\n", cs, tcst);
	}
	return 0;
}
