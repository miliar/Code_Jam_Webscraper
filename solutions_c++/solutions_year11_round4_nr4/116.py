#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9
#define EPS LD(1e-9)
#define DINF LD(1e50)

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef double LD;

const int mn=38;
int n;
VI alist[mn];
int anst;
int dist[mn][mn];

void go(VI v){
	int u=v[ v.sz-1 ];
	if(u==1){
		int cnt=1;
		FOR(i,2,n){
			bool ok=1;
			REP(j,v.sz)	if(v[j]==i)	ok=0;
			if(!ok)	continue;
			ok=0;
			REP(j,v.sz-1)	if(dist[i][ v[j] ]==1)	{ok=1;break;}
			if(ok)	cnt++;
		}
		anst>?=cnt;
		return ;
	}
	REP(i,n)	if(dist[u][i]==1 && dist[u][1]==1+dist[i][1]){
		VI nv=v;
		nv.pb(i);
		go(nv);	
	}	
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		n=GI;
		int m=GI;
		REP(i,n)	alist[i].clear();
		REP(i,m){
			int u,v;
			scanf("%d,%d",&u,&v);
			alist[u].pb(v);
			alist[v].pb(u);	
		}
		REP(i,n)	REP(j,n)	dist[i][j]=INF;
		REP(i,n)	dist[i][i]=0;
		REP(u,n)	REP(i,alist[u].sz)	dist[u][ alist[u][i] ]=1;
		REP(k,n)	REP(i,n)	REP(j,n)	dist[i][j]<?=dist[i][k]+dist[k][j];
		int ansc=dist[0][1]-1;
		anst=1;
		go(VI(1,0));
		printf("Case #%d: %d %d\n",kase,ansc,anst);
		
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
