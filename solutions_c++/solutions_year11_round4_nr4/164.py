//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long
#define CLR(x) memset(x,0,sizeof x)
#define SET(x,y) memset(x,y,sizeof x)


#define mx 500
int ds[mx],r,n,h;
vector < int > g[mx];
bool vis[mx],f,chk[mx],pr[mx][mx];

void dfs(int p) {
	if(p==1) {
		int i,t=0;
		for(i=0;i<n;i++) if(!chk[i] && vis[i]) t++;
		//cout<<t<<'\n';
		if(t>r) {
			r=t;
			//if(r==h) f=1;
		}
		return;
	}
	chk[p]=1;
	int i,j=g[p].size(),d=ds[p]+1;
	for(i=0;i<j;i++) if(!chk[g[p][i]]) {
		pr[p][i]=vis[g[p][i]];
		vis[g[p][i]]=1;
		//cout<<p<<' '<<g[p][i]<<' '<<vis[g[p][i]]<<'\n';
	}
	for(i=0;i<j;i++) if(ds[g[p][i]]==d) {
		dfs(g[p][i]);
		if(f) return;
	}
	for(i=0;i<j;i++) if(!chk[g[p][i]]) {
		vis[g[p][i]]=pr[p][i];
		//cout<<p<<' '<<g[p][i]<<' '<<vis[g[p][i]]<<'\n';
	}
	chk[p]=0;
}
	


int main() {
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);
	int i,j,k,d,I,T,u,w,v;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n>>w;
		for(i=0;i<n;i++) g[i].clear();
		while(w--) {
			scanf("%d,%d",&u,&v);
			g[u].push_back(v);
			g[v].push_back(u);
		}
		queue < int > q;
		memset(ds,63,sizeof ds);
		q.push(0);
		ds[0]=0;
		while(!q.empty()) {
			u=q.front();
			q.pop();
			j=g[u].size();
			d=ds[u]+1;
			for(i=0;i<j;i++) if(ds[g[u][i]]>d) {
				ds[g[u][i]]=d;
				q.push(g[u][i]);
			}
		}
		h=n-ds[1]+1;
		r=0;
		f=0;
		CLR(vis);
		CLR(chk);
		CLR(pr);
		dfs(0);
		printf("Case #%d: %d %d\n",I,ds[1]-1,r);
	}
	return 0;
}

