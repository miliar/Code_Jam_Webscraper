/*

#include <iostream>
#include <algorithm>
#include <string.h>
#include <cstdio>
#include <queue>
#include <map>
using namespace std;
struct node {
	int x,y;
}s,ns;

int use[105][105];
int mm[105][105];
int h,w,cnt;
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

bool ok(int x, int y){
	return x>=0&&x<h&&y>=0&&y<w;
}

void bfs(int x,int y){
	queue<node>qq;
	while(!qq.empty()) qq.pop();
	s.x=x;
	s.y=y;
	qq.push(s);
	int i,J,nx,ny,minn,k;
	while(!qq.empty()){
		s=qq.front();
		qq.pop();
		minn=mm[s.x][s.y];
		k=-1;
		for(i=0;i<4;i++){
			nx=s.x+dir[i][0];
			ny=s.y+dir[i][1];
			if(ok(nx,ny)){
				if(mm[nx][ny]<minn){
					minn=mm[nx][ny];
					k=i;
				}
			}
		}
		if(k!=-1){
			nx=s.x+dir[k][0];
			ny=s.y+dir[k][1];
			
			if(use[nx][ny]){
				use[s.x][s.y]=use[nx][ny];
				return;
			}
			else{
				
				if(!use[s.x][s.y])
					use[s.x][s.y]=++cnt;
				use[nx][ny]=use[s.x][s.y];
				ns.x=nx;
				ns.y=ny;
				qq.push(ns);
			}
		}
		else{
			if(!use[s.x][s.y])
			use[s.x][s.y]=++cnt;
			return;
		}
	}
}


int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int i,ii,J,ncase;
	scanf("%d",&ncase);
	for(ii=1;ii<=ncase;ii++){
		scanf("%d%d",&h,&w);
		for(i=0;i<h;i++)
		for(J=0;J<w;J++)
			scanf("%d",&mm[i][J]);
		
		memset(use,0,sizeof(use));
		cnt=0;
		
		for(i=0;i<h;i++)
		for(J=0;J<w;J++){
			if(!use[i][J]){
				bfs(i,J);
				
			}
		}
		for(i=0;i<h;i++)
		for(J=0;J<w;J++){
				bfs(i,J);

		}
		printf("Case #%d:\n",ii);
		cnt=0;
		map<int, int> my;
		my.clear();
		for(i=0;i<h;i++){
			for(J=0;J<w;J++){
				if(!my[use[i][J]])
					my[use[i][J]]=++cnt;
				use[i][J]=my[use[i][J]];
			}
		}
		
		for(i=0;i<h;i++){
			for(J=0;J<w-1;J++)
				printf("%c ",use[i][J]-1+'a');
				
			printf("%c\n",use[i][w-1]-1+'a');
		}
	}
}

*/
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>

using namespace std;

int use[105][105];
int mm[105][105];
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

int h,w,cnt;
bool ok(int x,int y){
	return x>=0&&x<h&&y>=0&&y<w;
}


void dfs(int x, int y){
	int i,minn,k=-1;
	minn=mm[x][y];
	int nx,ny;
	for(i=0;i<4;i++){
		nx=x+dir[i][0];
		ny=y+dir[i][1];
		if(ok(nx,ny)&&minn>mm[nx][ny]){
			k=i;
			minn=mm[nx][ny];
		}
	}
	if(k!=-1){
		nx=x+dir[k][0];
		ny=y+dir[k][1];
		
		if(use[nx][ny]){
			use[x][y]=use[nx][ny];
		}
		else{
			dfs(nx,ny);
			if(use[nx][ny])
				use[x][y]=use[nx][ny];
			else
				use[x][y]=++cnt;
		}
	}
	else
		use[x][y]=++cnt;
}

int main(){
	
	
	int i,J,ncase,ii;
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);
	scanf("%d",&ncase);
	for(ii=1;ii<=ncase;ii++){
		scanf("%d%d",&h,&w);
		for(i=0;i<h;i++)
		for(J=0;J<w;J++)
			scanf("%d",&mm[i][J]);
		
		cnt=0;
		memset(use,0,sizeof(use));
		for(i=0;i<h;i++)
		for(J=0;J<w;J++){
			if(!use[i][J]){
				dfs(i,J);
				//if(!use[i][J])
					//use[i][J]=++cnt;
			}
		}
		
		printf("Case #%d:\n",ii);
		for(i=0;i<h;i++){
			
			for(J=0;J<w-1;J++)
				printf("%c ",use[i][J]-1+'a');
			printf("%c\n",use[i][w-1]-1+'a');
		}
	}
}
	
	
	