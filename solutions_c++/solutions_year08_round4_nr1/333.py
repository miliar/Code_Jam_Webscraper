#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAXN 10010

int n, v;
int type[MAXN];
int ch[MAXN];
int b[MAXN][2];

int min4(int a, int b, int c, int d) {
	return min(min(a,b), min(c,d));
}

void updateAND(int i, int val) {
	int left, right;
	left=i*2;
	right=i*2+1;
	b[i][1]=min(b[i][1], b[left][1]+b[right][1]+val);
	b[i][0]=min4(b[i][0], b[left][0]+b[right][1]+val, b[left][1]+b[right][0]+val, b[left][0]+b[right][0]+val);
}

void updateOR(int i, int val) {
	int left, right;
	left=i*2;
	right=i*2+1;
	b[i][0]=min(b[i][0], b[left][0]+b[right][0]+val);
	b[i][1]=min4(b[i][1], b[left][1]+b[right][1]+val, b[left][0]+b[right][1]+val, b[left][1]+b[right][0]+val);	
}			

int main () {
	int i, pom;
	int t, c;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	for (scanf("%d", &t), c=1; c<=t; c++) {

		scanf("%d%d", &n, &v);

		for (i=1; i<=n; i++)
			b[i][0]=b[i][1]=MAXN;

		for (i=1; i<=(n-1)/2; i++)
			scanf("%d%d", &type[i], &ch[i]);

		for (i=(n-1)/2+1; i<=n; i++) {			
			scanf("%d", &pom);
			b[i][pom]=0;
		}

		for (i=(n-1)/2; i>=1; i--) {			
			
			if (type[i]) 				updateAND(i,0);

			if (type[i] && ch[i]) 		updateOR(i,1);

			if (!type[i])				updateOR(i,0);

			if (!type[i] && ch[i])		updateAND(i,1);
			
		}

		printf("Case #%d: ",c);
		if (b[1][v]==MAXN)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",b[1][v]);

	}
	return 0;
}
