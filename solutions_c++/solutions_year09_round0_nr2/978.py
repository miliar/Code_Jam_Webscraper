#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>

using namespace std;

#define MN		128

const int dr[] = {-1, 0, 0, 1};
const int dc[] = { 0,-1, 1, 0};

int T, N, M;
int A[MN][MN];

char u[MN][MN];
char curLabel;


char dfs(int r, int c)
{
	if (u[r][c]!=0) {
		return u[r][c];
	}

	int br=-1, bc;

	for (int k=0; k<4; ++k) {
		int nr = r + dr[k];
		int nc = c + dc[k];
		if (0<=nr&&nr<N && 0<=nc&&nc<M) {
			if (br==-1 || A[nr][nc]<A[br][bc]) {
				br = nr;
				bc = nc;
			}
		}
	}

	if (br==-1 || A[br][bc]>=A[r][c]) {
		u[r][c] = curLabel++;
	} else {
		u[r][c] = dfs(br, bc);
	}

	return u[r][c];
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("B.in", "r", stdin);
	//freopen("B.out", "w", stdout);

	scanf("%d", &T);

	for (int t=0; t<T; ++t) {
		memset(u, 0, sizeof u);
		curLabel = 'a';

		scanf("%d%d", &N, &M);
		for (int i=0; i<N; ++i) {
			for (int j=0; j<M; ++j) {
				scanf("%d", &A[i][j]);
			}
		}

		printf("Case #%d:\n", t+1);
		for (int i=0; i<N; ++i) {
			for (int j=0; j<M; ++j) {
				printf(j<M-1 ? "%c " : "%c\n", dfs(i, j));
			}
		}
	}

	return 0;
}