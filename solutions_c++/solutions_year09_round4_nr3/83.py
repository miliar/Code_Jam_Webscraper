#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
const int N=120;
pair<int ,int> c[N];
int T,n,m,a[N][N],g[N][N],d[N],b[N],q[N][N],C[N],ans,now;
void dfs(int i){
	if (i==n){
		ans=now;
		return;
	}
	for (int j=0;j<now;j++){
		int flag=1;
		for (int k=0;k<b[j];k++)
			if (!g[C[i]][q[j][k]]){
				flag=0;break;
			}
		if (flag){
			q[j][b[j]++]=C[i];
			dfs(i+1);
			b[j]--;
		}
	}
	if (now<ans){
		b[now]=1;
		q[now][0]=C[i];
		now++;
		dfs(i+1);
		now--;
	}
	return;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++){
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		for (int i=0;i<n;i++)
			d[i]=0;
		for (int i=0;i<n;i++)
			for (int j=i+1;j<n;j++){
				int flag=1;
				for (int k=1;k<m;k++)
					if (!(a[i][k-1]<a[j][k-1] && a[i][k]<a[j][k] || a[i][k-1]>a[j][k-1] && a[i][k]>a[j][k]))
						flag=0;
				g[i][j]=flag;d[i]+=flag;
				g[j][i]=flag;d[j]+=flag;
			}
		for (int i=0;i<n;i++)
			c[i]=make_pair(d[i],i);
		sort(c,c+n);
		for (int i=0;i<n;i++)
			C[i]=c[i].second;
		ans=n;
		now=0;
		dfs(0);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
