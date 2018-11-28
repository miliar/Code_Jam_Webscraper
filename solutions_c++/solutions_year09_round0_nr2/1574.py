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

using namespace std;

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) ) 
#define EPS 1e-9

int ar[110][110];
int n,m;

int basin[110][110];
int p=0;

int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};

FILE *in=fopen("B.in","r");
FILE *out=fopen("B.out","w");

int dfs(int x,int y)
{
	int i,ret;
	int best=1<<30,bx,by;
	for(i=0;i<4;i++){
		int nx=x+dx[i];
		int ny=y+dy[i];
		if(nx<0 || ny<0 || nx>=n || ny>=m)continue;
		if(ar[nx][ny]<best){
			best=ar[nx][ny];
			bx=nx;
			by=ny;
		}
	}
	if(best>=ar[x][y]){
		if(basin[x][y]!=-1)return basin[x][y];
		basin[x][y]=p++;
		return basin[x][y];
	}
	ret=dfs(bx,by);
	return ret;
}
int sol[110][110];
int main()
{
	int i,j,k,ret,T;
	fscanf(in,"%d",&T);
	for(int test=0;test<T;test++){
		p=0;
		fscanf(in,"%d%d",&n,&m);
		CLR(basin,-1);
		for(i=0;i<n;i++)for(j=0;j<m;j++)fscanf(in,"%d",&ar[i][j]);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				sol[i][j]=dfs(i,j);
		fprintf(out,"Case #%d:\n",test+1);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(j==m-1)fprintf(out,"%c\n",sol[i][j]+'a');
				else fprintf(out,"%c ",sol[i][j]+'a');
			}
		}
	}
	return 0;
}



