#include<cstdio>
inline int min(int A, int B){return A < B? A: B;}
int T, D, R, C, ans;
char grd[11][11];
int val[11][11];
bool chk(int X, int Y){
	int sX = 0, sY = 0;
	for(int i = 0; i <= ans; i++)
	    for(int j = 0; j <= ans; j++){
			if((i == 0 || i == ans) && (j == 0 || j == ans))continue;
			sX += (ans - (i * 2)) * val[X + i][Y + j];
			sY += (ans - (j * 2)) * val[X + i][Y + j];
		}
	//printf("%d %d %d %d\n", X, Y ,sX,sY);
	return (sX == 0 && sY == 0);
}
int main(){
	freopen("B-small-3.in", "r", stdin);
	freopen("B-small-3.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d%d%d", &R, &C, &D);
		for(int i = 0; i < R; i++){
		    scanf("%s", grd[i]);
			for(int j = 0; j < C; j++)
			    val[i][j] = grd[i][j] - '0' + D;
		}
		ans = min(R, C) - 1;
		while(ans > 1){
			bool flg = false;
			for(int i = 0; i + ans < R && !flg; i++)
			    for(int j = 0; j + ans < C && !flg; j++)
			        if(chk(i, j))flg = true;
			if(flg)break;
			ans--;
		}
		printf("Case #%d: ", t);
		if(ans <= 1)puts("IMPOSSIBLE");
		else printf("%d\n", ans + 1);
	}
}

