#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define maxn 5000

using namespace std;

struct node {
	int l,r,spd;
};

node a[maxn];
int tt;

bool cmp1(const node &a,const node &b) {
	return a.l<b.l;
}

bool cmp2(const node &a,const node &b) {
	return a.spd<b.spd;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		int x,s,r,t,n;
		scanf("%d%d%d%d%d\n",&x,&s,&r,&t,&n);
		for (int i=1;i<=n;++i) scanf("%d%d%d",&a[i].l,&a[i].r,&a[i].spd);
		sort(a+1,a+n+1,cmp1);
		int last=0;
		int m=n;
		for (int i=1;i<=n;++i) {
			if (a[i].l>last) {
				++m;
				a[m].l=last;
				a[m].r=a[i].l;
				a[m].spd=0;
			}
			last=a[i].r;
		}
		if (last<x) {
			++m;
			a[m].l=last;
			a[m].r=x;
			a[m].spd=0;
		}
		n=m;
		sort(a+1,a+n+1,cmp2);
		double res=t,ans=0;
		for (int i=1;i<=n;++i) {
			if (res>0) {
				double pp=(double)(a[i].r-a[i].l)/(double)(r+a[i].spd);
				if (pp>res) {
					ans+=res;
					ans+=((double)(a[i].r-a[i].l)-res*(double)(r+a[i].spd))/(double)(s+a[i].spd);
					res=0;
				} else {
					res-=pp;
					ans+=pp;
				}
			} else ans+=(double)(a[i].r-a[i].l)/(double)(s+a[i].spd);
		}
		printf("Case #%d: %.10lf\n",ii,ans);
	}
}
