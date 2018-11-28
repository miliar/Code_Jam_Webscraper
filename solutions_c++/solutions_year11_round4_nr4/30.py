#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
 
typedef long long LL;
typedef vector<int> vi;
typedef vector< pair<int, int> > vii;
#define MP(x,y) make_pair(x, y)
 

vi a[500];
int hasedge[500][500];
int dp[500][500];
int dist[500];
vi d[500];
int mark[500], mxans=0;
/*
void go(int lev, int cnt, int x) {
	//fprintf(stderr, "%d %d %d\n", lev, cnt, x);
	if(lev==dist[1]) {
		if(!hasedge[x][1]) return;
		if(cnt > mxans) mxans = cnt;
		return;
	}
	int i, j;
	for(i=0;i<a[x].size();i++) {
		if(dist[a[x][i]]!=lev) continue;
		int v = a[x][i];
		if(mark[v]==-1) {mark[v]=lev; ++cnt;}
		for(j=0;j<a[v].size();j++)
			if(mark[a[v][j]]==-1) {
				mark[a[v][j]]=lev;
				++cnt;
			}
		go(lev+1, cnt, v);
		if(mark[v]==lev) {mark[v]=-1;--cnt;}
		for(j=0;j<a[v].size();j++)
			if(mark[a[v][j]]==lev) {
				mark[a[v][j]]=-1;
				--cnt;
			}
	}
}
*/
int main(void) {
    int T, cs, x, y, i, n, m, j, k, u, v, w;
    scanf("%d", &T);
    for(cs=1;cs<=T;cs++) {
		scanf("%d%d", &n, &m);
		memset(hasedge,0,sizeof(hasedge));
		for(i=0;i<m;i++){
			scanf("%d,%d", &x, &y);
			a[x].push_back(y);
			a[y].push_back(x);
			hasedge[x][y]=hasedge[y][x]=1;
		}
		memset(dist,-1,sizeof(dist));
		dist[0] = 0;
		queue<int> Q;
		Q.push(0);
		d[0].push_back(0);
		while(!Q.empty()) {
			x = Q.front();
			Q.pop();
			for(i=0;i<a[x].size();i++) {
				if(dist[a[x][i]]==-1) {
					dist[a[x][i]] = dist[x]+1;
					Q.push(a[x][i]);
					d[dist[x]+1].push_back(a[x][i]);
				}
			}
		}

		memset(dp, -1, sizeof(dp));
		

		memset(mark, -1, sizeof(mark));
		mark[0] = 0;
		int cc=1;
		for(i=0;i<a[0].size();i++) {
			if(mark[a[0][i]]==-1) {
				mark[a[0][i]]=0;
				++cc;
			}
		}
		dp[0][0] = cc;
		for(i=0;i<dist[1];i++){
			vi &p = d[(i==0? i:i-1)];
			vi &q = d[i];
			for(j=0;j<p.size();j++)
				for(k=0;k<q.size();k++)
					if(p[j]==q[k] || hasedge[p[j]][q[k]]) {
						
						int u = p[j];
						int v = q[k];
					//	printf("dp[%d][%d]=%d\n", u, v, dp[u][v]);
						for(w=0;w<a[v].size();w++) {
							int x = a[v][w];
							if(dist[x]==dist[v]+1) {
								int dd = dp[u][v];
								for(y=0;y<a[x].size();y++) {
									int z=a[x][y];
									if(z!=x && v!=z && u!=z && !hasedge[u][z] && !hasedge[v][z])
										dd++;
								}
								if(dp[v][x] < dd)
									dp[v][x] = dd;
							}
						}
					}
		}
			
		mxans = 0;
//		go(1, cc, 0);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(j!=1 && i!=1 && dist[i]<dist[1] && dist[j]<dist[1] && hasedge[j][1] && dp[i][j] > mxans) {
//					printf("i=%d, j=%d\n", i, j);
					mxans = dp[i][j];
				}
		for(i=0;i<n;i++) {
			a[i].clear();
			d[i].clear();
		}
        printf("Case #%d: %d %d\n", cs, dist[1]-1, mxans - (dist[1]));
		fprintf(stderr, "Case #%d: %d %d\n", cs, dist[1]-1, mxans - (dist[1]));
    }
    return 0;
}

