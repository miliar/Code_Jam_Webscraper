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
FILE *out=fopen("D.out","w");

int n;

int memo[1001][1<<10];

int mod=30031;

int main()
{
	int i,k,test,tests,j;
	fscanf(in,"%d",&tests);
	int p,mask;
	for(test=1;test<=tests;test++){
		int ret=0;
		fscanf(in,"%d%d%d",&n,&k,&p);
		CLR(memo,0);
		int all=(1<<p)-1;
		memo[0][(1<<k)-1]=1;
		for(i=0;i<n;i++){
			for(mask=0;mask<(1<<p);mask++){
				if(memo[i][mask]==0)continue;
				if(!(mask&1))continue;
				memo[i+1][(mask>>1)|(1<<(p-1))]+=memo[i][mask];
				memo[i+1][(mask>>1)|(1<<(p-1))]%=mod;
				for(j=1;j<p;j++){
					if((mask&(1<<j)))continue;
					int nmask=mask | (1<<j);
					nmask>>=1;
					memo[i+1][nmask]+=memo[i][mask];
					memo[i+1][nmask]%=mod;
				}
			}
		}
		all=0;
		for(i=p-1;i>p-1-k;i--)all|=(1<<i);
		ret=memo[n-k][(1<<k)-1];
		printf("Case #%d: %d\n",test,ret);
		fprintf(out,"Case #%d: %d\n",test,ret);
	}
	return 0;
}
