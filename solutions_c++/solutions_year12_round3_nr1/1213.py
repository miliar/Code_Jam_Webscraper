#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <stack>
using namespace std;
const double PI = 3.14159265358979323846;

struct edge {
  int src, dst;
  edge(int s, int d)
    : src(s), dst(d) { }
};

typedef vector<edge> vertex;
typedef vector<vertex> graph;

bool used[1000];

bool dfs(int a,const graph& g){
	if(used[a])return true;
	used[a] = true;
	for(int i = 0,l = g[a].size(); i < l; i++){
		if(dfs(g[a][i].dst,g))return true;
	}
	return false;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int X = 1; X <= T; X++){
		//memset(used,0,sizeof(used));
		int n;
		cin>>n;
		graph g(n);
		for(int i = 0; i < n; i++){
			int m;
			cin>>m;
			for(int j = 0; j < m; j++){
				int a;
				cin>>a;
				g[i].push_back(edge(i,a-1));
			}
		}
		
		printf("Case #%d: ",X);
		
		for(int i = 0; i <= n; i++){
			memset(used,0,sizeof(used));
			if(i==n){
				cout<<"No"<<endl;
				break;
			}
			if(dfs(i,g)){
				cout<<"Yes"<<endl;
				break;
			}
			/*for(int j = 0,l = g[i].size(); j < l; j++){
				if(dfs(g[i][j].dst,g)){
					cout<<"YES"<<endl;
					i = n+1;
					break;
				}
			}
			*/
		}
	}
	return 0;
}
