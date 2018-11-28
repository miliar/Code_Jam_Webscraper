#include <stdio.h> 
#include <stdlib.h> 
#include <ctype.h> 
#include <string.h> 
#include <math.h> 
#include <algorithm>
#include <functional>
#include <vector> 
#include <set>
#include <queue>
#include <string> 
#include <iostream> 
#include <sstream>  
using namespace std; 

#define fo(i,n) for(i=0;i<(n);++i)
#define fo1(i,y,n) for(i=y; i<(n) ;i++)
#define pb push_back

typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ;  

long long x[1002],ret;
int n;

void solve (long long s, long long e, long long sum1, long long sum2, int i)
{
	if(i==n)
	{
		if(s != e) return ;
		if(sum1> ret && sum2) ret = sum1;
		if(sum2> ret && sum1) ret = sum2;
		return ;
	}
	solve(s^x[i],e,sum1+x[i],sum2,i+1);
	solve(s,e^x[i],sum1,sum2+x[i],i+1);
}

int main()
{
	FILE *in=fopen("C-small-attempt2.in","r");
	FILE *out=fopen("C-output.txt","w");
	int q,Q,N,i,j;
	char ch[5];
	fscanf(in,"%d",&q);
	for(Q=1;Q<=q;Q++)
	{
		fscanf(in,"%d",&n);
		for(N=0; N<n; N++)
			fscanf(in,"%lld",&x[N]);
		ret = 0;
		solve(0,0,0,0,0);
		if(ret!= 0)
			fprintf(out,"Case #%d: %lld\n",Q,ret);
		else
			fprintf(out,"Case #%d: NO\n",Q);
	}
	return 0;
}















