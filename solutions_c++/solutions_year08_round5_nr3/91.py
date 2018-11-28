#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define i64 __int64
#define INF 1e10
#define EPS 1e-11
#define SIZE 85
#define MAXN (80*80+5)

char g[SIZE][SIZE];

vector<int>adj[MAXN];
int matchL[MAXN],matchR[MAXN];
bool seen[MAXN];

int n,m,tot;
int moves[][2] = {
	{0,-1},{0,1},{-1,-1},{-1,1}
};

bool bpm(int u) {
	if(seen[u]) return false;
	seen[u] = 1;

	int i,v;
	rep(i,adj[u].size()) {
		v = adj[u][i];
		if(matchR[v] == -1 || bpm(matchR[v]) ) {
			matchL[u] = v;
			matchR[v] = u;
			return true;
		}
	}
	return false;
}

int main() {
	int T,kase=1;
	int i,j,k;
	int nx,ny;
	int ct,res;
	scanf("%d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d %d",&n,&m);
		rep(i,n) {
			scanf(" %s",g[i]);
		}
		tot = n * m;

		memset(matchL,-1,sizeof(matchL));
		memset(matchR,-1,sizeof(matchR));
		rep(i,tot) adj[i].clear();

		rep(i,n) rep(j,m) if(g[i][j] == '.') {
			rep(k,4) {
				nx = i + moves[k][0];
				ny = j + moves[k][1];
				if(nx < 0 || ny < 0 || nx >= n || ny >= m || g[nx][ny] == 'x') continue;
				//if(nx*m + ny <= i*m+j) continue;
				adj[i*m+j].push_back(nx*m+ny);
				adj[nx*m+ny].push_back(i*m+j);
			}
		}

		ct = 0;
		/*
		rep(i,n) rep(j,m) {
			cout<<i<<' '<<j<<endl;
			rep(k,adj[i*m+j].size()) cout<<adj[i*m+j][k]<<endl;
			cout<<endl;
		}*/
		rep(i,n) rep(j,m) if(g[i][j] == '.' && matchL[i*m+j] == -1) {
			memset(seen,0,sizeof(seen));
			if(bpm(i*m+j)) ct++;
		}

		//cout<<ct<<endl;
		//cout<<ct<<endl;
		tot = 0;
		rep(i,n) rep(j,m) if(g[i][j] == '.') tot++;
		res = tot - ct/2;
		printf("%d\n",res);
	}
	return 0;
}