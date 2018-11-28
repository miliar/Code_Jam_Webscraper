#include<stdio.h>
#include<memory.h>

int map[100][100];
bool flag[100][100];

int getnum(int x, int y) {
	if(x<0 || y<0) return 0;
	return map[x][y];
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		int H, W, R;
		scanf("%d%d%d", &H, &W, &R);
		map[0][0]=1;
		memset(flag, 0, sizeof(flag));
		for(int i=0;i<R;i++) {
			int r, c;
			scanf("%d%d", &r, &c);
			flag[r-1][c-1]=true;
		}
		for(int i=0;i<H;i++) {
			for(int j=0;j<W;j++) {
				if(!i&&!j) continue;
				if(flag[i][j]) map[i][j]=0;
				else map[i][j]=(getnum(i-2, j-1)+getnum(i-1, j-2))%10007;
			}
		}
		printf("Case #%d: %d\n", cas, map[H-1][W-1]);
	}
	return 0;
}