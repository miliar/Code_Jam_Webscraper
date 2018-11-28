#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
using namespace std;

#pragma comment(linker,"/stack:16000000")

#define ALL(v) v.begin(),v.end()
#define SZ(v) (int)v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<29;
const double eps = 1e-9;

const int MAXN = 10000;

int M[MAXN];
int cost[MAXN];
int actual_miss[MAXN];
int P;

int size = 0;

int f(int u,int l,int r)
{
	FORE(i,l,r)
		if(actual_miss[i] > M[i])
			return inf;
	
	if(u>size) return 0;


	int ret = inf;
	//play
	ret = min(ret,cost[u]+f(u*2,l,(l+r)/2) + f(u*2+1,(l+r)/2+1,r));
	
	// do not play;
	FORE(i,l,r)
		actual_miss[i]++;

	ret = min(ret,f(u*2,l,(l+r)/2) + f(u*2+1,(l+r)/2+1,r));

	FORE(i,l,r)
		actual_miss[i]--;

	return ret;
}

int main()
{
freopen ("B-large.in","r",stdin);
//freopen ("in.txt","r",stdin);
freopen ("B-large-out.txt","w",stdout);

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		cin>>P;
		FOR(i,0,1<<P)
			cin>>M[i];

		//size = (1<<(P+1)) - 1;
		size = (1<<P)-1;
		mset(actual_miss,0);

		VVI tcosts;
		int start = 1<<(P-1);
		for(;start>0;start/=2)
		{
			VI a(start);
			FOR(i,0,start)
				cin>>a[i];
			tcosts.push_back(a);
		}
		
		VI vcosts;
		for(int i = tcosts.size()-1;i>=0;--i)
			REPSZ(j,tcosts[i])
			vcosts.push_back(tcosts[i][j]);


		REPSZ(i,vcosts)
			cost[i+1] = vcosts[i];

		int ans = f(1,0,(1<<P)-1);
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}

