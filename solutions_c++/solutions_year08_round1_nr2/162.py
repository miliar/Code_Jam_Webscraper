#include <cstdio>
#include <string>
#include <set>
using namespace std;
const int c=2000;
struct rec {
	int x,y;
	rec (int a=0, int b=0) {
		x=a;
		y=b;
	}
};
bool operator < (const rec &a, const rec &b) {
	return a.y<b.y || a.y==b.y && a.x<b.x;
}
int kd,n,m;
set<rec> a[c+1];
int r[c+1];
void solve(int ii) {
	int i,j;
	memset(r,0,sizeof(r));
	set<rec>::iterator u;
	while (1) {
		for (i=1; i<=m; ++i) if (a[i].size()==0) {
			printf("Case #%d: IMPOSSIBLE\n",ii);
			return;
		}
		for (i=1; i<=m; ++i) if (a[i].begin()->y && !r[a[i].begin()->x]) {
			r[a[i].begin()->x]=1;
			break;
		}
		if (i<=m) {
			for (j=1; j<=m; ++j) {
				u=a[j].find(rec(a[i].begin()->x,0));
				if (u!=a[j].end()) a[j].erase(u);
			}				
	 	} else {
	 		printf("Case #%d: ",ii);
	 		for (i=1; i<=n; ++i) printf("%d ",r[i]);
	 		printf("\n");
	 		return;
	 	}
    }
}
int main() {
	int ii,i,j,x,y,k;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&kd);
	for (ii=1; ii<=kd; ++ii) {
		scanf("%d%d",&n,&m);
		for (i=1; i<=m; ++i) a[i].clear();
		for (i=1; i<=m; ++i) {
			scanf("%d",&k);
			for (j=1; j<=k; ++j) {
				scanf("%d%d",&x,&y);
				a[i].insert(rec(x,y));
			}
		}
		solve(ii);
	}
	return 0;
}                                                  	