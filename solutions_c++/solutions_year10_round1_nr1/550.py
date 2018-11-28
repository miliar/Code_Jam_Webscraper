#include <cstdio>
#include <string>
#include <cstring>

using namespace std;
int T, N, K;
char mp[55][55];
char rt[55][55];

int off[8][2] = {1,0, -1,0, 0,1, 0,-1, 1,1, -1,-1, -1,1, 1,-1};
int n;
bool f1, f2;
int inside(int x, int y) {
	if(x >= 0 && y >= 0 && x < n && y < n)
		return true;
	return false;
}

int AC() {
	for(int i = 0; i < n; ++i) {
		for(int j = 0; j < n; ++j) {
			if(rt[i][j] != '.') {
				
				for(int k = 0; k < 8; ++k) {
					int cnt = 1;
					int xx = i;
					int yy = j;
					while(1) {
						int x = xx + off[k][0];
						int y = yy + off[k][1];
						if(inside(x, y) && rt[x][y] == rt[i][j]){
							++cnt;
						} else {
							break;
						}
						xx = x;
						yy = y;
					}
					if(cnt >= K) {
						if(rt[i][j] == 'B') f1 = true;
						if(rt[i][j] == 'R') f2 = true;
					}
				}
			}
		}
	}
	return 0;
}
int main() {
	freopen("small.in", "r", stdin);
	freopen("a-out.txt", "w", stdout);
	scanf("%d", &T);
	int CT = 1;
	while(T--) {
		scanf("%d %d", &N, &K);
		for(int i = 0; i < N; ++i) {
			scanf("%s", &mp[i]);
		}
		memset(rt, '\0', sizeof(rt));
		n = N;
		for(int i = 0; i < n; ++i) {
			for(int j = n - 1; j >= 0; --j) {
				rt[i][n - 1 - j] = mp[j][i];
			}
		}
		/*for(int i = 0; i < n; ++i) {
			puts(rt[i]);
		}*/
		for(int i = 0; i < n; ++i) {
			int end = n - 1;
			for(int j = n - 1; j >= 0; --j) {
				if(rt[j][i] != '.') {
					rt[end][i] = rt[j][i];
					--end;
				}
			}
			for(int j = end; j >= 0; --j) {
				rt[j][i] = '.';
			}
		}
		/*for(int i = 0; i < n; ++i) {
			puts(rt[i]);
		}*/
		f1 = f2 = false;
		AC();
		printf("Case #%d: ", CT++);
		if(f1 && (f2 == false)) {
			puts("Blue");
		}
		if((f1 == false) && f2) {
			
			puts("Red");
		}
		if(f1 && f2) {
			puts("Both");
		}
		if((!f1) && (!f2)) {
			puts("Neither");
		}
	}
}