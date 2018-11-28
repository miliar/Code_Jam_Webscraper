#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

#define MAXN 60

int iCase;
int n,l;
int graph[MAXN][MAXN];
int new_graph[MAXN][MAXN];
int offset[8][2] = {{-1,-1}
					,{-1,0}
					,{-1,1}
					,{0,-1}
					,{0,1}
					,{1,-1}
					,{1,0}
					,{1,1}};

void work();
void read_graph();
void rotate();
void fall_down();
void print_newgraph();
bool check(int x,int y);
bool not_legal(int x, int y);

int main(){

	scanf("%d",&iCase);
	for(int i=0;i<iCase;++i){
		printf("Case #%d: ",i+1);
		scanf("%d %d",&n,&l);
		work();
	}
	return 0;
}

void work() {
	int result = 0;
	read_graph();
	rotate();
	fall_down();
	
	//judge
	//R win result &= 1
	//B win result &= 2
	for(int i=0;i<n;++i){
		for(int j=0;j<n;++j){
			if(new_graph[i][j] & result) continue;
			if(!new_graph[i][j]) continue;
			if(check(i,j)){
				result |= new_graph[i][j];
				//printf("%d %d %d\n",i,j,new_graph[i][j]);
			}
		}
	}

	if(result == 3)
		printf("Both\n");
	else if(result == 2)
		printf("Blue\n");
	else if(result == 1)
		printf("Red\n");
	else
		printf("Neither\n");

}

bool check(int x,int y){
	int i;
	int xx,yy,new_xx,new_yy;

	for(int i=0;i<8;++i){	//dir
		xx = x;
		yy = y;
		bool flag = true;
		for(int k=1;k<l;++k){
			new_xx = xx+offset[i][0];
			new_yy = yy+offset[i][1];
			if(not_legal(new_xx,new_yy)){
				flag= false;
				break;
			}
			if(new_graph[new_xx][new_yy] != new_graph[xx][yy]){
				flag =false;
				break;
			}
			xx = new_xx;
			yy = new_yy;
		}
		if(flag) return true;
	}
	return false;
}

bool not_legal(int x, int y){
	if(x<0 || x>=n) return true;
	if(y<0 || y>=n) return true;
	return false;
}

void fall_down(){
	//print_newgraph();
	//printf("----------------------------\n");
	//scan from bottom
	for(int i=0;i<n;++i){	//col
		for(int j=n-1;j>0;--j){	//row
			if(new_graph[j][i]==0){
				for(int k=j-1;k>=0;--k){
					if(new_graph[k][i]){
						new_graph[j][i]=new_graph[k][i];
						new_graph[k][i]=0;
						break;
					}
				}
			}
		}
	}
	//print_newgraph();
}

void read_graph(){
	int i,j;
	memset(graph,0,sizeof(graph));	
	for(i=0;i<n;++i){
		for(j=0;j<n;++j){
			char ch;
			cin >> ch;
			if(ch=='.')
				graph[i][j]=0;
			else if(ch=='R')
				graph[i][j]=1;
			else
				graph[i][j]=2;
		}
	}
/*
	for(int i=0;i<n;++i){
		for(int j=0;j<n;++j){
			if(graph[i][j]==0)
				printf(".");
			else if(graph[i][j]==1)
				printf("R");
			else
				printf("B");
		}
		printf("\n");
	}
	*/
}

void rotate(){
	int i,j,old_i,old_j;
	memset(new_graph,0,sizeof(new_graph));
	for(i=0;i<n;++i){
		old_j=i;
		old_i=n-1;
		for(int j=0;j<n;++j){
			new_graph[i][j]=graph[old_i][old_j];
			--old_i;
		}
	}
}

void print_newgraph(){
	for(int i=0;i<n;++i){
		for(int j=0;j<n;++j){
			if(new_graph[i][j]==0)
				printf(".");
			else if(new_graph[i][j]==1)
				printf("R");
			else
				printf("B");
		}
		printf("\n");
	}
}