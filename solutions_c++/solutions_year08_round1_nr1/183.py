#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
const int c=800;
int kd,n;
long long ans;
int x[c+1],y[c+1];
int main() {
	int ii,i;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&kd);
	for (ii=1; ii<=kd; ++ii) {
		scanf("%d",&n);
		for (i=0; i<n; ++i) scanf("%d",&x[i]);
		for (i=0; i<n; ++i) scanf("%d",&y[i]);
		sort(&x[0],&x[n]);
		sort(&y[0],&y[n]);
		ans=0;
		for (i=0; i<n; ++i) ans+=long long(x[i])*y[n-i-1];
		printf("Case #%d: %I64d\n",ii,ans);
	}
	return 0;
}
