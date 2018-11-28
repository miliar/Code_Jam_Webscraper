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

FILE *in=fopen("QC.in","r");
FILE *out=fopen("QC.out","w");

int k;

long long next[1001],cost[1001];

long long solve(int cur,vector < int > ar,int r)
{
	int i,j;
	int n=ar.size();
	CLR(next,-1);
	CLR(cost,0);
	long long ret=0;
	for(i=0;i<r;i++){
		if(next[cur]!=-1)break;
		int last=cur;

		long long sum=0;
		for(j=0;j<n;j++){
			if(sum+ar[cur]>k)break;
			sum+=ar[cur];
			cur=(cur+1)%n;
		}
		ret+=sum;
		next[last]=cur;
		cost[last]=sum;
	}
	if(i==r)return ret;
	r-=i;
	int start=cur;
	long long cyclength=0,cyccost=0;
	do{
		cyclength++;
		cyccost+=cost[cur];
		cur=next[cur];
	}while(cur!=start);
	ret+=(r/cyclength)*cyccost;
	r%=cyclength;

	for(i=0;i<r;i++){
		long long sum=0;
		for(j=0;j<n;j++){
			if(sum+ar[cur]>k)break;
			sum+=ar[cur];
			cur=(cur+1)%n;
		}
		ret+=sum;
	}
	return ret;
}



int main()
{
	int i,j,r,n;
	int ar[1001];
	int test,tests;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		fscanf(in,"%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)fscanf(in,"%d",&ar[i]);
		vector < int > t;
		for(i=0;i<n;i++)t.push_back(ar[i]);
		long long ret=solve(0,t,r);
		fprintf(out,"Case #%d: %lld\n",test,ret);
	}
	return 0;
}