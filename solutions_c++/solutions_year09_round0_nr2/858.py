#include <stdio.h>
#include <string.h>
const int SIZE = 120;
const int LEN = 50000;
const int WAY = 4;
const int INF = 1<<25;
const int ALP = 50;
class Node{
public:
	int val;
	int x,y;
	Node * pre ;
	int col;
	Node(int v=0,int ix=0,int iy=0){
		pre=NULL;
		val=v;
		x=ix;
		y=iy;
		col=-1;
	}
	void show(){
		printf("( %d , %d ) col: %d\n",x,y,col);
	}
};
Node map[SIZE][SIZE];
Node* que[LEN];
char c2ch[ALP];
int deta[WAY][2]={{-1,0},{0,-1},{0,1},{1,0}};
int hi,wi;
void init();
void work();
void show();
bool check(int ,int);
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
			map[i][j]=Node(tmp,i,j);
		}
}
void work(){
	int head=0,tail=0;
	int i,j,k;
	int color=0;
	for (i=0;i<hi;i++)
		for (j=0;j<wi;j++){
			int best = map[i][j].val;
			Node * aim=NULL;
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
		Node * nd = que[head];
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
	memset(c2ch,-1,sizeof(c2ch));
	for (i=0;i<hi;i++)
		for (j=0;j<wi;j++){
			int tmp = map[i][j].col;
			if (c2ch[tmp]==-1){
				c2ch[tmp]=lab++;
			}
		}
}
bool check(int x,int y){
	return (x>=0 && x<hi && y>=0 && y<wi);
}
void show(){
	int i,j;
	for (i=0;i<hi;i++){
		printf("%c",c2ch[map[i][0].col]);
		for (j=1;j<wi;j++){
			printf(" %c",c2ch[map[i][j].col]);
		}
		printf("\n");
	}
}