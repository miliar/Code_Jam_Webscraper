#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;
int n;
int level[2001];
int par[2001];
int height[2001];
int tree[2002][2002];
int subt[2002];

int dfs(int c,int l,int minchild){
	level[c]=l;
	if(c<minchild)return 1;
	int cminchild=minchild;
	subt[c]=1;
	for(int j=1;j<=tree[c][0];j++){
		if(dfs(tree[c][j],l+1,cminchild))return 1;
		cminchild=tree[c][j];
		subt[c]+=subt[tree[c][j]];
	}
	return 0;
}

void rec(int c){
	if(tree[c][0]==0)return;
	height[tree[c][1]]=height[c];
	if(c!=n-1){
		while((height[par[c]]-height[c])*(c-tree[c][1])>=(height[c]-height[tree[c][1]])*(par[c]-c))height[tree[c][1]]--;
	}
	for(int j=2;j<=tree[c][0];j++){
		height[tree[c][j]]=(height[c]-height[tree[c][1]])*(tree[c][j]-tree[c][1])/(c-tree[c][1])+height[tree[c][1]]-5;
		if(c!=n-1){
			while((height[par[c]]-height[c])*(c-tree[c][j])>=(height[c]-height[tree[c][j]])*(par[c]-c))height[tree[c][j]]--;
		}
	}
	for(int j=1;j<=tree[c][0];j++)rec(tree[c][j]);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d",&cases);
	
	for(int casenum=1;casenum<=cases;casenum++){
		printf("Case #%d: ",casenum);
		scanf("%d",&n);
		memset(tree,0,sizeof(tree));
		memset(level,0,sizeof(level));
		int t;
		for(int i=0;i<n-1;i++){
			scanf("%d",&t);
			par[i]=t-1;
			tree[t-1][++tree[t-1][0]]=i;
		}
		if(dfs(n-1,0,0)){
			puts("Impossible");
			continue;
		}
		height[n-1]=10000*n;
		rec(n-1);
		for(int i=0;i<n-1;i++)printf("%d ",height[i]);
		printf("%d\n",height[n-1]);
	}
	return 0;
}