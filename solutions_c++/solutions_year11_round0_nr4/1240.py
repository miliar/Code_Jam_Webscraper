#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
 
using namespace std;
 
bool vis[10001];
vector<int> V;
vector<int> Vi;
map<int,int> pos;
vector<int>  G[10001];
int nc=0;

void dfs(int u){
        //printf("%d\n",u);
        vis[u]=true;
		nc++;
        for(int i=0;i<G[u].size();i++) 
			if(!vis[G[u][i]]){
				dfs(G[u][i]);
			}
}
        
int main()
{
  // Type in your solution here
    int T, N, v, nt, ans;
    
	scanf("%d",&T);
	nt=1;
	while(T--){
		scanf("%d",&N);
        
		int nc=0;
        for(int i=0;i<N;i++){
                scanf("%d",&v);
                V.push_back(v);
				if(v!=i+1) nc++;
        }
		
        printf("Case #%d: %.6lf\n",nt,(nc)*1.0f);
		nt++;
	}
    return 0;
}
