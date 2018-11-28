/*
#include <stdio.h>
#include <memory.h>

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

int Map[200][200];
int ans[200][200];

#define MAX 99999999


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	int Case,p,H,W;
	char cur;
	int i,j;
	int k;
	scanf("%d",&Case);
	for (p = 1; p <= Case; p ++) {
		cur = 'a';
		scanf("%d%d",&H,&W);
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W; j ++) {
				scanf("%d",&Map[i][j]);
			}
		}
		memset(ans,-1,sizeof(ans));
		ans[0][0] = cur;
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W; j ++) {
				// find min..
				int d = MAX;
				for (k = 0; k < 4; k ++) {
					int x = i + dx[k];
					int y = j + dy[k];
					if (x < 0 || x >= H || y < 0 || y >= W) continue;
					if (Map[x][y] >= Map[i][j]) continue;
					
					if (Map[x][y] < d) {
						d = Map[x][y];
					}
				}
				if (d == MAX) { // sink...
					if (ans[i][j] == -1) {
						ans[i][j] = ++ cur;
					}						
				} else { // no sink. flow..
					for (k = 0; k < 4; k ++) {
						int x = i + dx[k];
						int y = j + dy[k];
						if (x < 0 || x >= H || y < 0 || y >= W) continue;
						if (Map[x][y] == d) {
							if (ans[i][j] == -1) {
								if (ans[x][y] != -1) {
									ans[i][j] = ans[x][y];
								} else {
									ans[i][j] = ++ cur;
									ans[x][y] = ans[i][j];
								}
							} else {
								ans[x][y] = ans[i][j];
							}
						//	break;
						}
					}
				}
			}
		}
		printf("Case #%d:\n",p);
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W - 1; j ++) {
				printf("%c ",ans[i][j]);
			}
			printf("%c\n",ans[i][j]);
		}
	







	}
	return 0;
}
*/


#include <stdio.h>
#include <memory.h>
#include <queue>

using namespace std;

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

int Map[200][200];
bool flag[200][200][4];


struct NODE
{
	int cor;
	int dic;
	int h;
}ans[200][200];

#define MAX 99999999

struct NNODE
{
	int x,y;
}st,ed;

bool flag2[200][200];

int H,W;




int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int Case,p;
	int cur;
	int i,j;
	int k;
	scanf("%d",&Case);
	for (p = 1; p <= Case; p ++) {
		cur = 'a';
		scanf("%d%d",&H,&W);
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W; j ++) {
				scanf("%d",&Map[i][j]);
			}
		}
		memset(ans,-1,sizeof(ans));
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W; j ++) {
				// find min..
				int d = MAX;
				for (k = 0; k < 4; k ++) {
					int x = i + dx[k];
					int y = j + dy[k];
					if (x < 0 || x >= H || y < 0 || y >= W) continue;
					if (Map[x][y] >= Map[i][j]) continue;
					else break;
				}
				if (k < 4) { // no sink..
				} else { // sink..
					//dfs(i,j,cur);

					memset(flag,false,sizeof(flag));

					st.x = i;
					st.y = j;

					flag[i][j][0] = true;
					flag[i][j][1] = true;
					flag[i][j][2] = true;
					flag[i][j][3] = true;

					ans[i][j].cor = cur;
					ans[i][j].dic = -1;
					
					queue<NNODE> Q;
					Q.push(st);
					while (!Q.empty()) {
						st = Q.front();
						Q.pop();
						for (k = 3; k >= 0; k --) {
							int x = st.x + dx[k];
							int y = st.y + dy[k];
							if (x < 0 || x >= H || y < 0 || y >= W) continue;
							if (Map[x][y] <= Map[st.x][st.y]) continue;
							if (flag[x][y][k]) continue;
							flag[x][y][k] = true;

							if (ans[x][y].cor == -1) {
								ans[x][y].cor = cur;
								ans[x][y].dic = k;
								ans[x][y].h = Map[st.x][st.y];
								ed.x = x;
								ed.y = y;
								Q.push(ed);
							} else {
								if (Map[st.x][st.y] < ans[x][y].h) {
									ans[x][y].cor = cur;
									ans[x][y].dic = k;
									ans[x][y].h = Map[st.x][st.y];
									ed.x = x;
									ed.y = y;
									Q.push(ed);
								} else if (Map[st.x][st.y] == ans[x][y].h) {
									if (k >= ans[x][y].dic) {
										ans[x][y].cor = cur;
										ans[x][y].dic = k;
										ans[x][y].h = Map[st.x][st.y];
										ed.x = x;
										ed.y = y;
										Q.push(ed);
									}
								}
							}
						}
					}
					cur ++;
				}
			}
		}
/*
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W - 1; j ++) {
				printf("%c ",ans[i][j].cor);
			}
			printf("%c\n",ans[i][j].cor);
		}*/

		// reverse..
		memset(flag2,false,sizeof(flag2));

		cur = 'a' + 100;
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W; j ++) {
				if (flag2[i][j]) continue;


				flag2[i][j] = true;
				int cor = ans[i][j].cor;
				st.x = i;
				st.y = j;
				queue<NNODE> Q;
				Q.push(st);
				ans[i][j].cor = cur;
				

				while (!Q.empty()) {
					st = Q.front();
					Q.pop();
					for (k = 0; k < 4; k ++) {
						int x = st.x + dx[k];
						int y = st.y + dy[k];
						if (x < 0 || x >= H || y < 0 || y >= W) continue;
						if (flag2[x][y]) continue;
						
						if (ans[x][y].cor == cor) {flag2[x][y] = true;
							ans[x][y].cor = cur;
							ed.x = x;
							ed.y = y;
							Q.push(ed);
						}
					}
				}
				cur ++;
			}
		}
		printf("Case #%d:\n",p);
		for (i = 0; i < H; i ++) {
			for (j = 0; j < W - 1; j ++) {
				printf("%c ",ans[i][j].cor-100);
			}
			printf("%c\n",ans[i][j].cor-100);
		}
	







	}
	return 0;
}

