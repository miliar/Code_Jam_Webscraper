#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=2010;

long long ret, a[maxn], k, sum[maxn];
int p[maxn], fnd[maxn];
int T, R, n;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int task = 0;
	for( scanf("%d", &T); T--; ){
		scanf("%d%d%d", &R, &k, &n);
		for (int i=0; i<n; i++){
			scanf("%d", a+i);
			a[i+n] = a[i];
		}
		for (int i=0; i<n; i++){
			sum[i] = 0; p[i] = i;
			for (int j=i, t=0; t<n; j++, t++)
			if ( sum[i]+a[j]>k ) break;else{
				sum[i] += a[j];
				p[i] = j+1; if ( p[i]>=n ) p[i] -= n;
			}
		}
		ret = 0;
		memset( fnd, 0, sizeof(fnd) );
		long long cur = 0;
		int tm = 0;
		bool fnsh = false;
		for (int o=0; R>0; )
		if ( !fnsh ){
			if ( fnd[o]==2 ){
				ret += cur*(R/tm);
				R %= tm;
				fnsh = true;
				continue;
			}else
			if ( fnd[o]==1 ){
				cur += sum[o];
				tm++;
			}
			fnd[o]++;
			ret += sum[o];
			o = p[o];
			R--;
		}else{
			ret += sum[o];
			o = p[o];
			R--;
		}
		printf("Case #%d: %lld\n", ++task, ret);
	}
	return 0;
}
