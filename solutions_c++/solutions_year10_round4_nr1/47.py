#include <iostream>

using namespace std;

int n;
int d[200][200];

int onBoard(int y, int x) {
	return (0<=y && y<2*n-1 && 0<=x && x<2*n-1);
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++) {
		scanf("%d",&n);
		memset(d,-1,sizeof(d));
		int r=0;
		for (int i=0;i<n;i++,r++) {
			for (int j=0;j<=i;j++) {
				scanf("%d",&d[r][n-1-i+2*j]);
			}
		}
		for (int i=n-2;i>=0;i--,r++) {
			for (int j=0;j<=i;j++) {
				scanf("%d",&d[r][n-1-i+2*j]);
			}
		}
		/*for (int i=0;i<2*n-1;i++) {
			for (int j=0;j<2*n-1;j++) {
				printf("%3d",d[i][j]);
			}
			printf("\n");
		}*/
		int s=2*n-1, best=-1;
		for (int y=0;y<s;y++) for (int x=0;x<s;x++) {
			int dis=0;
			for (int i=0;i<s;i++) for (int j=0;j<s;j++) {
				int distance=abs(y-i)+abs(x-j);
				if (d[i][j]!=-1) dis=max(dis,distance);
			}
			int have=n*(n-1)+n;
			int rez=dis*(dis+1)+dis+1 - have;

			int i2,j2,ok=1;
			for (int i=0;i<s;i++) for (int j=0;j<s;j++) {
				if (d[i][j]==-1) continue;
				//horizontal
				i2=i; j2=x+x-j;
				if (onBoard(i2,j2) && d[i2][j2]!=-1 && d[i][j]!=d[i2][j2]) ok=0;
				//vertical
				i2=y+y-i; j2=j;
				if (onBoard(i2,j2) && d[i2][j2]!=-1 && d[i][j]!=d[i2][j2]) ok=0;
			}
			if (ok && (best==-1 || rez<best)) best=rez;
		}
		printf("Case #%d: %d\n",test,best);
	}
    return 0;
}
