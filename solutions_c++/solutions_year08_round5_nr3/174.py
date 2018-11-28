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

FILE *in=fopen("C.in","r");
FILE *outt=fopen("C.out","w");

char ar[100][100];

int n,m;

int memo[11][11][1<<12];

int solve(int x,int y,int mask)
{
	if(x==n)return 0;
	if(y==m)return solve(x+1,0,mask);
	int &ret=memo[x][y][mask],vis=0;
	if(ret!=-1)return ret;
	ret=1<<20;
	ret=solve(x,y+1,mask>>1);
	if((mask & 1) && y)vis=1;
	if((mask & (1<<2)) && y!=m-1)vis=1;
	if((mask & 1<<m) && y)vis=1;
	if(!vis && ar[x][y]=='.')ret=max(ret,1+solve(x,y+1,(mask>>1)|(1<<m)));
	return ret;
}

int main()
{
	int i,j,k,test,tests;
	int ret;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		ret=0;
		fscanf(in,"%d%d",&n,&m);
		for(i=0;i<n;i++){
			fscanf(in,"\n");
			for(j=0;j<m;j++){
				fscanf(in,"%c",&ar[i][j]);
			}
		}
		CLR(memo,-1);
		ret=solve(0,0,0);
		fprintf(outt,"Case #%d: %d\n",test,ret);
	}
	return 0;
}
