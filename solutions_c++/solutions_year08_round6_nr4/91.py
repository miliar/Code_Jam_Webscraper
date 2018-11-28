#include <cstdio>
#include <cstring>

int i,j,k,s,t,n,m;
int a[200][200];
struct node{
	int s,t;
}b[20];
bool f;
bool vi[20];
int tmp[20];
bool check()
{
	int i;
	for (i=1;i<m;++i)
	    if (a[tmp[b[i].s]][tmp[b[i].t]]==0) return false;
	return true;
}
void dfs(int nu)
{
	int i;
	if (f) return;
	for (i=1;i<=n;++i)
		if (!vi[i])
		{
			tmp[nu]=i;
			vi[i]=1;
			if (nu==m)
			    f|=check();
			else dfs(nu+1);
			if (f) return;
			vi[i]=0;
		}
}
int T,I;
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		printf("Case #%d: ",I);
		f=false;
		scanf("%d",&n);
		memset(a,0,sizeof a);
		for (i=1;i<n;++i){
			scanf("%d%d",&s,&t);
			a[s][t]=a[t][s]=1;
		}
		memset(vi,0,sizeof vi);
		scanf("%d",&m);
		for (j=1;j<m;++j)
		    scanf("%d%d",&b[j].s,&b[j].t);
		dfs(1);
		if (f) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
