#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
#include <complex>
#include <queue>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define rep(i,X,n) for( int (i) = (X) ; (i)<(n) ; (i) ++)
#define repit(it,X,n) for(__typeof((X)) it = (X) ; (it) != (n) ; (it)++)
#define PRINT(...) fprintf(stdout,__VA_ARGS__)
#define ALL(X) (X).begin(),(X).end()

struct Time
{
	int s;
	int e;
	Time(int a,int b)
	:s(a),e(b)
	{
	}
	Time()
	{
	}
};

vector<vector<int> > adjl;
vector<Time> tim;

int l[301];
int r[301];
int vis[301];
int n,m;

bool match(int ind)
{
	rep(i,0,adjl[ind].size())
	{
		int j = adjl[ind][i];
		if(vis[j])
			continue;
		vis[j] = 1;
		if(r[j] == -1 || match(r[j]))
		{
			l[ind] = j;
			r[j] = ind;
			return true;
		}
	}
	return false;
}

int Max_Match()
{
	memset(l,-1,sizeof(l));
	memset(r,-1,sizeof(r));
	int res=0;
	rep(i,0,n+m)
	{
		memset(vis,0,sizeof(vis));
		if(l[i] == -1)
			if(match(i))
				res++;
	}
	return res;
}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("out.out","wt",stdout);
	
	int t;
	int T,a,b,c,d;
	
	scanf("%d",&t);
	rep(tt,0,t)
	{
		adjl.clear();
		tim.clear();
		scanf("%d",&T);
		scanf("%d %d",&n,&m);
		adjl.resize(2*(n+m));
		rep(i,0,n+m)
		{
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			tim.PB(Time(a*60+b,c*60+d));
		}
		rep(i,0,n)
		{
			rep(j,0,m)
			{
				if(tim[i].e+T<=tim[j+n].s)
				{
					adjl[i].PB(n+j);
				}
			}
		}
		rep(i,n,n+m)
		{
			rep(j,0,n)
			{
				if(tim[i].e+T<=tim[j].s)
				{
					adjl[i].PB(j);
				}
			}
		}
		
		int x = Max_Match();
		
		int xx=0,yy=0;
		rep(i,0,n)
		{
			if(r[i]==-1)
				xx++;
		}
		rep(i,n,n+m)
			if(r[i] == -1)
				yy++;
		
/*		printf("%d\n",x);
		rep(i,0,n+m)
		{
			printf("%d %d\n",l[i],r[i]);
		}*/
		printf("Case #%d: %d %d\n",tt+1,xx,yy);
	}
	return 0;
}
