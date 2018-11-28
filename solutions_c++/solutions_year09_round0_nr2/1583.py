#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;

#define valid(x,y) (x>=0 && y>=0 && x<m && y<n)
int m,n;
int x11[]={-1,0,0,1},y11[]={0,-1,1,0};
int visited[200][200],arr[200][200];
bool visited2[200][200];
vector<PI> graph[200][200];

void dfs1(int i,int j){
	visited2[i][j]=1;
	int min1=arr[i][j],X=-1,Y=-1;
	REP(ind,4)if(valid(i+x11[ind],j+y11[ind])){
		int i1=i+x11[ind],j1=j+y11[ind];
		if(arr[i1][j1]<min1){
			min1=arr[i1][j1];
			X=i1;
			Y=j1;
		}
	}
	if(X!=-1){
		graph[i][j].PB(make_pair(X,Y));
		graph[X][Y].PB(make_pair(i,j));
		if(!visited2[X][Y])dfs1(X,Y);
	}
	return;
}
void dfs2(int i,int j,int level){
	visited[i][j]=level;
	EACH(it,graph[i][j]){
		int i1=it->first,j1=it->second;
		if(!visited[i1][j1])dfs2(i1,j1,level);
	}
	return;
}
int main(){
	int t;cin>>t;
	FOR(cas,1,t+1){
		cout<<"Case #"<<cas<<":\n";
		cin>>m>>n;
		REP(i,m)REP(j,n)graph[i][j].clear();
		REP(i,m)REP(j,n)scanf("%d",&arr[i][j]);
		int label=1;
		memset(visited,0,sizeof(visited));
		memset(visited2,0,sizeof(visited));
		REP(i,m)REP(j,n){
			if(!visited2[i][j])dfs1(i,j);
		}
		REP(i,m)REP(j,n){
			if(!visited[i][j]){
					dfs2(i,j,label);
					label++;
			}
		}
		int avail=0;
		char allot[label+10];
		memset(allot,0,sizeof(allot));
		REP(i,m){
			REP(j,n){
				if(allot[visited[i][j]]==0){
					allot[visited[i][j]]=avail+'a';
					avail++;
				}
				printf("%c%c",allot[visited[i][j]],((j==n-1)?'\n':' '));
			}
		}
	}
}
