#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;

struct node {
	int l,p,idx;
};

node a[2000];
int n,tt;

bool cmp(const node &a,const node &b) {
	if (a.l*b.p!=a.p*b.l) return a.l*b.p<a.p*b.l;
	else return a.idx<b.idx;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			scanf("%d",&a[i].l);
		for (int i=0;i<n;++i)
			scanf("%d",&a[i].p);
		for (int i=0;i<n;++i) a[i].idx=i;

		sort(a,a+n,cmp);

		printf("Case #%d:",ii);
		for (int i=0;i<n;++i)
			printf(" %d",a[i].idx);
		printf("\n");
	}
}
