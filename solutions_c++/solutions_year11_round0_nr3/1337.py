#include <iostream>
#include <cstdio>
#include <cstdlib>
#define inf 1000000000

using namespace std;

int n,tt;
int a[1010];

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d",&n);
		int cur=0,mini=inf,sum=0;
		for (int i=1;i<=n;++i) {
			scanf("%d",&a[i]);
			cur^=a[i];
			mini=min(a[i],mini);
			sum+=a[i];
		}
		if (cur==0) printf("Case #%d: %d\n",ii,sum-mini);
		else printf("Case #%d: NO\n",ii);
	}
}
