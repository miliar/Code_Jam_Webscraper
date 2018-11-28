#include <cstdio>
#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <climits>
using namespace std;

int A[101][101];
int D[101][101][4];
char M[101][101];

int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

void solve(int pno)
{
	int H, W;
	int i, j, k;
	
	memset(A, 0, sizeof(A) );
	memset(D, 0, sizeof(D) );
	memset(M, 0, sizeof(M) );
	
	cin >> H >> W;
	
	int min_alt;
	int min_dir;
	int ii, jj;
	
	for (i = 0; i < H; ++i) {
		for (j = 0; j < W; ++j) {
			cin >> A[i][j];
		}
	}
	
	for (i = 0; i < H; ++i) {
		for (j = 0; j < W; ++j) {
			min_alt = INT_MAX;
			min_dir = -1;
			for (k = 0; k < 4; ++k) {
				ii = i + dir[k][0];
				jj = j + dir[k][1];
				if (ii < 0 || ii >= H || jj < 0 || jj >= W) continue;
				if (A[ii][jj] >= A[i][j]) continue;
				if (min_alt > A[ii][jj]) {
					min_alt = A[ii][jj];
					min_dir = k;
				}
			}
			if (min_dir >= 0) {
				D[i][j][min_dir] = 1;
				D[i + dir[min_dir][0]][j + dir[min_dir][1]][3 - min_dir] = 1;
			}
		}
	}
	
	stack<pair<int, int> > st;
	char idx = 'a';
	
	for (i = 0; i < H; ++i) {
		for (j = 0; j < W; ++j) {
			if (M[i][j]) continue;
			st.push(make_pair(i, j) );
			while (!st.empty() ) {
				int x = st.top().first;
				int y = st.top().second;
				st.pop();
				if (M[x][y]) continue;
				M[x][y] = idx;
				for (k = 0; k < 4; ++k) {
					if (D[x][y][k]) {
						st.push(make_pair(x + dir[k][0], y + dir[k][1]) );
					}
				}
			}
			++idx;
		}
	}
	printf("Case #%d:\n", pno);
	for (i = 0; i < H; ++i) {
		for (j = 0; j < W; ++j) {
			printf("%c", M[i][j]);
			if (j != W - 1) printf(" ");
		}
		printf("\n");
	}
	
	return;
}

int main()
{
	int T;
	
	cin >> T;
	for (int i = 0; i < T; ++i) solve(i + 1);
	
	return 0;
}

