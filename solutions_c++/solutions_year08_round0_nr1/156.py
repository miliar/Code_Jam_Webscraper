#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

VS sr,sq;
int ns,nq,dp[110][1050],isq[1050];

int solve(int si,int qi)
{
	int ret = 10000000;
	if(dp[si][qi]!=-1)return dp[si][qi];
	if(qi==nq)return dp[si][qi]=0;
	int i,j,k;
	if(isq[qi]!=si)ret = solve(si,qi+1);
	else
	{
		for(i=0;i<ns;i++)
		{
			if(si==i)continue;
			int t = 1+solve(i,qi);
			ret = min(ret,t);
		}
	}
	return dp[si][qi]=ret;
}


void main()
{
	int probnum,numtest;
	string ins;
	getline(cin,ins);
	numtest=atoi(ins.c_str());
	for(probnum=0;probnum<numtest;probnum++)
	{
		int i,j,k;
		printf("Case #%d: ",probnum+1);
		getline(cin,ins);
		ns=atoi(ins.c_str());
		sq.clear();
		sr.clear();
		for(i=0;i<ns;i++)
		{
			getline(cin,ins);
			sr.push_back(ins);
		}
		getline(cin,ins);
		nq=atoi(ins.c_str());
		for(i=0;i<nq;i++)
		{
			getline(cin,ins);
			sq.push_back(ins);
		}
		memset(dp,-1,sizeof(dp));
		for(i=0;i<ns;i++)for(j=0;j<nq;j++)if(sr[i]==sq[j])isq[j]=i;
		int swt=1000000;
		for(i=0;i<ns;i++)
		{
			int t = solve(i,0);
			swt=min(swt,t);
		}
		cout<<swt<<endl;
	}
}