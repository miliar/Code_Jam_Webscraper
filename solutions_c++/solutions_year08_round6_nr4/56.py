#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<set>
#include<map>
#include<deque>
#include<functional>
using namespace std;

const int maxn=128;
int a[maxn][maxn];
int b[maxn][maxn];
int flag[maxn];
int c[maxn];
int n,m;

void input()
{
	int i,t1,t2;
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
	scanf("%d",&n);
	for(i=1;i<n;i++){
		scanf("%d%d",&t1,&t2);
		a[t1][t2]=a[t2][t1]=1;
	}
	scanf("%d",&m);
	for(i=1;i<m;i++){
		scanf("%d%d",&t1,&t2);
		b[t1][t2]=b[t2][t1]=1;
	}
}

bool dfs(int x)
{
	int i,j;
	if(x>m){
		for(i=1;i<=m;i++){
			for(j=i+1;j<=m;j++){
				if(b[i][j]==1 && a[c[i]][c[j]]==0) return false;
				if(b[i][j]==0 && a[c[i]][c[j]]==1) return false;
			}
		}
		return true;
	}
	for(i=1;i<=n;i++) if(flag[i]==0){
		flag[i]=1;
		c[x]=i;
		if(dfs(x+1)) return true;
		flag[i]=0;
	}
	return false;
}

bool solve()
{
	memset(flag,0,sizeof(flag));
	if(dfs(1)) return true;
	return false;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("d.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		input();
		if(solve()) printf("Case #%d: YES\n",i);
		else printf("Case #%d: NO\n",i);
	}
	return 0;
}
