#include <cstdio>
#include <algorithm>
using namespace std;
int a[1001];
int r, k, n, j;
void sim(int &p, long long &e){
	int i, kk = k;
	for(i=0; i<n; ++i){
		if(a[p] > kk)
			break;
		kk -= a[p];
		e += a[p];
		p = (p+1) % n;
	}
}
int main(){
	int t, i;
	scanf("%d", &t);
	for(i=0; i<t; ++i){
		scanf("%d %d %d", &r, &k, &n);
		for(j=0; j<n; ++j)
			scanf("%lld", &a[j]);
		long long e = 0, ee = 0;
		int b = min(r, n);
		int p = 0, pp;
		for(j=0; j<b; ++j)
			sim(p, e);
		r -= b;
		if(r > n){
			pp = p;
			for(j=0; j<r; ++j){
				sim(p, ee);
				if(pp == p)
					break;
			}
			e += (r / (j+1)) * ee;
			r %= (j+1);
		}
		for(j=0; j<r; ++j)
			sim(p, e);
		printf("Case #%d: %lld\n", i+1, e);
	}
}
