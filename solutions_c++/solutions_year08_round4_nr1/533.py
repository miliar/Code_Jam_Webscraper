#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstdarg>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

#define LL __int64
#define ALL(v) v.begin(), v.enode()
#define SZ(v) v.size()
#define VI vector<int>
#define pb push_back
#define debug(x) cerr<<#x<<"="<<i<<enodel
#define f0(i,n) for(i=0;i<n;i++)
#define f1(i,n) for(i=1;i<=n;i++)

inline void OUT(const char* fmt, ...)
{
	va_list va;
	va_start(va,fmt);
	vprintf(fmt,va);
	vfprintf(stderr,fmt,va);
	va_end(va);
}
//#define OUT printf

const int maxn=10000*3;
const int INF=1<<25;

struct Node {
	int t0,t1;
	int g,c;
}node[maxn];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int cas;
	scanf("%d",&cas);
	for(int lv=1;lv<=cas;lv++) {
		OUT("Case #%d: ",lv);
		int i,j,k,m,re;
		scanf("%d%d",&m,&re);
		k=(m-1)/2;
		f1(i,k) {
			scanf("%d%d",&node[i].g,&node[i].c);
		}
		for(;i<=m;i++) {
			scanf("%d",&k);
			if(k) {
				node[i].t0=INF;
				node[i].t1=0;
			} else {
				node[i].t0=0;
				node[i].t1=INF;
			}
		}
		for(i=(m-1)/2;i>0;i--) {
			int u=2*i, v=u+1;
			node[i].t0=_MIN(node[u].t0,node[v].t0);
			if(!node[i].g) {
				if(!node[i].c) node[i].t0=node[u].t0+node[v].t0;
				else node[i].t0=_MIN(node[u].t0+node[v].t0,node[i].t0+1);
			}
			node[i].t1=_MIN(node[u].t1,node[v].t1);
			if(node[i].g) {
				if(!node[i].c) node[i].t1=node[u].t1+node[v].t1;
				else node[i].t1=_MIN(node[u].t1+node[v].t1,node[i].t1+1);
			}
			node[i].t0=_MIN(node[i].t0,INF);
			node[i].t1=_MIN(node[i].t1,INF);
		}
		int ans;
		if(re) {
			ans=node[1].t1;
		} else ans=node[1].t0;
		if(ans<INF) {
			OUT("%d\n",ans);
		} else {
			OUT("IMPOSSIBLE\n");
		}
	}
	return 0;
}
