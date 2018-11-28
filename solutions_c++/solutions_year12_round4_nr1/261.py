#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int tt;
int n,D;
int d[10000],l[10000];
int f[10010];

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			scanf("%d%d",&d[i],&l[i]);

		scanf("%d",&D);
		f[0]=d[0];
		for (int i=1;i<n;++i) {
			f[i]=-1;
			for (int j=0;j<i;++j)
				if (f[j]!=-1 && f[j]>=d[i]-d[j]) f[i]=max(f[i],min(d[i]-d[j],l[i]));
		}

		bool flag=false;
		for (int i=0;i<n;++i)
			if (f[i]!=-1 && D-d[i]<=f[i]) flag=true;
		if (flag) printf("Case #%d: YES\n",ii);
		else printf("Case #%d: NO\n",ii);
	}
}
