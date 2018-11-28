#include <stdio.h>

int nprob, prob;
int H, W, R;
int brd[110][110];
int f[110][110];

int dp(int r, int c) {
	if (f[r][c] >= 0)
		return f[r][c];
		
	if (brd[r][c] == 1) {
		f[r][c] = 0;
		return 0;
	}
		
	if (r == H-1 || c == W-1) {
		if (r == H-1 && c == W-1) {
			f[r][c] = 1;
		} else {
			f[r][c] = 0;
		}
		return f[r][c];
	}
	
	f[r][c] = 0;
	if (r < H-2 && c < W-1) {
		f[r][c] += dp(r+2, c+1); f[r][c] %= 10007;
	}
	
	if (r < H-1 && c < W-2) {
		f[r][c] += dp(r+1, c+2); f[r][c] %= 10007;
	}
	
	return f[r][c];
}

int main() {
//	freopen("d.in", "r", stdin);
//	freopen("d.out", "w", stdout);
	
	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		scanf("%d%d%d", &H, &W, &R);
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				brd[i][j] = 0;
		
		for (int i = 0; i < R; i++) {
			int r, c;
			scanf("%d%d", &r, &c);
			brd[--r][--c] = 1;
		}
		
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				f[i][j] = -1;
				
		printf("Case #%d: %d\n", prob, dp(0, 0));
	}
	
	return 0;
}
