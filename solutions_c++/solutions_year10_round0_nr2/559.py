#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

inline long long gcd(long long a,long long b) {
	while(b) {
		long long r=a%b;
		a=b;
		b=r;
	}
	return a;
}

#define MAX 1100

long long T[MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%lld",&T[i]);
		long long d=0;
		for(int i=0;i<n;++i)
			for(int j=i+1;j<n;++j)
				d=gcd(d,abs(T[i]-T[j]));
		long long ans=T[0]%d;
		if(ans) ans=d-ans;
		printf("Case #%d: %lld\n",test,ans);
	}
	return 0;
}
