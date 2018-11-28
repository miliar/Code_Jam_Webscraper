#include <stdio.h>

char pic[51][51];
int r, c;
int dr[3] = {0,1,1};
int dc[3] = {1,0,1};

int transform() {
	int i, j, d;
	int newr, newc;

	for (i=0;i<r;i++) {
		for (j=0;j<c;j++) {
			if (pic[i][j] == '#' ) {
				for (d=0;d<3;d++) {
					newr = i + dr[d];
					newc = j + dc[d];
					if (newr >= r || newc >= c || pic[newr][newc] != '#' ) {
						return 0;
					}	
				}	
				pic[i][j] = '/';
				pic[i][j+1]='\\';
				pic[i+1][j]='\\';
				pic[i+1][j+1]='/';
			}
		}
	}
	return 1;
}

void solve() {
	int i;

	scanf("%d%d", &r, &c);
	for (i=0;i<r;i++){
		scanf("%s", pic[i]);
	}

	if (!transform()) {
		printf("Impossible\n");
	} else {
		for (i=0;i<r;i++){
			printf("%s\n", pic[i]);
		}
	}
}

int main() {
	int t, i;
	scanf("%d",&t);
	for (i=1;i<=t;i++) {
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}
