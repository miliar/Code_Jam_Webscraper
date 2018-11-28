#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

		char grid[200][200];
		vector<pair<int,int> > connections[200][200];

bool seen[200][200];

int dfs(int r, int c) {
	if (seen[r][c]) return 0;
	seen[r][c] = 1;
	int ret = 2;
	for (int i = 0; i < connections[r][c].size(); i++) {
		ret += dfs(connections[r][c][i].first,connections[r][c][i].second)-1;
	}
	return ret;
}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);

		
		int R, C; scanf("%d%d ",&R,&C);
		for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			connections[i][j] = vector<pair<int,int> >();
			seen[i][j] = 0;
		}
		}
		for (int i = 0; i < R; i++) {
			scanf("%s ",grid[i]);
			for (int j = 0; j < C; j++) {
				int r1,r2,c1,c2;
				switch (grid[i][j]) {
				case '-':
				r1=r2=i;
				c1=j-1,c2=j+1;
				break;
				case '|':
				c1=c2=j;
				r1=i-1,r2=i+1;
				break;
				case '\\':
				r1=i-1;c1=j-1;
				r2=i+1;c2=j+1;
				break;
				case '/':
				r1=i-1;c1=j+1;
				r2=i+1;c2=j-1;
				break;
				}
				r1 = (r1+R)%R;
				r2 = (r2+R)%R;
				c1 = (c1+C)%C;
				c2 = (c2+C)%C;
				connections[r1][c1].push_back(make_pair(r2,c2));
				connections[r2][c2].push_back(make_pair(r1,c1));
			}
		}

		int ret=1;

		for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (seen[i][j]) continue;
			if (dfs(i,j) != 0) {
				ret = 0;
				break;
			}
			ret *= 2;
			ret %= 1000003;
		}
		}
		
		
		printf("Case #%d: %d\n",test,ret);
	}
}
