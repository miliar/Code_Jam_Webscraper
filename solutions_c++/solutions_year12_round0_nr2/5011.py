#include <cstdio>
const int c=128;
int tt,ii,n,s,p;
int t[c];
int main() {
	scanf("%d",&tt);
	int i,ans;
	for (ii=1; ii<=tt; ++ii) {
		scanf("%d%d%d",&n,&s,&p);
		for (i=1; i<=n; ++i) scanf("%d",&t[i]);
		ans=0;
		for (i=1; i<=n; ++i) {
			t[i]-=p;
			if (t[i]<0) continue;
			if ((p-1)*2<=t[i]) ++ans; else
			if ((p-2)*2<=t[i] && s) ++ans,--s;
		}
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}
