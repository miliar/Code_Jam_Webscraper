#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <memory.h>
#include <string>
#include <iostream>
using namespace std;
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
const int maxn=101;
int a[maxn][maxn];
int id[maxn][maxn];
int n,m;
int type[maxn][maxn];
char ans[maxn][maxn];

void init(){
	scanf("%d%d",&n,&m);
	int cur=0;
	for (int i=1;i<=n;i++){
		for (int j=1;j<=m;j++){
			scanf("%d",&a[i][j]);
			cur++;
			id[i][j]=cur;
		}
	}	
	return;
}

bool outside(int x,int y){
	return (x<1)||(x>n)||(y<1)||(y>m);
}

int dfs(int x,int y){
	int way=-1;
	int waybest=-1;
	for (int i=0;i<4;i++)
	{
		int tx=x+dx[i];
		int ty=y+dy[i];
		if (outside(tx,ty)){
			continue;
		}
		if (a[tx][ty]>=a[x][y]){
			continue;
		}
		if ((way==-1)||(a[tx][ty]<waybest)){
			way=i;
			waybest=a[tx][ty];
			continue;
		}
	}
	if (way==-1){
		type[x][y]=id[x][y];
		return id[x][y];
	}
	type[x][y]=dfs(x+dx[way],y+dy[way]);
	return type[x][y];
}

void gettype(){	
	memset(type,0xff,sizeof(type));
	for (int i=1;i<=n;i++){
		for (int j=1;j<=m;j++){
			if (type[i][j]>=0)
			{
				continue;
			}
			dfs(i,j);
		}
	}
	return;
}

void dfsans(int x,int y,char cc){
	ans[x][y]=cc;
	for (int i=0;i<4;i++){
		int tx=x+dx[i];
		int ty=y+dy[i];
		if (outside(tx,ty)){
			continue;
		}
		if (ans[tx][ty]!=0){
			continue;
		}
		if (type[tx][ty]!=type[x][y]){
			continue;
		}
		dfsans(tx,ty,cc);
	}
	return;
}

void getans(){
	char cur='a';
	memset(ans,0,sizeof(ans));
	for (int i=1;i<=n;i++){
		for (int j=1;j<=m;j++){
			if (ans[i][j]!=0){
				continue;
			}
			dfsans(i,j,cur);
			cur++;
		}
	}
	return;
}

void printans(){
	for (int i=1;i<=n;i++){
		for (int j=1;j<=m;j++){
			printf("%c",ans[i][j]);
			if (j!=m){
				printf(" ");
			}
		}
		printf("\n");
	}
	return;
}

int main(){
	//freopen("2.in","r",stdin);
	int t;
	scanf("%d",&t);
	for (int k=1;k<=t;k++)
	{
		init();
		printf("Case #%d:\n",k);
		gettype();
		getans();
		printans();
	}
	return 0;
}	
