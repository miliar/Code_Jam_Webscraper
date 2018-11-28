/**
* @author Gareve
* @problem
* @judge
*/
#define DEBUG
#ifndef NDEBUG	
	#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;
#else
	#define DBG(a) ;
#endif
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <queue>
#include <set>
#include <map>
#define P pair<int,vector<int> >

using namespace std;

int n,w;
void resuelva(){
	cin>>n>>w;
	int x,y;
	string str;
	vector<int> g[40];
	vector<set<int> > tr[40];
	for(int i=1;i<=w;i++){
		cin>>str;
		sscanf(str.c_str(),"%d,%d",&x,&y);
		//printf(":%d %d\n",x,y);
		g[x].push_back(y);
		g[y].push_back(x);
	}
	vector<int> dist(n,-1);
	dist[0]=0;
	queue<int> q;
	q.push(0);

	set<int> st;
	for(int i=0;i<g[0].size();i++)st.insert(g[0][i]);
	tr[0].push_back(st);
	while(!q.empty()){
		x = q.front();
		q.pop();
		//printf("[%d,%d]",x,dist[x]);

		for(int i=0;i<g[x].size();i++){
			y = g[x][i];
			if(dist[y]==-1 or dist[x]+1<dist[y]){
				dist[y]=dist[x]+1;
				q.push(y);
				/*for(int j=0;j<tr[x].size();j++){
					st = set<int>(tr[x][j].begin(),tr[x][j].end());
					for(int k=0;k<g[y].size();k++)
						st.insert(g[y][k]);
					if(st.find(y)!=st.end())st.erase(st.find(y));
					if(st.find(x)!=st.end())st.erase(st.find(x));
					tr[y].push_back(st);
				}*/
			}
		}
	}
	int res=-1;
	queue<P > qq;
	qq.push(P(1,vector<int>(0)));
	vector<int> vc,vv;
	int tmp;
	while(!qq.empty()){
		x = qq.front().first;
		vc = qq.front().second;
		qq.pop();

		if(x==0){
			set<int> un;
			for(int i=0;i<vc.size();i++){
				x = vc[i];
				//printf("[%d]",x);
				for(int j=0;j<g[x].size();j++){
					y = g[x][j];
					un.insert(y);
				}
			}
			//printf("\n");
			for(int i=0;i<vc.size();i++)if(un.find(vc[i])!=un.end())un.erase(un.find(vc[i]));
			//for(set<int>::iterator it=un.begin();it!=un.end();it++)printf("(%d)",*it);printf("\n");
			tmp = un.size();
			if(tmp>res)
				res=tmp;
			continue;
		}

		for(int i=0;i<g[x].size();i++){
			y = g[x][i];
			if(dist[y]+1 == dist[x]){
				vv.assign(vc.begin(),vc.end());
				vv.push_back(y);
				qq.push(P(y,vv));
			}
		}
	}


	//int res=-1,t;
	/*for(int i=0;i<g[1].size();i++){
		y = g[1][i];
		if(dist[y]!=dist[1]-1)continue;
		for(int j=0;j<tr[y].size();j++){
			//for(set<int>::iterator it=tr[y][j].begin();it!=tr[y][j].end();it++)printf("%d ",*it);printf("\n");
			t = tr[y][j].size();
			if(t>res)
				res = t;
		}
	}*/
	//for(int i=0;i<n;i++)printf("   %d: %d\n",i,dist[i]);
	printf("%d %d\n",dist[1]-1,res);
}
int main(){
   int _q;
   cin>>_q;
   for(int i=1;i<=_q;i++){
      printf("Case #%d: ",i);
      resuelva();
   }
}

