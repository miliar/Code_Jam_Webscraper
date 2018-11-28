#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define maxn 410

using namespace std;

struct node {
	int x;
	node *next;
};


int g[maxn][maxn];
int f[maxn][maxn];
int dist[maxn];
node *gg[maxn];
bool used[maxn];
int tt;
int level[maxn][maxn];

void makeedge(int st,int ed) {
	node *p=new node;
	p->x=ed; p->next=gg[st]; gg[st]=p;
}

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		int n,m;
		scanf("%d%d",&n,&m);
		memset(g,0,sizeof(g));
		memset(gg,0,sizeof(gg));
		for (int i=1;i<=m;++i) {
			int x,y;
			scanf("%d,%d",&x,&y);
			g[x][y]=g[y][x]=1;
			makeedge(x,y); makeedge(y,x);
		}
		memset(dist,127,sizeof(dist));
		dist[0]=0;
		memset(used,false,sizeof(used));
		for (int i=1;i<=n;++i) {
			int pp=-1;
			for (int j=0;j<n;++j)
				if (!used[j] && (pp==-1 || dist[j]<dist[pp]))
					pp=j;
			if (pp==-1) break;
			used[pp]=true;
			for (int j=0;j<n;++j)
				if (g[pp][j]>0 && dist[pp]+1<dist[j])
					dist[j]=dist[pp]+1;
		}

		memset(level,0,sizeof(level));
		for (int i=0;i<n;++i) if (dist[i]<n) {
			level[dist[i]][0]++;
			level[dist[i]][level[dist[i]][0]]=i;
		}
		memset(f,0,sizeof(f));
		for (int i=1;i<=level[0][0];++i)
			for (int j=1;j<=level[1][0];++j) {
				int cnt=0;
				for (int k=0;k<n;++k)
					if (g[level[0][i]][k]>0 || g[level[1][j]][k]>0) cnt++;
				f[level[0][i]][level[1][j]]=cnt;
			}
		for (int i=0;i<=dist[1]-3;++i)
			for (int j=1;j<=level[i][0];++j)
				for (int k=1;k<=level[i+1][0];++k) {
					memset(used,false,sizeof(used));
					node *p=gg[level[i][j]];
					while (p!=0) {
						used[p->x]=true;
						p=p->next;
					}
					used[level[i][j]]=true;
					p=gg[level[i+1][k]];
					while (p!=0) {
						used[p->x]=true;
						p=p->next;
					}
					used[level[i+1][k]]=true;
					for (int l=1;l<=level[i+2][0];++l)
					if (g[level[i+1][k]][level[i+2][l]]>0){
						int cnt=0;
						p=gg[level[i+2][l]];
						while (p!=0) {
							if (!used[p->x]) cnt++;
							p=p->next;
						}
						if (!used[level[i+2][l]]) cnt++;
						f[level[i+1][k]][level[i+2][l]]=max(f[level[i+1][k]][level[i+2][l]],
								f[level[i][j]][level[i+1][k]]+cnt);
					}
				}
		int ans=0;
		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j)
				if (g[j][1]>0 && dist[j]+1==dist[1])
					ans=max(ans,f[i][j]);
		if (dist[1]==1) {
			node *p=gg[0];
			while (p!=0) {
				ans++;
				p=p->next;
			}
			ans++;
		}
		printf("Case #%d: %d %d\n",ii,dist[1]-1,ans-dist[1]);
	}

}
