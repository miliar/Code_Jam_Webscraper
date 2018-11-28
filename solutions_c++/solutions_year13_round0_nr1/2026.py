#include <bits/stdc++.h>
#define fr(i,a,b) for (int i = (a); i < (b); ++i)
using namespace std;

char grid[5][5];
int di[] = {1,-1,0,0,1,-1,-1,1};
int dj[] = {0,0,1,-1,1,-1,1,-1};

bool v(int i, int j) {return i >= 0 && j >= 0 && j < 4 && i < 4;}

bool check(char c) {
	int cnt = 0;
	fr(i,0,4) {
		fr(j,0,4) {
			if (grid[i][j] == c) {
				fr(k,0,8) {
					cnt = 1;
					int ii = i + di[k], jj = j + dj[k];
					while (v(ii,jj)) {
						if (grid[ii][jj] == c) ++cnt;
						else break;
						ii += di[k]; jj += dj[k];
					}
					if (cnt >= 4) return true;
				}				
			}
		}
	}
	return false;
}

int main() {
	int nt;
	int ti, tj;
	scanf("%d", &nt); ++nt;
	fr(_,1,nt) {
		ti = tj = -1;
		bool ponto = false;
		fr(i,0,4) {
			scanf("%s", grid[i]);
			fr(j,0,4) {
				if (grid[i][j] == 'T') {
					ti = i; tj = j;
				}
				ponto |= (grid[i][j] == '.');
			}
		}
		printf("Case #%d: ", _);
		if (ti != -1) {
			grid[ti][tj] = 'X';
			if (check('X')) {printf("X won\n");continue;}
			grid[ti][tj] = 'O';
			if (check('O')) {printf("O won\n");continue;}
			grid[ti][tj] = 'T';
		} else {
			if (check('X')) {printf("X won\n");continue;}
			else if (check('O')) {printf("O won\n");continue;}
		}
		if (!ponto) printf("Draw\n");
		else printf("Game has not completed\n");
		
	}
	return 0;
}
