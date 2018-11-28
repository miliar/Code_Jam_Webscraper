#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

const int maxn = 210;
const long double eps = 1e-15;

int p[maxn], v[maxn];
long long n,d;

bool good(long double t){
	long double maxr = p[0] - t;
	for (int i = 0 ; i < n ; i++){
		maxr = max(maxr, p[i] - t );
		if (maxr < eps + p[i] + t && p[i] + t - max(maxr, p[i] - t) + eps > (v[i] - 1) * d){
			maxr += v[i] * d;
		} else {
			return false;
		}
	}
	return true;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int k;
	scanf("%d",&k);
	for (int i = 1 ; i <= k ; i++){
		printf("Case #%d: ", i);
		scanf("%lld%lld",&n, &d);
		for (int j = 0 ; j < n ; j++){
			scanf("%d%d",&p[j],&v[j]);
		}
		long double l = 0.0, r = 1e15, res = -1.0;
		for (int j = 0 ; j < 200 ; j++){
			long double t = (l + r) / 2.0;
			if (good(t)){
				res  = t;
				r = t;
			} else {
				l = t;
			}
		}
		printf("%.1Lf\n",res);
	}
	return 0;
}