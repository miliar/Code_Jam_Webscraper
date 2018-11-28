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

FILE *in=fopen("D.in","r");
FILE *outt=fopen("D.out","w");

int can[120][120];

int memo[120][120];

int dx[2]={1,2};
int dy[2]={2,1};

int n,m,r;

int mod=10007;

int solve(int x,int y)
{
	if(x==n-1 && y==m-1)return 1;
	int &ret=memo[x][y],i;
	if(ret!=-1)return ret;
	ret=0;
	for(i=0;i<2;i++){
		int nx=x+dx[i];
		int ny=y+dy[i];
		if(nx>=n || ny>=m || can[nx][ny])continue;
		ret+=solve(nx,ny);
		ret%=mod;
	}
	return ret;
}

int main()
{
	int i,j,k,test,tests,ret;
	int x,y;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		CLR(can,0);
		CLR(memo,-1);
		fscanf(in,"%d%d%d",&n,&m,&r);
		for(i=0;i<r;i++){
			fscanf(in,"%d%d",&x,&y);
			x--;y--;
			can[x][y]=1;
		}
		ret=solve(0,0);
		fprintf(outt,"Case #%d: %d\n",test,ret);
	}
	return 0;
}
