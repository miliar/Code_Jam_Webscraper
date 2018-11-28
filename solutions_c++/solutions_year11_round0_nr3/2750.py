#include <cstdio>
#include <algorithm>
using namespace std;

int val[20];

int main() {
	int N,T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t) {
		scanf("%d",&N);
		long long total = 0;
		for(int a=0;a<N;++a) {
			scanf("%d",&val[a]);
			total += val[a];
		}
		long long res = 0;
		for(int a=1;a<(1<<N);++a) {
			long long tmp = 0;
			long long x = 0,y=0;
			for(int b=0;b<N;++b) {
				if(((1<<b)&a) > 0) {
					tmp += val[N-1-b];
					x ^= val[b];
				}
				else {
					y ^= val[b];
				}
			}
			if(x==y && tmp != total) res = max(res,tmp);
		}
		printf("Case #%d: ",t);
		if(res == 0) printf("NO\n");
		else printf("%lld\n",res);
	}
	return 0;
}
