#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	int N, M, V, G, C, I;
	int to0[10010], to1[10010];
	int c[10010],g[10010],v[10010];
	scanf("%d",&N);
	for(int n=0;n<N;++n) {
		scanf("%d%d",&M,&V);
		for(int m=1;m<=(M-1)/2;++m)
			scanf("%d%d",&(g[m]),&(c[m]));
		for(int m=1;m<=(M+1)/2;++m) {
			scanf("%d",&I);
			if(I==0)
				to0[m+(M-1)/2]=0,to1[m+(M-1)/2]=1<<28;
			else
				to1[m+(M-1)/2]=0,to0[m+(M-1)/2]=1<<28;
		}
		for(int m=(M-1)/2;m>0;--m) {
			if(g[m]==1) { // and gate
				if(c[m]==1) { // changeable
					to0[m]=min(to0[2*m], to0[2*m+1]);
					to1[m]=min(to1[2*m]+to1[2*m+1], min(to1[2*m],to1[2*m+1])+1);
				} else { // fixed
					to0[m]=min(to0[2*m], to0[2*m+1]);
					to1[m]=to1[2*m]+to1[2*m+1];
				}
			} else { // or gate
				if(c[m]==1) { // changeable
					to0[m]=min(to0[2*m]+to0[2*m+1], min(to0[2*m],to0[2*m+1])+1);
					to1[m]=min(to1[2*m],to1[2*m+1]);
				} else { // fixed
					to0[m]=to0[2*m]+to0[2*m+1];
					to1[m]=min(to1[2*m],to1[2*m+1]);
				}
			}
			if(to0[m]>(1<<28))
				to0[m]=1<<28;
			if(to1[m]>(1<<28))
				to1[m]=1<<28;
		}
/*		for(int m=1;m<=M;++m)
			printf("(%d,%d) ",to0[m],to1[m]);
		printf("\n");*/
		printf("Case #%d: ", n+1);
		if(V==0) {
			if(to0[1]<(1<<28))
				printf("%d", to0[1]);
			else printf("IMPOSSIBLE");
		} else {
			if(to1[1]<(1<<28))
				printf("%d", to1[1]);
			else printf("IMPOSSIBLE");
		}
		printf("\n");
	}
}