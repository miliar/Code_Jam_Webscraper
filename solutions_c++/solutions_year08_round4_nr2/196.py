#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int kd,n,m,a;
int x2,y2,x3,y3;
bool ok(int a, int &x, int &y) {
	int nn=n;
	int mm=m;
	int i;
	bool q;
	if (a==0) {
		x=y=0;
		return 1;
	}
	if (a<=n) {
		x=a;
		y=1;
		return 1;
	}
	if (a<=m) {
		x=1;
		y=a;
		return 1;
	}
	if (a>n*m) return 0;
	q=0;
	if (nn>mm) {
		swap(nn,mm);
		q=1;
	}
	for (i=a/mm; i*i<=a && i<=nn; ++i) {
		if (a%i==0) {
			x=i;
			y=a/i;
			break;
		}
	}
	if (i*i<=a && i<=nn && a%i==0 && a/i<=mm) {
		if (q) swap(x,y);
		return 1;
	}
	return 0;			 
}
void solve() {
	int i;
	for (i=a; i<=2*a; ++i) if (ok(i,x2,y3) && ok(i-a,x3,y2)) break;
	if (i<=2*a) printf("0 0 %d %d %d %d\n",x2,y2,x3,y3); else printf("IMPOSSIBLE\n");
}
int main() {
	int i;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&kd);
	for (i=1; i<=kd; ++i) {
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}