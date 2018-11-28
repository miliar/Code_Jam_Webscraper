#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
//long long small[1005], big[1005];
bool isp[1000005];
long long P[1000005];
int pi = 0;
int main() {
	memset(isp,1,sizeof(isp));
	isp[0] = isp[1] = 0;
	for(int i=2;i<=1000000;++i)
		if(isp[i])
			for(int j=i+i;j<=1000000;j+=i)
				isp[j] = 0;
	for(int i=2;i<=1000000;++i)
		if(isp[i]) P[pi++] = i;
	/*
	small[1] = 0; big[1] = 1;
	for(int n=2;n<=1000;++n) {
		small[n] = small[n-1];
		big[n] = big[n-1];
		if(isp[n]) ++small[n];
		for(int i=2;i<=n;++i)
			if(isp[i]) {
				// check if n = i^k
				int v = 1;
				for(int k=1;k<=9;++k) {
					v *= i;
					if(v == n) goto end;
					if(v > n) break;
				}
			}
		continue;
		end:;
		++big[n];
	}
	small[1] = 1;
	*/
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		long long N;
		scanf("%lld",&N);
		if(N == 1) {
			printf("Case #%d: 0\n",cn);
			continue;
		}
		long long ans = 1;
		for(int i=0;i<pi;++i) {
			if(P[i]*P[i] > N) break;
			long long k = P[i]*P[i];
			while(k <= N) {
				++ans;
				k *= P[i];
			}
		}
		printf("Case #%d: %lld\n",cn,ans);
	}
}
