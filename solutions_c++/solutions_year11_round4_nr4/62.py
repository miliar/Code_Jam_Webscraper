#include "hpmv.h"

hello

int N;
vector<int> adj[512];
int W;
in(N,W);
FOR(i,W){
	int a,b;
	in(a);inc();in(b);
	adj[a].push_back(b);
	adj[b].push_back(a);
}
bool vis[512];
memset(vis,0,sizeof(vis));
typedef pair<int,vector<int> > tiv;
queue<pair<int,vector<int> > > bfs;
bfs.push(pair<int,vector<int> >(0, array(0)));
vis[0]=true;
while(!bfs.empty()){
	tiv ele = bfs.front();
	
	int v = ele.second.back();
	vis[v]=true;
	if(v==1){
		//finish.
		out((int)(ele.second.size()-2), " ");
		int bestsize = ele.first;
		tiv sol;
		int maxt = 0;
		bool threat[512];
		while(!bfs.empty()){
			sol = bfs.front();
			bfs.pop();
			//out("exam:");outarr(sol.second);ent;
			if(sol.first!=bestsize) break;
			if(sol.second.back()!=1) continue;
			memset(threat,0,sizeof(threat));
			
			for(int i=0;i<sol.second.size()-1;i++){
				int myv = sol.second[i];
				threat[myv]=true;
				for(int j=0;j<adj[myv].size();j++){
					
					threat[adj[myv][j]]=true;
				}
				
			}
			int totalthreat = 0;
			for(int i=0;i<N;i++)
				if(threat[i]) totalthreat++;
			//out("vector: ");outarr(sol.second);ent;
			//out("threats: ");outarr(N,threat);ent;
			totalthreat-=sol.second.size()-1;
			infl(maxt,totalthreat);
			
		}
		out(maxt);ent;return;
	}
	else bfs.pop();
	for(int i=0;i<adj[v].size();i++){
		if(!vis[adj[v][i]])
		{
			vector<int> newvec = ele.second;
			newvec.push_back(adj[v][i]);
			tiv newele = tiv(ele.first+1, newvec);
			bfs.push(newele);
		}
	}
}






cya
