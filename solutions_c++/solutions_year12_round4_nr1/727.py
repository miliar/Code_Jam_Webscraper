#include<cstdio>
#include<cstring>
#include<queue>
#include<map>
using namespace std;

int d[10005], l[10005];
int n;

int vis[10005];
bool bfs(){
	memset(vis, -1, sizeof(vis));
	queue<pair<int, int> > que;
	que.push(make_pair(0,d[0]));
	vis[0] = d[0];
	while(!que.empty()){
		int u = que.front().first;
		int ud = que.front().second;
		que.pop();
		for(int i=u+1;i<=n;i++){
			if(d[i]>d[u]+ud) continue;
			if(i==n) return true;
			int td = min(d[i]-d[u], l[i]);
			if(vis[i]>=td) continue;
			que.push(make_pair(i,td));
			vis[i] = td;
		}
	}
	return false;
}


int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t, cas=0;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		
		for(int i=0;i<n;i++){
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &d[n]);

		printf("Case #%d: ", ++cas);
		if(bfs()) puts("YES");
		else puts("NO");
	}
	
}