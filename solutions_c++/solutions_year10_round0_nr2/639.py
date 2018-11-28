#include <stdio.h>
#include <string.h>
#include <set>
#include <algorithm>
using std::set;

int n;
long long num[1010];
long long rem[1010];

long long GCD(long long a,long long b) {
	if(b == 0)	return a;
	return GCD(b,a%b);
}

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		set<long long> Q;
		for(int i=0;i<n;i++) {
			long long k;
			scanf("%lld",&k);
			Q.insert(k);
		}
		n = 0;
		for(set<long long >::iterator it=Q.begin();it!=Q.end();it++)
			num[n++] = (*it);
		
		/*if(n == 2) {
			printf("Case #%d: %lld\n",++c, num[1]-num[0]);
			continue;
		}*/
		
		for(int i=1;i<n;i++)
			rem[i] = num[i]-num[i-1];
		long long ans = rem[1];
		for(int i=2;i<n;i++)
			ans = GCD(ans,rem[i]);
		//printf("%d\n",ans);
		if(num[0]%ans == 0)	ans = 0;
		else	ans = ans-(num[0]%ans);
		printf("Case #%d: %lld\n",++c,ans);
	}
	
	return 0;
}
