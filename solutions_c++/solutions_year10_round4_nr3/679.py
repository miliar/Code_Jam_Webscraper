
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <vector>

using namespace std;

int R;
bool bac[101][101];

bool check() {
	for(int i = 0; i < 101; i++)
		for(int j = 0; j < 101; j++)
			if(bac[i][j])
				return true;
	return false;
}

int solve() {
	for(int t = 0;; t++) {
		if(!check())
			return t;
		
		bool bac2[101][101];
		memset(bac2, 0, sizeof(bac2));
		for(int i = 1; i < 101; i++)
			for(int j = 1; j < 101; j++) {
				if(bac[i-1][j] && bac[i][j-1])
					bac2[i][j] = true;
				if(bac[i][j]) {
					if(bac[i-1][j] || bac[i][j-1])
						bac2[i][j] = true;
				}
			}
		for(int i = 0; i < 101; i++)
			for(int j = 0; j < 101; j++)
				bac[i][j] = bac2[i][j];
	}
	return 0;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d", &R);
		memset(bac, 0, sizeof(bac));
		for(int j = 0; j < R; j++) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int x = x1; x <= x2; x++)
				for(int y = y1; y <= y2; y++)
					bac[x][y] = true;
		}
		printf("Case #%d: %d\n", i+1, solve());
	}
	
	return 0;
}