#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<VPII> VVPII;

void run(int casenr) {
	int n,m; scanf("%d%d",&n,&m);
	VVI e(n); VVI adj(n,VI(n,0)); REP(i,m) { int x,y; scanf("%d,%d",&x,&y); e[x].PB(y); e[y].PB(x); adj[x][y]=adj[y][x]=1; }
//	printf("%d %d\n",n,m); REP(i,n) { printf("%d:",i); sort(e[i].begin(),e[i].end()); REPSZ(j,e[i]) printf(" %d",e[i][j]); puts(""); }

	VI d(n,-1);
	queue<int> q;
	d[0]=0; q.push(0);
	while(!q.empty()) { int at=q.front(); q.pop(); REPSZ(i,e[at]) { int to=e[at][i]; if(d[to]!=-1) continue; d[to]=d[at]+1; q.push(to); } }

	VPII edges;
	REP(at,n) REPSZ(i,e[at]) { int to=e[at][i]; if(d[to]!=d[at]+1) continue; if(d[at]>=d[1]) continue; edges.PB(MP(at,to)); }

	VPII order; REPSZ(i,edges) order.PB(MP(-d[edges[i].first],i)); sort(order.begin(),order.end());

	int ret=-1;
	VI best(SZ(edges),-1);
	REPSZ(i,order) {
		int ind=order[i].second,at=edges[ind].first,to=edges[ind].second;
		if(to==1) {
			best[ind]=SZ(e[at]);
		} else {
			REP(j,i) {
				int ind2=order[j].second,at2=edges[ind2].first,to2=edges[ind2].second;
				if(at2!=to) continue;
				if(best[ind2]==-1) continue;
				int cur=best[ind2]-1;
				REP(k,n) if(k!=at&&k!=to&&k!=to2&&adj[at][k]&&!(adj[to][k]||to2!=1&&adj[to2][k])) ++cur;
				if(best[ind]==-1||cur>best[ind]) {
//					printf("\t(%d,%d)=%d\n",at2,to2,cur);
					best[ind]=cur;
				}
			}
		}
//		printf("(%d,%d)=%d\n",at,to,best[ind]);
		if(at==0&&(ret==-1||best[ind]>ret)) ret=best[ind];
	}

	printf("Case #%d: %d %d\n",casenr,d[1]-1,ret);
}

int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
	return 0;
}

 
