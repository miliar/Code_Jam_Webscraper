#include <stdio.h>
#include <algorithm>
#include <vector>
#define MAXN 1000001
using namespace std;
long long T, N, ans;
int P[MAXN];
void sieve() {
	int i, j;
	for(i=2;i*i<MAXN;i++) { 		
		if(P[i]>0)continue;
		for(j=i*i;j<MAXN;j+=i) P[j]=i;	
	}	
}
int main() {
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	long long i, j, t, k;
	sieve();
	scanf("%lld", &T);
	for(t=0;t<T;t++) {
		scanf("%lld", &N);
		if(N==1) {
			printf("Case #%lld: 0\n",t+1);
			continue;
		}
		ans = 1;
		for(i=2;i*i<=N;i++) {
			if(P[i] == 0 ) {
				k = i;
				for(j=0;k<=N;j++) k*=i;			
				ans += j - 1;				
			}		
		}
		
		printf("Case #%lld: %lld\n",t+1, ans);
	}	
	return 0;	
}
