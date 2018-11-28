#include<iostream>
#include<algorithm>
using namespace std;

const int maxn = 805;

int n;
int x[maxn];
int y[maxn];

int main() {
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++) {
		scanf("%d", &n);
		for(int j=0;j<n;j++) scanf("%d", &x[j]);
		for(int j=0;j<n;j++) scanf("%d", &y[j]);
		sort(x,x+n);
		sort(y,y+n);

		long long res = 0ll;
		for(int j=0;j<n;j++) {
			res += (1ll * x[j]) * y[n-1-j];
		}

		printf("Case #%d: %lld\n", i+1, res);
	}
	return 0;
}

/*
 * x1*y1+x2*y2 x1*y2+x2*y1
 * x2(y2-y1)   x1(y2-y1)
 */

