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

FILE *in=fopen("R1B.in","r");
FILE *out=fopen("R1B.out","w");

long long L,P,C;

int memo[1001][1001],best[1001][1001];

int solve(int x,int y)
{
	if(x*C>=y){
		best[x][y]=x;
		return 0;
	}
	int &ret=memo[x][y];
	if(ret!=-1)return ret;
	ret=1<<20;
	for(int i=best[x][y-1];i<=best[x+1][y];i++){
		int q=max(1+solve(i,y),1+solve(x,i));
		if(q<ret){
			ret=q;
			best[x][y]=i;
		}
	}
	return ret;
}
int main()
{
	int i,j,n,k;
	int tests;
	fscanf(in,"%d",&tests);
	for(int test=0;test<tests;test++){
		fscanf(in,"%lld %lld %lld",&L,&P,&C);
		int ret=0;
		CLR(memo,-1);
		for(i=0;i<1001;i++)best[i][i]=i;
		for(int r=2;r<=P-L+1;r++){
			for(i=L;i<=P-r+1;i++)
				ret=solve(i,i+r-1);
		}
		fprintf(out,"Case #%d: %d\n",test+1,ret);
	}
	return 0;
}