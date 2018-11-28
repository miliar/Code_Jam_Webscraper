#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#define maxn (9)
using namespace std;

int ans,test,Case,N,M,color[maxn],hash[maxn],u[maxn],v[maxn];
bool a[maxn][maxn];

bool check(vector<int>&list){
	int len=list.size();
	bool find=false;
	for (int i=0;i<len;i++)
		for (int j=i+2;j<len;j++) if (((i==0 && j!=len-1)|| i>0)&& a[list[i]][list[j]]){
			find=true;
			vector<int>tmp1,tmp2;
			tmp1.clear();
			tmp2.clear();
			for (int k=i;k<=j;k++) tmp1.push_back(list[k]);
			for (int k=j;k<len;k++) tmp2.push_back(list[k]);
			for (int k=0;k<=i;k++) tmp2.push_back(list[k]);
			return check(tmp1) && check(tmp2);
		}
	if (!find){
		bool vis[maxn];
		for (int i=1;i<=ans;i++) vis[i]=false;
		for (int i=0;i<len;i++) vis[color[list[i]]]=true;
		for (int i=1;i<=ans;i++) if (!vis[i]) return false;
		return true;
	}
}
bool dfs(int c,int dep,int rem){
	if (dep>N){
		if (rem>0) return false;
		vector<int>list;
		list.clear();
		for (int i=1;i<=N;i++) list.push_back(i);
		return check(list);
	}
	for (int i=1;i<=c;i++){
		color[dep]=i;
		if (!hash[i]) rem--;
		hash[i]++;
		if (dfs(c,dep+1,rem)) return true;
		hash[i]--;
		if (!hash[i]) rem++;
	}
	return false;
}
int main(){
	freopen("i.txt","r",stdin);
	for (scanf("%d",&test);test--;){
		printf("Case #%d: ",++Case);
		memset(a,0,sizeof(a));
		scanf("%d%d",&N,&M);
		for (int i=1;i<=M;i++) scanf("%d",&u[i]);
		for (int i=1;i<=M;i++) scanf("%d",&v[i]);
		for (int i=1;i<=M;i++) a[u[i]][v[i]]=a[v[i]][u[i]]=true;
		ans=min(N,5);
		for (;ans>=1;ans--){
			memset(hash,0,sizeof(hash));
			if (dfs(ans,1,ans)) break;
		}
		printf("%d\n",ans);
		for (int i=1;i<=N;i++){
			printf("%d",color[i]);
			if (i<N) printf(" ");
				else puts("");
		}
	}
	return 0;
}
