//Author: Fluorine
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

void dfs(int);
int a[10],tot,n,m,x,y;
bool v1[10][10],v2[10][10],visit[10],t;

int main(){
	scanf("%d",&tot);
	for (int cases=0;cases<tot;++cases){
		memset(v1,false,sizeof(v1));
		memset(v2,false,sizeof(v2));
		scanf("%d",&n);
		for (int i=1;i<n;++i){
			scanf("%d%d",&x,&y);
			v1[x][y]=v1[y][x]=true;
		}
		scanf("%d",&m);
		for (int i=1;i<m;++i){
			scanf("%d%d",&x,&y);
			v2[x][y]=v2[y][x]=true;
		}
		memset(visit,false,sizeof(visit));
		t=false;
		dfs(1);
		if (t) printf("Case #%d: YES\n",cases+1);
		else printf("Case #%d: NO\n",cases+1);
	}
	return 0;
}

void dfs(int dep){
	if (dep>m){
		bool tt=true;
		for (int i=1;i<m;++i){
			for (int j=i+1;j<=m;++j)
				if (v2[i][j]!=v1[a[i]][a[j]]){
					tt=false;
					break;
				}
			if (!tt) break;
		}
		if (tt) t=true;
		return;
	}
	for (int i=1;i<=n;++i){
		if (visit[i]) continue;
		visit[i]=true;
		a[dep]=i;
		dfs(dep+1);
		if (t) return;
		visit[i]=false;
	}
}
