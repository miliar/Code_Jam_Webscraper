#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#define task "file"
#define Inf (int)1e9
using namespace std;
int test;
char map[30][30];
int u[30][30];
int xs,ys,xf,yf;
deque<int> X,Y;
int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};
int n,m;

int in(int x,int y){
	return (x>0 && x<=n && y>0 && y<=m);
}

int abs(int a){
	return (a>0)?a:-a;
}

int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	scanf("%i\n",&test);
	
	for (int zzz=1;zzz<=test;zzz++){
		printf("Case #%i: ",zzz);
		for (int i=0;i<30;i++)
		for (int j=0;j<30;j++) map[i][j]='#';
		scanf("%i %i\n",&n,&m);
		for (int i=1;i<=n;i++){
			for (int j=1;j<=m;j++){
				scanf("%c",&map[i][j]);
				if (map[i][j]=='O'){
					xs=i;
					ys=j;
				}
				if (map[i][j]=='X'){
					xf=i;
					yf=j;
				}
			}
			scanf("\n");
		}
		for (int i=0;i<30;i++)
			for (int j=0;j<30;j++)
				u[i][j]=Inf;
		u[xs][ys]=0;
		X.push_back(xs);
		Y.push_back(ys);
		while (!X.empty()){
			int curx=X.front();
			int cury=Y.front();
			X.pop_front();
			Y.pop_front();
			for (int i=0;i<4;i++){
				int nx=curx+dx[i];
				int ny=cury+dy[i];
				if (map[nx][ny]!='#' && u[nx][ny]>u[curx][cury]+1){
					u[nx][ny]=u[curx][cury]+1;
					X.push_back(nx);
					Y.push_back(ny);
				}
			}
			for (int i=0;i<4;i++)
				for (int j=0;j<4;j++)
					if (i!=j){
						int xxx=curx;
						int yyy=cury;
						while (map[xxx+dx[i]][yyy+dy[i]]!='#'){
								xxx+=dx[i];
								yyy+=dy[i];
						}
						
							int xx=curx;
							int yy=cury;
							while (map[xx+dx[j]][yy+dy[j]]!='#'){
								xx+=dx[j];
								yy+=dy[j];
							}
							if (u[xx][yy]>u[curx][cury]+abs(xxx-curx)+abs(yyy-cury)+1){
								u[xx][yy]=u[curx][cury]+abs(xxx-curx)+abs(yyy-cury)+1;
								X.push_back(xx);
								Y.push_back(yy);
							}
						
					}
			
		}
		if (u[xf][yf]==Inf) printf("THE CAKE IS A LIE\n");
		else printf("%i\n",u[xf][yf]);

	}


	return 0;
}
