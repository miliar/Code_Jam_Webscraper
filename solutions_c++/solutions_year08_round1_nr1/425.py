#include <cstdio>
#include <algorithm>
using namespace std;

int T,TT,N;
long long vetor[2][800];
int main(void) {
	TT=1;
	for(scanf("%d",&T);T--;TT++) {
		scanf("%d",&N);
		for(int j=0;j<2;j++)
			for(int i=0;i<N;i++)
				scanf("%lld",&vetor[j][i]);
		sort(vetor[0],vetor[0]+N);
		sort(vetor[1],vetor[1]+N);
		long long ans=0;
		for(int i=0;i<N;i++) {
			ans+=vetor[0][i]*vetor[1][N-i-1];
		}
		printf("Case #%d: %lld\n",TT,ans);

	}
	return 0;
}
