#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define  SIZE  200
const int LEN = 50000;
const int WAY = 4;
const int INF = 100000000;
const int ALP = 50;
class Cell{
public:
	int val;
	int x,y;
	Cell * pre ;
	int col;
	Cell(int v=0,int ix=0,int iy=0){
		val=v;
		x=ix,y=iy;
		col=-1;
		pre=NULL;
	}
};
Cell map[SIZE][SIZE];
Cell* que[LEN];
char col2char[ALP];
int deta[WAY][2]={{-1,0},{0,-1},{0,1},{1,0}};
int hi,wi;
void init();

inline bool check(int x,int y){
	return (x>=0 && x<hi && y>=0 && y<wi);
}
void work(){
	int head=0,tail=0;
	int i,j,k;
	int color=0;
	for (i=0;i<hi;i++)
		for (j=0;j<wi;j++){
			int best = map[i][j].val;
			Cell * aim=NULL;
			for (k=0;k<WAY;k++){
				int nx = i+deta[k][0];
				int ny = j+deta[k][1];
				if (check(nx,ny)&& best>map[nx][ny].val){	
					best = map[nx][ny].val;
					aim = &map[nx][ny];
				}
			}
			if (aim){
				map[i][j].pre = aim;
			}else{
				map[i][j].col = color++;
				que[tail]=&map[i][j];
				tail=(tail+1)%LEN;
			}
		}
	//bfs
	while (head!=tail){
		Cell * nd = que[head];
		head = (head+1)%LEN;
		for (k=0;k<WAY;k++){
			int nx = nd->x + deta[k][0];
			int ny = nd->y + deta[k][1];
			if (check(nx,ny) && map[nx][ny].pre==nd &&map[nx][ny].col==-1){
				map[nx][ny].col = nd->col;
				que[tail] = &map[nx][ny];
				tail=(tail+1)%LEN;
			}
		}
	}
	char lab='a';
	memset(col2char,-1,sizeof(col2char));
	for (i=0;i<hi;i++)
		for (j=0;j<wi;j++){
			int tmp = map[i][j].col;
			if (col2char[tmp]==-1){
				col2char[tmp]=lab++;
			}
		}
}
void show();

int main(){
	int cas;
	scanf("%d",&cas);
	int i;
	for (i=1;i<=cas;i++){
		init();
		work();
		printf("Case #%d:\n",i);
		show();
	}
	return 0;
}
void init(){
	scanf("%d%d",&hi,&wi);
	int i,j;
	for (i=0;i<hi;i++)
		for (j=0;j<wi;j++){
			int tmp;
			scanf("%d",&tmp);
			map[i][j]=Cell(tmp,i,j);
		}
}
void show(){
	int i,j;
	for (i=0;i<hi;i++){
		printf("%c",col2char[map[i][0].col]);
		for (j=1;j<wi;j++){
			printf(" %c",col2char[map[i][j].col]);
		}
		printf("\n");
	}
}