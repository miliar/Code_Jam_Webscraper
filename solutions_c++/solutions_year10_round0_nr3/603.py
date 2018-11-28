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
#define SZ(v) v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=start;i<N;++i)
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

const int inf = 1<<25;
const double eps = 1e-9;

i64 R,Capacity,N,ans;
vector<int> was;
vector<i64> groups;

pair<i64,i64> memo[1<<10];

pair<i64,i64> f(int i)
{
	if(memo[i].first!=-1)
		return memo[i];

	int u = i;

	i64 people_on_board = 0,groups_on_board = 0;
	for(;;)
	{
		if(i>=N) i = 0;
		if(people_on_board + groups[i] > Capacity)
			break;
		people_on_board+=groups[i];
		groups_on_board++;
		i++;
		if(groups_on_board == N)
			break;
	}
	return memo[u] = pair<i64,i64>(people_on_board,i%N);
}

int prefLength(int i)
{
	if(was[i] == -1)
		return 0;
	return 1 + prefLength(f(i).second);
}


i64 simulate(int i,int R)
{
	if(R==0) 
		return 0;
	pair<i64,i64> p = f(i);
	return p.first + simulate(p.second,R-1);
}

int main()
{
freopen ("C-large.in","r",stdin);
//freopen ("in.txt","r",stdin);
freopen ("output1.txt","w",stdout);



	int tt;
	cin>>tt;
	for(int cas = 1;cas<=tt;++cas)
	{
		mset(memo,-1);
		cin>>R>>Capacity>>N;
		groups.resize(N);
		FOR(i,0,N)
			cin>>groups[i];
		ans = 0;
		was = VI(N,0);
		i64 periodPos;
		i64 period;

		pair<i64,i64> p;
		int cur = 0;
		was[0] = 1;
		while(1)
		{
			p = f(cur);
			if(was[p.second] != 0)
			{
				periodPos = p.second;
				period = was[cur] - was[p.second] + 1;
				was[p.second] = -1;
				break;
			}
			was[p.second] = was[cur]+1;
			cur = p.second;
		}
		
		
		if(R<=prefLength(0))
		{
			ans = simulate(0,R);
			R = 0;
		}
		else
		{
			R-=prefLength(0);
			ans = simulate(0,prefLength(0));

			i64 k = R/period;
			
			i64 periodEarn = simulate(periodPos,period);
			ans+=k*periodEarn;

			i64 left = R%period;
			ans+= simulate(periodPos,left);
		}
		printf("Case #%d: %lld\n",cas,ans);
	}

	return 0;
}

