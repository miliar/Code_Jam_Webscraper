#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#include <iostream>

using namespace std;

int dx[] = {-1,0,0,1}, dy[] = {0,-1,1,0}, h, w, alt[100][100];
bool use[100][100];
char ans[100][100], cur_basin;

inline bool onBoard(int x, int y) {
	return x>=0 && x<h && y>=0 && y<w;
}

void DFS(int x, int y) {
	//cerr << x << " " << y << endl;
	use[x][y] = 1;
	int best = 10001, best_dir;
	for (int i=0; i<4; i++) if (onBoard(x+dx[i],y+dy[i]) && alt[x+dx[i]][y+dy[i]]<best) best = alt[x+dx[i]][y+dy[i]], best_dir = i;
	if (best<alt[x][y]) {
		if (!use[x+dx[best_dir]][y+dy[best_dir]]) DFS(x+dx[best_dir],y+dy[best_dir]);
		ans[x][y] = ans[x+dx[best_dir]][y+dy[best_dir]];		
	} else {
		ans[x][y] = cur_basin++;
	}
}

int main() {
	int t;
	scanf("%d",&t);
	for (int test=1; test<=t; test++) {
		cur_basin = 'a';
		printf("Case #%d:\n",test);
		scanf("%d%d",&h,&w);
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++) scanf("%d",&alt[i][j]);
		memset(use,0,sizeof(use));
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				if (!use[i][j]) DFS(i,j);
				putchar(ans[i][j]);putchar(' ');
			}
			putchar('\n');
		}
	}
}
