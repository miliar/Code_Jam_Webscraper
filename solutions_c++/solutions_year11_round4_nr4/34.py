#include <stdio.h>
#include <string.h>
#define maxn 450
#define maxm 2010
int st[maxn],aim[maxm<<1],link[maxm<<1],ln;
int a[maxn][maxn];
int n,m;
int dis[maxn];
int dis2[maxn];
int q[maxn];
int tag[maxn];
int g[maxn][maxn][maxn];
char s[1000];
void in_edge(int x,int y){
	aim[ln]=y;
	link[ln]=st[x];
	st[x]=ln++;
}
void dij(int *dis,int sp){
	int i,j,k,qn=1;
	q[0]=sp;
	dis[sp]=0;
	for (int p=0;p<qn;p++)
		for (i=0;i<n;i++)
			if (a[q[p]][i] && dis[i]==-1){
				dis[i]=dis[q[p]]+1;
				q[qn++]=i;
			}
}
int max(int x,int y){return x>y?x:y;}
int f(int x,int y,int z){
	if (g[x][y][z]==-1){
		int &gt=g[x][y][z];
		if (x==1){
			gt=1;
			return 1;
		}
		int tot=0;
		for (int i=st[x];i!=-1;i=link[i])
			if (aim[i]!=y && !a[y][aim[i]] && !a[z][aim[i]]) tot++;
		// for (int i=0;i<n;i++)
			// if (i!=y && a[x][i] && !a[y][i] && !a[z][i]){
				// tot++;
			// }
		for (int i=st[x];i!=-1;i=link[i])
			if (dis[aim[i]]==dis[x]+1 && dis2[aim[i]]+dis[aim[i]]==dis[1])
				gt=max(gt,f(aim[i],x,y)+tot-1);
		// for (int i=0;i<n;i++)
			// if (a[x][i] && dis[i]==dis[x]+1 && dis2[i]+dis[i]==dis[1]){
				// gt=max(gt,f(i,x,y)+tot-1);
			// }
	}
	return g[x][y][z];
}
int main(){
	int i,j,k;
	int cp,tn;
	for (scanf("%d",&tn),cp=1;cp<=tn;cp++){
		scanf("%d %d",&n,&m);
		memset(a,0,sizeof(a));
		memset(st,-1,sizeof(st));
		ln=0;
		for (i=0;i<m;i++){
			int u,v;
			scanf("%s",s);
			k=0;
			for (j=0;j<strlen(s) && s[j]!=',';j++) k=k*10+s[j]-'0';
			u=k;
			k=0;
			for (j++;j<strlen(s) && s[j]!=',';j++) k=k*10+s[j]-'0';
			v=k;
			a[u][v]=a[v][u]=1;
			in_edge(u,v);
			in_edge(v,u);
		}
		memset(dis,-1,sizeof(dis));
		memset(dis2,-1,sizeof(dis2));
		dij(dis,0);
		dij(dis2,1);
		memset(g,-1,sizeof(g));
		printf("Case #%d: %d %d\n",cp,dis[1]-1,f(0,n,n));
	}
	return 0;
}