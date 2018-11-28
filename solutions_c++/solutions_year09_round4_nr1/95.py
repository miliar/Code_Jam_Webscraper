#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n,m,a[55],l[55],dist[55][55],dx[55],dy[55];
char st[55];
bool vx[55],vy[55];

inline bool Extended_path(int u)
{
	vx[u]=1;
	for (int v=0;v<n;v++)
	if (!vy[v] && dx[u]+dy[v]==dist[u][v]) {
		vy[v]=1;
		if (l[v]==-1 || Extended_path(l[v]))
			return l[v]=u,true;
	}
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int Test,Case=0;
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d",&n);
		for (int i=0;i<n;i++) {
			scanf("%s",st);a[i]=-1;
			for (int j=0;j<n;j++)
			if (st[j]=='1') a[i]=j;
		}
		int ret=0;
		for (int i=0;i<n;i++) {
			int k=i;
			for (int j=i;j<n;j++)
			if (a[j]<=i) {
				k=j;break;
			}
			for (int j=k;j>i;j--) {
				swap(a[j],a[j-1]);
				ret++;
			}
		}
		printf("Case #%d: %d\n",++Case,ret);
	}
	return 0;
}
