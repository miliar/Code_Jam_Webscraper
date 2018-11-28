#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 2000
#define INF 100000000

int x1[MAX],x2[MAX],y1[MAX],y2[MAX];
int n;
int adj[MAX][MAX],visited[MAX];
int mn,mx,mxx,mxy;

void dfs(int i){
	int j;
	visited[i]=1;
	mn=min(mn,x1[i]+y1[i]);
	//mx=max(mx,x2[i]+y2[i]);
	mxx=max(mxx,x2[i]);
	mxy=max(mxy,y2[i]);
	for (j=0; j<n; j++){
		if (adj[i][j] && !visited[j]) dfs(j);
	}
}

int main(){
	int t,i,j,k,tt,u;
	cin>>t;
	for (u=1; u<=t; u++){
		cin>>n	;
		
		for (i=0; i<n; i++){
			cin>>x1[i]>>y1[i]>>x2[i]>>y2[i];
			visited[i]=0;
		}
		for (i=0; i<n; i++){
			for (j=0; j<n; j++)
				adj[i][j]=0;
		}
		for (i=0; i<n; i++){
			for (j=0; j<n; j++){
				if (i==j) continue;
				if (x1[j]==x2[i]+1 && y1[j]==y2[i]+1) continue;
				if (x1[i]==x2[j]+1 && y1[i]==y2[j]+1) continue;
				if (x1[i]<=x2[j]+1 && x1[j]<=x2[i]+1 && y1[i]<=y2[j]+1 && y1[j]<=y2[i]+1) adj[i][j]=adj[j][i]=1;
			}
		}
		tt=0;
		for (i=0; i<n; i++){
			if (visited[i]) continue;
			mn=INF;
			mx=-INF;
			mxx=-INF;
			mxy=-INF;
			dfs(i);
			mx=mxx+mxy;
			if (mx-mn+1>tt) tt=mx-mn+1;
		}
		cout<<"Case #"<<u<<": "<<tt<<endl;
	}
	return 0;
}
