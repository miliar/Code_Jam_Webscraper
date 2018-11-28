#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
using namespace std;

const int maxn	=	10005;

int d[maxn],len[maxn],tar,n,l[maxn];
bool vis[maxn];

inline bool solve()
{
	queue<int> q;
	q.push(0);
	memset(vis,false,sizeof(vis));
	vis[0]=true;
	
	memset(l,0,sizeof(l));
	l[0]=min(d[0],len[0]);
	while (q.size()){
		int u=q.front();
		if (d[u]+l[u]>=tar) return true;
		vis[u]=false;
		q.pop();
		for (int j=0;j<n;++j)
		if (abs(d[j]-d[u])<=l[u]){
			int limit=min(abs(d[j]-d[u]),len[j]);
			if (limit>l[j]){
				l[j]=limit;
				if (!vis[j]){
					vis[j]=true;
					q.push(j);
				}
			}
		}
	}
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test){
		scanf("%d",&n);
		for (int i=0;i<n;++i){
			scanf("%d%d",&d[i],&len[i]);
		}
		scanf("%d",&tar);
		if (solve()) printf("Case #%d: YES\n",test);
		else printf("Case #%d: NO\n",test);
	}
	return 0;
}
