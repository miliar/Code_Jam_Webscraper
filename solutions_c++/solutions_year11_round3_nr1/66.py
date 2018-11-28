#include <cstdio>
using namespace std;

char g[100][100];
int n,m,T;

bool ok(int x,int y) {
	return x>=0 && x<n && y>=0 && y<m && g[x][y]=='#';
}

int main() {
	scanf("%d",&T);
	for (int I=1;I<=T;I++) {
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++) {
			scanf("%s",g[i]);
		}
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				if (g[i][j]=='#') {
					if (ok(i,j) && ok(i+1,j) && ok(i,j+1) && ok(i+1,j+1)) {
						g[i][j]='/';g[i+1][j+1]='/';
						g[i+1][j]='\\';g[i][j+1]='\\';
					}
				}
			}
		}
		
		bool ans=true;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (g[i][j]=='#') ans=false;
		printf("Case #%d:\n",I);
		if (ans) {
			for (int i=0;i<n;i++) {
				for (int j=0;j<m;j++) printf("%c",g[i][j]);
				printf("\n");
			}
		} else {
			printf("Impossible\n");
		}
	}
	
}