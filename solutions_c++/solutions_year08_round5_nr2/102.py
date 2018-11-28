#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("B.in","r");
FILE *outt=fopen("B.out","w");

int dx[4]={0,0,-1,1};
int dy[4]={-1,1,0,0};

class gtr{
public:
	int x;
	int y;
	int px;
	int py;
	int dir;
	int cost;
	gtr(){}gtr(int x1,int y1,int px1,int py1,int dir1,int cost1){
		x=x1;y=y1;px=px1;py=py1;dir=dir1;cost=cost1;
	}
};
int vis[20][20][20][20][4];

deque < gtr > Q;

char ar[20][20];

int n,m;

int fx[20][20][4],fy[20][20][4];

bool check(int x,int y)
{
	if(x<0 || y<0 || x>=n || y>=m || ar[x][y]=='#')return 0;
	return 1;
}

int main()
{
	int i,j,k,test,tests,found,curx,cury;
	int ret,cx,cy,sx,sy;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		ret=1<<30;
		CLR(vis,0);
		found=0;
		while(Q.size())Q.pop_back();
		fscanf(in,"%d%d",&n,&m);
		for(i=0;i<n;i++){
			fscanf(in,"\n");
			for(j=0;j<m;j++){
				fscanf(in,"%c",&ar[i][j]);
				if(ar[i][j]=='O'){
					sx=i;
					sy=j;
				}
				if(ar[i][j]=='X'){
					cx=i;
					cy=j;
				}
			}
		}
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(ar[i][j]=='#')continue;

				for(k=0;k<4;k++){
					curx=i;
					cury=j;
					while(check(curx,cury)){
						curx+=dx[k];
						cury+=dy[k];
					}
					curx-=dx[k];
					cury-=dy[k];
					fx[i][j][k]=curx;
					fy[i][j][k]=cury;
				}
			}
		}			

		Q.push_back(gtr(sx,sy,n,m,0,0));
		vis[sx][sy][n][m][0]=1;
		while(Q.size()){
			gtr fr=Q.front();Q.pop_front();
			if(ar[fr.x][fr.y]=='X'){
				found=1;
				ret=fr.cost;
				break;
			}

			for(i=0;i<4;i++){
				int nx=fr.x+dx[i];
				int ny=fr.y+dy[i];
				if(!check(nx,ny))continue;
				if(vis[nx][ny][fr.px][fr.py][fr.dir])continue;
				vis[nx][ny][fr.px][fr.py][fr.dir]=1;
				Q.push_back(gtr(nx,ny,fr.px,fr.py,fr.dir,fr.cost+1));
			}
			for(i=0;i<4;i++){
				int nx=fr.x+dx[i];
				int ny=fr.y+dy[i];
				if(nx>=0 && ny>=0 && nx<n && ny<m && ar[nx][ny]!='#')continue;
				if(fr.x==fr.px && fr.y==fr.py && fr.dir==i)continue;
				if(fr.px==n)continue;
				if(vis[fr.px][fr.py][fr.x][fr.y][i])continue;
				vis[fr.px][fr.py][fr.x][fr.y][i]=1;
				Q.push_back(gtr(fr.px,fr.py,fr.x,fr.y,i,fr.cost+1));
			}
			for(i=0;i<4;i++){
				int npx=fx[fr.x][fr.y][i];
				int npy=fy[fr.x][fr.y][i];
				if(vis[fr.x][fr.y][npx][npy][i])continue;
				vis[fr.x][fr.y][npx][npy][i]=1;
				Q.push_front(gtr(fr.x,fr.y,npx,npy,i,fr.cost));
			}
		}
		if(!found)fprintf(outt,"Case #%d: THE CAKE IS A LIE\n",test);
		else fprintf(outt,"Case #%d: %d\n",test,ret);
	}
	return 0;
}
