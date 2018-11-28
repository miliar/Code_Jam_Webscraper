#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cassert>
#include <cmath>
using namespace std;
int P[2005], H[2005], N;
int peak(int x) {
	int cp = x+1;
	for(int i=x+2;i<=N;++i) {
		if((long long)(H[i]-H[x])*(cp-x) > (long long)(H[cp]-H[x])*(i-x))
			cp = i;
	}
	return cp;
}
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		scanf("%d",&N);
		memset(H,0,sizeof(H));
		bool imp = 0;
		for(int i=1;i<N;++i)
			scanf("%d",&P[i]);
		for(int i=N-1;i>=1;--i) {
			for(int j=i+1;j<P[i];++j)
				if(P[j] > P[i]) {
					imp = 1;
					goto end;
				}
		}
		for(int i=N-1;i>=1;--i) {
			for(;;) {
				bool bad = 0;
				for(int j=i;j<N;++j)
					while(peak(j) != P[j]) {
						for(int k=P[j];k<=N;++k)
							++H[k];
						bad = 1;
						break;
					}
				if(!bad) break;
			}
		}
		end:;
		printf("Case #%d:",cn);
		if(imp) printf(" Impossible\n");
		else {
			for(int i=1;i<N;++i) assert(peak(i) == P[i]);
			for(int i=1;i<=N;++i) printf(" %d",H[i]);
			printf("\n");
		}
	}
}
