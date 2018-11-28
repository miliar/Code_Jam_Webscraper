#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define two(n) (1<<(n))

int TT,R,K,N;
int grupos[1024];
pair<int,int> prox[1024];
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		scanf("%d %d %d",&R,&K,&N);
		for(int i=0;i<N;i++)
			scanf("%d",grupos+i);
		for(int i=0;i<N;i++) {
			long long soma=0;
			int j;
			for(j=i;j!=i or soma==0;j=(j+1)%N) {
				if(soma+grupos[j]>K)
					break;
				soma+=grupos[j];
			}
			prox[i]=make_pair(j,(int)soma);
		}
		int p=0;
		long long euros=0;
		for(int i=0;i<R;i++) {
			euros+=prox[p].second;
			p=prox[p].first;
		}
		printf("Case #%d: %lld\n",T,euros);
	}

	return 0;
}
