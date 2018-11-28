#include<cstdio>
#include<vector>
using namespace std;
struct node
{
	int a,b;
};
vector<node>co[2005];
bool ok;
int n,m;
int sum,r;
bool mark[100005];
bool rr[100005];
void dfs(int dep)
{
	int i,a,b,j;
	if(sum>=r)return;
	if(dep==n)
	{
		for(i=0;i<m;i++)
		{
			for(j=0;j<co[i].size();j++)
			{
				a=co[i][j].a;
				b=co[i][j].b;
				if(mark[a]==b)break;
			}
			if(j==co[i].size())break;
		}
		if(i==m)
		{
			ok=1;
			if(r>sum)
			{
				r=sum;
				for(i=0;i<n;i++)rr[i]=mark[i];
			}
		}
		return;
	}
	mark[dep]=0;
	dfs(dep+1);
	sum++;
	mark[dep]=1;
	dfs(dep+1);
	sum--;
	mark[dep]=0;
}	
int main()
{
	int t,cc,i,a,b,c,j;
	node p;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("bsm.out","w",stdout);
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)co[i].clear();
		for(i=0;i<m;i++)
		{
			scanf("%d",&a);
			for(j=0;j<a;j++)
			{
				scanf("%d%d",&p.a,&p.b);
				p.a--;
				co[i].push_back(p);
			}
		}
		ok=0;sum=0;r=100000;
				dfs(0);
		if(ok==0)
		printf("Case #%d: IMPOSSIBLE\n",cc);
		else
		{
			printf("Case #%d:",cc);
			for(i=0;i<n;i++)printf(" %d",rr[i]);
			printf("\n");
		}
	}
	return 0;
}
		
				
				
	
