#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

long long sub[1000005];
long long a[1000005];
int main () {
	freopen ("B-large.in","r",stdin);
	freopen ("b-large.out","w",stdout);
	int t;
	scanf ("%d",&t);
	for (int ca=1;ca<=t;ca++) {
		long long L,t,n,C;
		scanf ("%lld%lld%lld%lld",&L,&t,&n,&C);
		for (int i=0;i<C;i++) {
			scanf ("%lld",&a[i]);
		}
		long long sum =0 ;
		for (int i=0;i<n;i++) {
			sum+=a[i%C]*2;
		}
		long long cnt=0;
		bool flag = 0;
		for (int i=0;i<n;i++) {
			if (flag==1) {
				sub[i] = a[i%C];
				continue;
			}
			if (cnt+a[i%C]*2<=t) {
				cnt+=a[i%C]*2;
				sub[i] = 0;
				continue;
			}
			long long tmp = t-cnt;
			tmp += a[i%C]-tmp/2;
			sub[i] = a[i%C]*2-tmp;
			flag = 1;
		}
		sort (sub,sub+n);
		long long ans = 0;
		for (int i=n-1;i>=n-L;i--) {
			ans += sub[i];
		}
		printf ("Case #%d: %lld\n",ca,sum-ans);		
	}			
	return 0;
}
