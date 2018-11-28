#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
using namespace std;

int main() {
	int C, N, M, A;
	bool prim[10000];
	int prims[1300];
	int P=0;
	memset(prim, true, sizeof(prim));
	prim[0]=prim[1]=false;
	for(int p=2;p<10000;++p)
		if(prim[p]) {
			prims[P++]=p;
			for(int i=2*p;i<10000;i+=p)
				prim[i]=false;
		}
	scanf("%d",&C);
	for(int c=0;c<C;++c) {
		bool done = false;
		scanf("%d%d%d",&N,&M,&A);
		printf("Case #%d: ",c+1);
		fflush(stdout);
		for(int x1=0;x1<=N && !done;++x1) {
			for(int y1=0;y1<=M && !done;++y1) {
				for(int x2=0;x2<=N && !done; ++x2) {
					for(int y2=0;y2<M && !done; ++y2) {
						if(abs(x1*y2-x2*y1)==A) {
							done=true;
							printf("0 0 %d %d %d %d",x1,y1,x2,y2);
						}
					}
				}
				/*if(x1==0 && y1==0)
					continue;
				int prod=A+x1*y1;
				if(N*M<prod)
					continue;
				int pc=prod;
				for(int p=0;p<P && prims[p]<min(N,M);++p)
					while(pc%prims[p]==0)
						pc/=prims[p];
				if(pc<=max(N,M)) {
					for(int x2=(x1==0?1:x1);x2<=N && !done;++x2)
						if(prod%x2==0 && prod/x2<=M && abs(x1*prod/x2-y1*x2)==A) {
							printf("0 0 %d %d %d %d",x1,y1,x2,prod/x2);
							assert(abs(x1*prod/x2-y1*x2)==A);
							done=true;
						}
				}*/
			}
		}
		if(!done)
			printf("IMPOSSIBLE");
		printf("\n");
	}
}