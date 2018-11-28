#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int tt,n;

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d",&n);
		int ans=0;
		for (int i=1;i<=n;++i) {
			int x;
			scanf("%d",&x);
			ans+=x!=i;
		}
		printf("Case #%d: %d.000000\n",ii,ans);
	}
}
