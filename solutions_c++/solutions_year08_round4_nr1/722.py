#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define fo(i,n) for(i=0;i<(int)(n);i++)
#define loop(i,n) for(i=0,int __n=n;i<__n;i++)
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) (a*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
FILE *in=fopen("a-large.in","r");
FILE *out=fopen("a-large.out","w");
int n,cases,z,targ;
int best[2][10009];
int gates[10009];
int chg[10009];
inline bool isleaf(int x)
{
	return x >(n-1)/2;
}
int solve(int v,int x)
{
	if(isleaf(x))
	{
		if(v!=gates[x])
			return 1<<20;
		 return 0;
	}
	int &ret=best[v][x];
	if(ret!=-1)
		return ret;
	ret=1<<20;
	int r0,r1,l0,l1,u;

	r0=solve(0,x*2+1);
	r1=solve(1,x*2+1);
	l0=solve(0,x*2);
	l1=solve(1,x*2);
	if(v==1)
	{
		//use and
		
		u=(gates[x]==1?0:1);
		if(!(u==1 && chg[x]==0))
		{
			u+=r1+l1;
			ret=min(ret,u);
		}


		//use or
		u=(gates[x]==0?0:1);
		if(!(u==1 && chg[x]==0))
		{
			u+=min(r1+l1,min(r0+l1,r1+l0));
			ret=min(ret,u);
		}
	}
	else
	{
		//use or
		u=(gates[x]==0?0:1);
		if(!(u==1 && chg[x]==0))
		{
			u+=r0+l0;
			ret=min(ret,u);
		}
		//use and
		u=(gates[x]==1?0:1);
		if(!(u==1 && chg[x]==0))
		{
			u+=min(r0+l0,min(r0+l1,r1+l0));
			ret=min(ret,u);
		}
	}

	return ret;
}

int main()
{
	fscanf(in,"%d",&cases);
	int i,j,k,ans;
	int g,c,v;
	for(z=0;z<cases;z++)
	{	
		fscanf(in,"%d%d",&n,&targ);
		CLS(best,-1);
		for(i=1;i<=n;i++)
		{
			if(isleaf(i))
				fscanf(in,"%d",&gates[i]);
			else
				fscanf(in,"%d%d",&gates[i],&chg[i]);
		}
		ans=solve(targ,1);
		if(ans>n)
			fprintf(out,"Case #%d: IMPOSSIBLE\n",z+1);
		else
		fprintf(out,"Case #%d: %d\n",z+1,ans);
	}
}