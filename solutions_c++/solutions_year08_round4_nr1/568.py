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

FILE *in=fopen("A.in","r");
FILE *outt=fopen("A.out","w");

int n,v;

int memo[11000][2];

int FF;

int g[11000],c[11000];

int solve(int node,int v)
{
	if(c[node]==-1){
		if(g[node]==v)return 0;
		return 1<<20;
	}
	int &ret=memo[node][v];
	if(ret!=-1)return ret;
	ret=1<<20;
	int i,j;
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			int x1=solve(2*node,i);
			int x2=solve(2*node+1,j);
			if(x1>=1<<20 || x2>=1<<20)continue;
			int z=i&j;
			if(z==v && g[node])ret=min(ret,x1+x2);
			z=i|j;
			if(z==v && !g[node])ret=min(ret,x1+x2);
			if(c[node]){
				if(((i|j)==v) || ((i&j)==v))
					ret=min(ret,1+x1+x2);
			}
		}
	}
	return ret;
}

int main()
{
	int i,j,k,test,tests;
	int n,ret;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		CLR(c,-1);
		fscanf(in,"%d%d",&n,&v);
		FF=(n-1)/2;
		for(i=0;i<FF;i++)
			fscanf(in,"%d%d",&g[i+1],&c[i+1]);
		for(i=FF+1;i<=n;i++)
			fscanf(in,"%d",&g[i]);
		CLR(memo,-1);
		ret=solve(1,v);
		if(ret==1<<20)fprintf(outt,"Case #%d: IMPOSSIBLE\n",test);
		else fprintf(outt,"Case #%d: %d\n",test,ret);
	}
	return 0;
}
