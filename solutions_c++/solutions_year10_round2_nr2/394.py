#include <iostream>
using namespace std;
typedef struct  
{
	int x,v;
}node;

node hash[100];
int goal[100];
int main() {
	int C;
	freopen("B1.in","r",stdin);
	freopen("B1.out","w",stdout);
	scanf("%d",&C);
	int b;
	for (b = 1; b <= C; ++b) {
		int i,j,K,B,T,N;
		scanf("%d%d%d%d",&N,&K,&B,&T);
		for (i=0;i<N;++i){
			scanf("%d", &hash[i].x);
		}
		for (i=0;i<N;++i){
			scanf("%d", &hash[i].v);
		}

		int now = 0;
		int nid = N-1;
		int ret = 0;
		for (i = N-1; i >=0; --i) {
			if (T*hash[i].v + hash[i].x >= B) {
				for (j = N-1; j >i; --j) {
					if (hash[j].v * T + hash[j].x < B) {
						++ret;
					}
				}
				++now;
				if (now == K) {
					break;
				}
			} 
		}

		printf("Case #%d: ", b);
		if (now < K) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ret);
		}
	}
	return 0;
}