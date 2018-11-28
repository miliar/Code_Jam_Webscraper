#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
	int t,n;
	long long int x[805],y[805];
	scanf("%d\n",&t);
	for(int ii=1;ii<=t;++ii) {
		scanf("%d\n",&n);
		for(int i=0;i<n;++i) scanf("%lld ",x+i);
		for(int i=0;i<n;++i) scanf("%lld ",y+i);
		sort(x,x+n);sort(y,y+n);
		long long int s = 0;
		for(int i=0;i<n;++i) s += x[i]*y[n-i-1];
		printf("Case #%d: %lld\n",ii,s);
	}
	return 0;
}
