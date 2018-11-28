#include<iostream>
#define MAX 101
using namespace std;
int father[MAX*MAX];
int map[MAX][MAX];
int code[MAX*MAX];
bool visit[MAX][MAX];
int getRoot(int i);
void dfs(int x,int y,int h,int w,int r);
int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	
	int t,h,w,cases=0;
	int i,j;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&h,&w);
		cases++;
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				scanf("%d",&map[i][j]);
				visit[i][j]=false;
				father[i*w+j]=i*w+j;
				code[i*w+j]=-1;
			}
		}
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				if(!visit[i][j]){
					dfs(i,j,h,w,i*w+j);
				}
			}
		}
		printf("Case #%d:\n",cases);
		int index=0;
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				if(j)printf(" ");
				int r=getRoot(i*w+j);
				if(code[r]==-1){
					code[r]=index++;
				}
				printf("%c",code[r]+'a');
			}
			printf("\n");
		}
	}
	return 0;
}
int getRoot(int i){
	if(father[i]==i)return i;
	father[i]=getRoot(father[i]);
	return father[i];
}
void dfs(int x,int y,int h,int w,int r){
	visit[x][y]=true;
	father[x*w+y]=r;
	int min=(1<<29);
	int i,j;
	if(x-1>=0&&min>map[x-1][y]){
		min=map[x-1][y];
		i=x-1;j=y;
	}
	if(y-1>=0&&min>map[x][y-1]){
		min=map[x][y-1];
		i=x;j=y-1;
	}
	if(y+1<w&&min>map[x][y+1]){
		min=map[x][y+1];
		i=x;j=y+1;
	}
	if(x+1<h&&min>map[x+1][y]){
		min=map[x+1][y];
		i=x+1;j=y;
	}
	if(min>=map[x][y])return;
	else{
		if(visit[i][j]){
			father[r]=getRoot(i*w+j);
			return;
		}
		else dfs(i,j,h,w,r);
	}
}