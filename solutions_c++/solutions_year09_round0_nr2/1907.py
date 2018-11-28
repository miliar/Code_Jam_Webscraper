#include <iostream>
#include <string>
#include <map>
using namespace std;

const int N = 105, visited = -1;
int a[N][N], adj[N][N][4];
int dx[5] = {0, 0, -1, 1, 0};
int dy[5] = {0, -1, 0, 0, 1};
char res[N][N];
int Q[N * N];

int main(int argc, char** argv){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int cas, h, w;
	scanf("%d", &cas);
	for(int cs = 1; cs <= cas; ++cs){
		scanf("%d%d", &h, &w);
		for(int y = 0; y < h; ++y){
			for(int x = 0; x < w; ++x){
				scanf("%d", &a[y][x]);
			}
		}
		memset(adj, -1, sizeof(adj));
		for(int y = 0; y < h; ++y){
			for(int x = 0; x < w; ++x){
				int d1 = 0;
				int x1 = x;
				int y1 = y;
				for(int d2 = 1; d2 <= 4; ++d2){
					int x2 = x + dx[d2];
					int y2 = y + dy[d2];
					if(0 <= x2 && x2 < w && 0 <= y2 && y2 < h){
						if(a[y2][x2] < a[y1][x1]){
							x1 = x2;
							y1 = y2;
							d1 = d2;
						}
					}
				}
				if(d1){
					--d1;
					adj[y][x][d1] = x1 + y1 * w;
					adj[y1][x1][3 - d1] = x + y * w;
				}
			}
		}
		char label = 'a';
		for(int y = 0; y < h; ++y){
			for(int x = 0; x < w; ++x){
				if(a[y][x] == visited) continue;
				int begin = 0, end = 0;
				Q[end++] = x + y * w;
				a[y][x] = visited;
				while(begin < end){
					int cur = Q[begin++];
					int x1 = cur % w;
					int y1 = cur / w;
					res[y1][x1] = label;
					for(int d = 0; d < 4; ++d){
						if(adj[y1][x1][d] == -1) continue;
						int x2 = adj[y1][x1][d] % w;
						int y2 = adj[y1][x1][d] / w;
						if(a[y2][x2] != visited){
							a[y2][x2] = visited;
							Q[end++] = adj[y1][x1][d];
						}
					}
				}
				++label;
			}
		}
		printf("Case #%d:\n", cs);
		for(int y = 0; y < h; ++y){
			for(int x = 0; x < w - 1; ++x)
				printf("%c ", res[y][x]);
			printf("%c\n", res[y][w - 1]);
		}
	}
	
	return 0;
}