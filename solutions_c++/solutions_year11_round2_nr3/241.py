#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

vector<vector<int> >adjl;
vector<vector<int> >comps;
int n,m;
int st[101],en[101],col[101],rcol[101];
vector<int>sta;
int inst[101];

void dfs(int ind,int prev)
{
	if(inst[ind])
	{
		int sz=comps.size();
		comps.resize(sz+1);
		for(int i = sta.size()-1;i>=0;--i)
		{
			comps.back().PB(sta[i]);
			if(sta[i]==ind)
				break;
		}
		return;
	}
	sta.PB(ind);
	inst[ind]=1;
	rep(i,0,adjl[ind].size())
	{
		if(adjl[ind][i]==prev)
			continue;
		dfs(adjl[ind][i],ind);
	}
	inst[ind]=0;
	sta.pop_back();
}

bool can(int ind,int mxcol)
{
	if(ind == n)
	{
		rep(i,0,comps.size())
		{
			set<int>cols;
			rep(j,0,comps[i].size())
			{
				cols.insert(col[comps[i][j]]);
			}
			if(cols.size()!=mxcol)
				return false;
		}
		return true;
	}
	rep(i,0,mxcol)
	{
		col[ind]=i;
		if(can(ind+1,mxcol))
			return true;
		col[ind]=-1;
	}
	return false;
}

int main()
{
	freopen("1.txt","rt",stdin);
	freopen("2.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d %d",&n,&m);
		rep(i,0,m)
			scanf("%d",&st[i]);
		rep(j,0,m)
			scanf("%d",&en[j]);
		adjl.clear();
		adjl.resize(n);
		comps.clear();
		rep(i,0,n)
			adjl[i].PB((i+1)%n),adjl[(i+1)%n].PB(i);
		rep(i,0,m)
			adjl[st[i]-1].PB(en[i]-1),adjl[en[i]-1].PB(st[i]-1);
		int res=1;
		sta.clear();
		memset(inst,0,sizeof(inst));
		dfs(0,-1);
		
		rep(i,2,n+1)
		{
			if(!can(0,i))
			{
				res=i-1;
				break;
			}
			memcpy(rcol,col,sizeof(col));
		}
		printf("Case #%d: ",tt+1);
		printf("%d\n",res);
		char*ss="";
		rep(i,0,n)
			printf("%s%d",ss,rcol[i]+1),ss=" ";
		printf("\n");
	}
	return 0;
}
