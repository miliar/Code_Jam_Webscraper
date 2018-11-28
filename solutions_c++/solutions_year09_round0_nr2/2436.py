#include <cstdio>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

bool vis[110][110];
int a[110][110];
char b[110][110], ch;
int h, w;
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
char re;
vector< pair<int,int> > path;

void run(int x, int y){
//		printf("%d %d\n", x, y);
	vis[x][y] = true;
	path.push_back( make_pair(x, y));
	int min = 10000000, minx, miny;
	bool jump = false;
	for (int i=0; i<4; i++){
		int nx = x + dir[i][0];
		int ny = y + dir[i][1];
		if (nx >=0 && nx < h && ny >= 0 && ny < w){
			if (a[x][y] > a[nx][ny] && a[nx][ny] < min) {	
				minx = nx;
				miny = ny;
				min = a[nx][ny];
				jump = true;
			}
		}
	}

	if (jump){
		if (!vis[minx][miny])
			run(minx, miny);
		else
			re = b[minx][miny];
	}
}

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		scanf("%d%d", &h, &w);
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		memset(vis, 0, sizeof(vis));
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++)
				scanf("%d", &a[i][j]);

		ch = 'a';
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++)
				if (!vis[i][j]){
					re = '#';
					path.clear();
					run(i, j);
					if (re == '#') {
						re = ch++;
	//										printf("new -- %d %d %c\n", i, j, re);
					}else{
		//								printf("curr -- %d %d %c\n", i, j, re);
					}
					int size = path.size();
					for (int k=0; k<size; k++){
						b[path[k].first][path[k].second] = re;
				//					printf("(%d %d) ", path[k].first, path[k].second);
					}
			//									printf("\n");
				}

		printf("Case #%d:\n", ++ca);
		for (int i=0; i<h; i++){
			for (int j=0; j<w; j++){
				if (j!=0) printf(" ");
				printf("%c", b[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
