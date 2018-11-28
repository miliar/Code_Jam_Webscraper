#include<cstdio>
#include<cstring>

int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};

int main(){
	int T;
	int ca=0;
	scanf("%d", &T);
	while (T--){
		int H, W;
		scanf("%d%d", &H, &W);
		int M[H][W];
		for (int i = 0 ; i < H; ++i)
			for (int j = 0 ; j < W; ++j)
				scanf("%d", &M[i][j]);
		int vis[H][W];
		memset(vis, 0, sizeof(vis));
		vis[0][0] = 'a';
		int x = 0, y = 0;
		for (;;){
			bool ok = 0;
			//printf("%d %d\n", x, y);
			int px, py, ph=M[x][y];
			for (int i = 0 ; i < 4; ++i){
				int nx = x+dir[i][0], ny = y+dir[i][1];
				if (nx<0||nx>=H||ny<0||ny>=W) continue;
				if (M[nx][ny] < ph) ok=1, ph = M[nx][ny], px=nx, py=ny;
			}
			if (!ok) break;
			vis[px][py] = 'a';
			x = px, y = py;
		}
		char next = 'b';
		int L[10000][2];
		for (int i = 0 ; i < H; ++i)
			for (int j = 0 ; j < W; ++j)
				if (!vis[i][j]){
					int x = i, y= j;
					int cnt = 0;
					L[cnt][0] = x, L[cnt++][1] = y;
					char code = next;
					//printf("==\n");
					for (;;){
						//printf(">>%d %d\n" ,x, y);
						bool ok = 0;
						int px, py, ph=M[x][y];
						for (int k = 0 ; k < 4; ++k){
							int nx = x+dir[k][0], ny = y+dir[k][1];
							if (nx<0||nx>=H||ny<0||ny>=W) continue;
							if (M[nx][ny] < ph) ok=1, ph = M[nx][ny], px=nx, py=ny;
						}
						if (!ok) break;
						if (vis[px][py]){
							code = vis[px][py];
							break;
						}
						L[cnt][0] = px, L[cnt++][1] = py;
						x = px, y = py;
					}
					//printf("code = %c\n", code);
					for (int k = 0 ; k < cnt; ++k)
						vis[L[k][0]][L[k][1]] = code;
					next += next==code;
				}
		printf("Case #%d:\n", ++ca);
		for (int i = 0 ; i < H ; ++i)
			for (int j = 0 ; j < W; ++j)
				printf("%c%c", vis[i][j], j==W-1?'\n':' ');
	}
	return 0;
}
