#include<cstdio>
#include<cstring>
using namespace std;
double w[1000000];
char f[1000000][20],i[1000][20],str[10000];
int c,m,t0[1000000],t1[1000000];
void dfs(int p)
{
//printf("( %d\n",p);
	scanf(" (%lf",&w[p]);
	scanf(" %c",&f[p][0]);
	if( f[p][0]==')' ){ f[p][0]=0; return; }
	ungetc(f[p][0],stdin);
	scanf("%s",f[p]);
	t0[p]=c;
	c++;
	dfs(t0[p]);
	t1[p]=c;
	c++;
	dfs(t1[p]);
	scanf(" )");
//printf("%d )\n",p);
}
double dfs2(int p)
{
	int s,t;
	if( f[p][0]==0 ) return w[p];
	t=0;
	for(s=0;s<m;s++) if( strcmp(i[s],f[p])==0 ) t=1;
	if( t==1 ) return w[p]*dfs2(t0[p]);
	return w[p]*dfs2(t1[p]);
}
int main()
{
	int a,s,n,t;
int T,X;
scanf("%d",&T);
for(X=1;X<=T;X++)
{
	printf("Case #%d:\n",X);
	scanf("%d",&t);
	c=1;
	dfs(0);
	scanf("%d",&n);
//printf("%d\n",n);
	for(a=0;a<n;a++)
	{
		scanf("%*s%d",&m);
		for(s=0;s<m;s++)
		{
			scanf("%s",i[s]);
		}
		printf("%.7lf\n",dfs2(0));
	}
}
	return 0;
}
