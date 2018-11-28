#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define pii pair<int,int>
#define pdd pair<double,double>
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).size())
#define C(a) memset((a),0,sizeof(a))
#define VI vector <int>
#define ll long long

int a,b,c,d,i,j,n,m,k,kolt;
VI sm[11],back[11];
int beg[11];
int ans[11],cnt[1<<8];

bool fnd(int v,int s,int mask,int cz,int pr=-1)
{
	if (v!=s && s!=pr)
	{
		rept(i,L(back[v]))
		{
			if (back[v][i]!=s) continue;
			if (cnt[mask]+cz<c) return 0;
		}
	}
	if (v==n-1) return 1;
	rept(i,L(sm[v]))
	{
		int w=sm[v][i];
		int nmask=mask,nz=cz;
		if (ans[w]==-1) ++nz; else
		nmask|=1<<ans[w];
		if (!fnd(w,s,nmask,nz,v)) return 0;
	}
	return 1;
}
inline bool check(int v)
{
	if (!fnd(v,v,1<<ans[v],0)) return 0; else
	return 1;
}
bool rec(int v)
{
	if (v>=n) return 1;
	rept(i,c)
	{
		if (!v && i) return 0;
		ans[v]=i;
		bool ok=1;
		FORD(j,v,0) if (!check(j))
		{
			ok=0;
			break;
		}
		if (!ok)
		{
			ans[v]=-1;
			continue;
		}
		if (rec(v+1)) return 1;
		ans[v]=-1;
	}
	return 0;
}
inline bool solve(int c)
{
	memset(ans,-1,sizeof(ans));
	::c=c;
	return rec(0);
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rept(i,1<<8)
	{
		rept(j,8) if (i&1<<j) ++cnt[i];
	}
	rep(hod,kolt)
	{
		cerr<<hod<<" "<<1.0*clock()/CLOCKS_PER_SEC<<endl;
		scanf("%d%d",&n,&m);
		rept(i,n) sm[i].clear(),back[i].clear();
		rept(i,n-1) sm[i].pb(i+1);
		back[n-1].pb(0);
		rept(i,m) scanf("%d",&beg[i]),--beg[i];
		rept(i,m)
		{
			scanf("%d",&a); --a;
			sm[beg[i]].pb(a);
			back[a].pb(beg[i]);
		}
		
		printf("Case #%d: ",hod);
		if (!m)
		{
			printf("%d\n",n);
			rept(i,n)
			{
				if (i) printf(" ");
				printf("%d",i+1);
			}
			printf("\n");
			continue;
		}
		k=1;
		FORD(i,5,1)
		{
			if (solve(i))
			{
				k=i;
				break;
			}
		}

		printf("%d\n",k);
		rept(i,n)
		{
			if (i) printf(" ");
			printf("%d",ans[i]+1);
		}
		printf("\n");
	}
}
