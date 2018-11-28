#include <stdio.h>


int main() {
	int en;
	int i, j, k;
	bool ec[110][110];
	int ecase,ecount;
	int er;
	int many;
	int ans;
	int dr[11000], dc[11000], dmany;
	int cr[11000], cc[11000], cmany;
	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		scanf("%d", &er);
		for (i = 0; i<=100; i++)
			for(j=0;j <=100;j++)
				ec[i][j] = false;
		many= 0;
		while (er > 0) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (j = x1; j<=x2; j++)
				for(k=y1;k<=y2;k++)
					if (ec[j][k] == false) {
						ec[j][k] = true;
						many++;
					}
			er--;
		}
		ans=0;
		while(many>0) {
			dmany = 0;
			cmany = 0;
			for (i = 1; i <= 100; i++)
				for (j = 1; j <= 100; j++)
					if (ec[i][j] && !ec[i-1][j] && !ec[i][j-1]) {
						dr[dmany] = i;
						dc[dmany] = j;
						dmany++;
					}
					else if (!ec[i][j] && ec[i-1][j] && ec[i][j-1]) {
						cr[cmany] = i;
						cc[cmany] = j;
						cmany++;
					}
			for (i = 0; i < dmany; i++) {
				ec[ dr[i] ][ dc[i] ] = false;
				many--;
			}
			for (i = 0; i < cmany; i++) {
				ec[ cr[i] ][ cc[i] ] = true;
				many++;
			}
			ans++;
		}
		printf("Case #%d: %d\n", ecount, ans);
	}
	return 0;
}
