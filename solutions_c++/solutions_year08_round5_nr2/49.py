#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

#define LL long long

using namespace std;

char data[30][30];
int H,W;

struct cellstr {
	int curx;
	int cury;
	int ballx;
	int bally;
	int handx;
	int handy;
	int cost;
	cellstr() {
	}
	cellstr(int a, int b, int c, int d, int e, int f) {
		cury=a;
		curx=b;
		bally=c;
		ballx=d;
		handy=e;
		handx=f;
		cost=1;
	}
	cellstr(int a, int b, int c, int d, int e, int f,int ss) {
		cury=a;
		curx=b;
		bally=c;
		ballx=d;
		handy=e;
		handx=f;
		cost=ss;
	}

};

struct wallestr {
	int y,x;
	wallestr(int a, int b) {
		y=a;
		x=b;
	}
	wallestr() {
	}
};

vector<cellstr> adjlist[10][10][10][10][10][10];
int visited[10][10][10][10][10][10];
wallestr walle[10][10][5];
const int incx[] = {-1,0,0,1};
const int incy[] = {0,-1,1,0};

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t,T;
	scanf("%d", &T);
	int i,j,k;
	int x,y,by,bx,hy,hx;

	for (t=1; t<=T; t++) {
		int sx,sy;
		scanf("%d %d", &H, &W);
		for (i=0; i<H; i++) {
			scanf("%s", data[i]);
			for (j=0; j<W; j++) {
				if (data[i][j]=='O') {
					sx=j;
					sy=i;
				}
			}
		}

		for (y=0; y<H; y++) {
			for (x=0; x<W; x++) {
				if (data[y][x]=='#') continue;
				for (k=0; k<4; k++) {
					int ny=y+incy[k];
					int nx=x+incx[k];
					int ly=y;
					int lx=x;
					walle[y][x][k]=wallestr(H,W);
					while (!(ny<0 || ny>=H || nx<0 || nx>=W)) {
						if (data[ny][nx]=='#') {
							break;
						}
						ly=ny;
						lx=nx;
						ny=ny+incy[k];
						nx=nx+incx[k];
					}
					walle[y][x][k]=wallestr(ly,lx);
				}
			}
		}
		for (y=0; y<H; y++) {
			for (x=0; x<W; x++) {
				for (by=0; by<=H; by++) {
					for (bx=0; bx<=W; bx++) {
						for (hy=0; hy<=H; hy++) {
							for (hx=0; hx<=W; hx++) {
								adjlist[y][x][by][bx][hy][hx].clear();
								for (k=0; k<4; k++) {
									int ny=y+incy[k];
									int nx=x+incx[k];
									if (ny<0 || ny>=H || nx<0 || nx>=W) continue;
									if (data[ny][nx]=='#') continue;
									adjlist[y][x][by][bx][hy][hx].push_back(cellstr(ny,nx,by,bx,hy,hx));
								}

								// shoot ball
								for (k=0; k<4; k++) {
									int ax=walle[y][x][k].x;
									int ay=walle[y][x][k].y;
									adjlist[y][x][by][bx][hy][hx].push_back(cellstr(y,x,ay,ax,hy,hx,0));
								}								

								// shoot hand
								for (k=0; k<4; k++) {
									int ax=walle[y][x][k].x;
									int ay=walle[y][x][k].y;
									adjlist[y][x][by][bx][hy][hx].push_back(cellstr(y,x,by,bx,ay,ax,0));
								}

								// transport
								if (y==hy && x==hx) {
									adjlist[y][x][by][bx][hy][hx].push_back(cellstr(by,bx,by,bx,hy,hx,1));
								}

								if (y==by && x==bx) {
									adjlist[y][x][by][bx][hy][hx].push_back(cellstr(hy,hx,by,bx,hy,hx,1));
								}
								
							}
						}
					}
				}
			}
		}

		memset(visited,-1,sizeof(visited));
		queue<cellstr> q;
		queue<cellstr> q2;
		q.push(cellstr(sy,sx,H,W,H,W));
		visited[sy][sx][H][W][H][W]=0;
		int ans=-1;
		int nq=0;
		while (!q.empty() || !q2.empty()) {
			cellstr cur;
			if (!q2.empty()) {
				cur=q2.front(); q2.pop();
			}
			else {
				cur=q.front(); q.pop();
			}
			if (cur.curx<0 || cur.curx>=W || cur.cury<0 || cur.cury>=H) continue;

			int val=visited[cur.cury][cur.curx][cur.bally][cur.ballx][cur.handy][cur.handx];
//			printf("%d %d %d %d %d %d\n",cur.cury,cur.curx,cur.bally,cur.ballx,cur.handy,cur.handx);
			if (data[cur.cury][cur.curx]=='X') {
				ans=val;
				break;
			}
			for (i=0; i<adjlist[cur.cury][cur.curx][cur.bally][cur.ballx][cur.handy][cur.handx].size(); i++) {
				cellstr next=adjlist[cur.cury][cur.curx][cur.bally][cur.ballx][cur.handy][cur.handx][i];
				if (visited[next.cury][next.curx][next.bally][next.ballx][next.handy][next.handx]==-1) {
					visited[next.cury][next.curx][next.bally][next.ballx][next.handy][next.handx]=val+next.cost;
					if (next.cost==0)
						q2.push(next);
					else
						q.push(next);
				}
			}
		}

		if (ans!=-1) 
			printf("Case #%d: %d\n",t,ans);
		else
			printf("Case #%d: THE CAKE IS A LIE\n",t);
	}
	return 0;
}

