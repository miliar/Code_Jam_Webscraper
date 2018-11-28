#include <iostream>
#include <cstdlib>
#include <algorithm>
#define maxn 10001

using namespace std;

struct point {
	int x,y;
};

bool comp(point a,point b) {
	if (a.x<b.x) return true;
	else return false;
}

int ii,tt,i,j,n,cnt;
point a[maxn];

int main() {
	freopen("rope.in","r",stdin);
	freopen("rope.out","w",stdout);

	scanf("%d\n",&tt);
	for (ii=1;ii<=tt;++ii) {
		scanf("%d\n",&n);
		for (i=1;i<=n;++i)
			scanf("%d%d\n",&a[i].x,&a[i].y);

		sort(a+1,a+n+1,comp);

		cnt=0;
		for (i=2;i<=n;++i)
			for (j=1;j<n;++j)
				if (a[j].y>a[i].y) cnt++;
		printf("Case #%d: %d\n",ii,cnt);
	}
}
