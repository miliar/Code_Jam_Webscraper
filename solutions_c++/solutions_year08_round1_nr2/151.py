#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int t, c;
int n, m;
char a[2][2010][2010];
int b[2010];
int used[2010];
int ans[2010];

int check() {
	int j, k;
	memset(used, 0, sizeof(used));
	for (j=1;j<=n;j++) 	
		for (k=1;k<=m;k++) 					
			if (a[ans[j]][j][k])
				used[k]=1;	
	if (count(used+1,used+m+1,1)==m)
		return -1;
	for (j=1;j<=m;j++)
		if (b[j]!=0 && used[j]==0)
			return b[j];	
	return 0;
}

int main () {
	int i, j, k;
	int x, y;
	int res, pos, pom;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	for (scanf("%d", &c), t=1; t<=c; t++) {

		scanf("%d%d", &n, &m);
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		for (i=1; i<=m; i++)
			for (scanf("%d" ,&j); j; j--) {
				scanf("%d%d", &x, &y);
				a[y][x][i]=1;
				if (y)
					b[i]=x;
			}
		memset(ans, 0, sizeof(ans));
		while (1) {
			pom = check();
			if (pom<=0) break;
			ans[pom]=1;
		}
		
		printf("Case #%d:",t);
		if (pom==0)
			printf(" IMPOSSIBLE");
		else
			for (j=1;j<=n;j++)
				printf(" %d",ans[j]);
		printf("\n");

/*
		// make graph
		scanf("%d%d", &n, &m);
		source=2*n+m+1;
		sink=2*n+m+2;
		n0=sink+1;
		n1=sink+2;

		for (i=1; i<=m; i++)
			for (scanf("%d" ,&j); j; j--) {
				scanf("%d%d", &x, &y);
				add(y*n+x, i, 1);
			}

		for (i=2*n+1; i<=2*n+m; i++) 
			add(i, sink, 1);
		
		add(source, n0, m);
		add(source, n1, m);

		for (i=1; i<=n; i++)
			add(n0, i, 1);

		for (i=n+1; i<=2*n; i++)
			add(n1, i, 1);
		
		// bin search on answer
		l=0;
		r=m;
		ans=-1;
		while (l<=r) {
			med=(l+r)/2;
			if (solve(med)) {
				r=med-1;
				ans=med;
			}
			else
				l=med+1;
		}

		// answer
		printf("Case #%d: ",t);
		if (ans==-1)
			printf("IMPOSSIBLE\n");
		else
*/
	}

	return 0;
}