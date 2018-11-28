#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define size(x) int((x).size())
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
typedef long long I64; typedef unsigned long long U64;
const double EPS=1e-12;
const int INF=999999999;
typedef vector<int> VI;
typedef vector<string> VS;

int dirs[4][2]={{-1,0},{0,1},{1,0},{0,-1}};

const int MAXW=500;

struct Node {
	char x,y;
	int bw,yw;
};

int m,n;
char g[17][20];
int wallId[17][17][4];

int nWall;
int wall[MAXW+1][3];

int sx,sy,tx,ty;
int toWall[17][17][4];

int f[17][17][MAXW+1][MAXW+1];

void build()
{
	bool flag[17][17];
	memset(flag,0,sizeof(flag));
	queue<Node> Q;
	Node p,q;

	nWall=0;
	memset(wallId,0,sizeof(wallId));
	memset(toWall,0,sizeof(toWall));

	p.x=sx,p.y=sy;
	Q.push(p);
	flag[sx][sy]=1;
	while(!Q.empty()) {
		p=Q.front();
		Q.pop();
		
		for(int i=0;i<4;i++) {
			int x=p.x,y=p.y;
			while(x>=0 && x<m && y>=0 && y<n && g[x][y]!='#') x+=dirs[i][0],y+=dirs[i][1];

			int d=(i+2)%4;
			int &id=wallId[x][y][d];
			if(id==0) {
				nWall++;
				if(nWall>MAXW) printf("ERROR\n");

				wall[nWall][0]=x;
				wall[nWall][1]=y;
				wall[nWall][2]=d;
				id=nWall;
			}

			toWall[p.x][p.y][i]=id;
		}

		for(int i=0;i<4;i++) {
			q.x=p.x+dirs[i][0];
			q.y=p.y+dirs[i][1];
			if(q.x>=0 && q.x<m && q.y>=0 && q.y<n && g[q.x][q.y]=='.' && !flag[q.x][q.y]) {
				flag[q.x][q.y]=1;
				Q.push(q);
			}
		}
	}
}

void getPos(int w,int &x,int &y)
{
	x=wall[w][0]+dirs[wall[w][2]][0];
	y=wall[w][1]+dirs[wall[w][2]][1];
}

int com()
{
	deque<Node> Q;
	Node p,q;

	memset(f,-1,sizeof(f));
	p.x=sx,p.y=sy,p.bw=p.yw=0;
	f[p.x][p.y][p.bw][p.yw]=0;
	Q.push_back(p);

	while(!Q.empty()) {
		p=Q.front();
		Q.pop_front();

		int w=f[p.x][p.y][p.bw][p.yw];

//		printf("%d %d %d %d : %d\n",p.x,p.y,p.bw,p.yw,w);

		if(p.x==tx && p.y==ty) return w;

		for(int i=0;i<4;i++) {
			int id=toWall[p.x][p.y][i];
			q=p;
			q.bw=id;
			
			if(q.bw!=q.yw && f[q.x][q.y][q.bw][q.yw]<0) {
				f[q.x][q.y][q.bw][q.yw]=w;
				Q.push_front(q);
			}

			q=p;
			q.yw=id;
			if(q.bw!=q.yw && f[q.x][q.y][q.bw][q.yw]<0) {
				f[q.x][q.y][q.bw][q.yw]=w;
				Q.push_front(q);
			}
		}

		int bx,by,yx,yy;
		bool canT=0;

		if(p.bw>0 && p.yw>0) {
			canT=1;
			getPos(p.bw,bx,by);
			getPos(p.yw,yx,yy);
		}

		for(int i=0;i<4;i++) {
			int x=p.x+dirs[i][0],y=p.y+dirs[i][1];
			if(canT) {
				if(x==wall[p.bw][0] && y==wall[p.bw][1] && ((i+2)%4)==wall[p.bw][2]) x=yx,y=yy;
				else if(x==wall[p.yw][0] && y==wall[p.yw][1] && ((i+2)%4)==wall[p.yw][2]) x=bx,y=by;
			}
			if(x<0 || x>=m || y<0 || y>=n || g[x][y]=='#') continue;

			q=p;
			q.x=x,q.y=y;
			if(f[q.x][q.y][q.bw][q.yw]<0) {
				f[q.x][q.y][q.bw][q.yw]=w+1;
				Q.push_back(q);
			}
		}
	}

	return -1;
}

void solve()
{
	scanf("%d%d",&m,&n);
	memset(g[0],'#',sizeof(g[0]));
	memset(g[m+1],'#',sizeof(g[m+1]));
	for(int i=1;i<=m;i++) {
		scanf("%s",g[i]+1);
		g[i][0]=g[i][n+1]='#';
	}
	
	m+=2,n+=2;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++) {
			if(g[i][j]=='O') sx=i,sy=j,g[i][j]='.';
			else if(g[i][j]=='X') tx=i,ty=j,g[i][j]='.';
		}

	/*
	for(int i=0;i<m;i++) {
		g[i][n]=0;
		printf("%s\n",g[i]);
	}
	*/

	build();

	/*
	for(int i=1;i<=nWall;i++) printf("%d : %d %d %d\n",i,wall[i][0],wall[i][1],wall[i][2]);
	for(int x=0;x<m;x++)
		for(int y=0;y<n;y++) {
			printf("%d %d: ",x,y);
			for(int i=0;i<4;i++) printf(" %d",toWall[x][y][i]);printf("\n");
		}
		*/


	int ans=com();
	if(ans<0) printf("THE CAKE IS A LIE"); else printf("%d",ans);
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
		printf("\n");
	}

	return 0;
}
