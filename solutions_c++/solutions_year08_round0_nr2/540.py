#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAXN 210

int g[MAXN];
char b[MAXN][MAXN];
pair<int,int> a[MAXN];
int n, m, T;
int marked[MAXN];

int gt(int a, int b) {
	return a*60+b;
}

int dfs(int i) {
	int j;
	if (i==0)
		return 1;	
	for (j=1; j<=n+m; j++)
		if (b[i][j] && marked[j]==0) {
			marked[j]=1;
			if (dfs(g[j])) {
				g[j]=i;		
				return 1;
			}
		}
	return 0;
}

int main () { 
	int t, c;
	int i, j;
	int h1, m1, h2, m2;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	for (scanf("%d",&c), t=1; t<=c; t++) {
		scanf("%d", &T);
		scanf("%d%d", &n, &m);
		for (i=1; i<=n+m; i++) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a[i].first=gt(h1, m1);
			a[i].second=gt(h2, m2);
			if (a[i].first>=a[i].second)
				a[i].second+=24*60;
		}
		memset(b, 0, sizeof(b));
		for (i=1; i<=n; i++) 
			for (j=n+1; j<=n+m; j++) {
				b[i][j]=(a[i].second+T<=a[j].first);					
				b[j][i]=(a[j].second+T<=a[i].first);					
			}
		memset(g, 0, sizeof(g));
		for (i=1; i<=n+m; i++) {
			memset(marked, 0, sizeof(marked));
			dfs(i);
		}
		a[0].first=a[0].second=0;
		for (i=1;i<=n;i++) 			a[0].first+=(g[i]==0);
		for (i=n+1;i<=n+m;i++) 		a[0].second+=(g[i]==0);
		printf("Case #%d: %d %d\n", t, a[0].first, a[0].second);
	}	
	return 0;
}