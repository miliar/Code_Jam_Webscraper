#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

int P[111][33];
vector<int> adj[111];
int lnk[111];
int flag[111],flags;
bool find(int p){
	for(int i=0,q;i<adj[p].size();i++)if(flag[q=adj[p][i]]!=flags){
		flag[q]=flags;
		if(lnk[q]==-1||find(lnk[q])){
			lnk[q]=p;
			return true;
		}
	}
	return false;
}
int main(){
	int T,cas=0,n,K;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&K);
		for(int i=0;i<n;i++)
			for(int j=0;j<K;j++)
				scanf("%d",&P[i][j]);
		for(int i=0;i<n;i++)
			adj[i].clear();
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)if(P[i][0]>P[j][0]){
				bool found=false;
				for(int k=0;k<K;k++)if(P[i][k]<=P[j][k])
					found=true;
				if(!found)
					adj[i].push_back(j);
			}
		memset(lnk,-1,sizeof(lnk));
		int ret=n;
		for(int i=0;i<n;i++)if(flags++,find(i))
			ret--;
		printf("Case #%d: %d\n",++cas,ret);
	}
}
