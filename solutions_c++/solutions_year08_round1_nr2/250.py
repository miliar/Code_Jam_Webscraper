#include "stdio.h"
#include <vector>
using namespace std;
int boo[2005],res[2005],z[2005],ok,n,m,sx[2005],sy[2005];
vector <int> x[2005],y[2005];
void search(int step,int s,int sum)
{
	int i,k;
	vector <int> a;
	if(s>=ok)
		return;
	if(step==n+1)
	{
		if(sum==m&&(s<ok))
		{
			for(i=1;i<=n;i++)
				res[i]=z[i];
			ok=s;
		}
		return;
	}
	k=0;
	z[step]=1;
	for(i=0;i<sx[step];i++)
	{
		if(boo[x[step][i]]==0)
		{
			boo[x[step][i]]=1;
			a.push_back(x[step][i]);
			k++;
		}
	}
	search(step+1,s+1,sum+k);
	for(i=0;i<k;i++)
		boo[a[i]]=0;
	a.clear();
	z[step]=0;
	k=0;
	for(i=0;i<sy[step];i++)
	{
		if(boo[y[step][i]]==0)
		{
			boo[y[step][i]]=1;
			a.push_back(y[step][i]);
			k++;
		}
	}
	search(step+1,s,sum+k);
	for(i=0;i<k;i++)
		boo[a[i]]=0;
}
int main()
{
	int kase,tot,i,k,j,t;
	scanf("%d",&kase);
	for(tot=1;tot<=kase;tot++)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
		{
			x[i].clear();
			y[i].clear();
		}
		for(i=1;i<=m;i++)
		{
			scanf("%d",&t);
			while(t--)
			{
				scanf("%d%d",&k,&j);
				if(j==1)
					x[k].push_back(i);
				else
					y[k].push_back(i);
			}
			boo[i]=0;
		}
		for(i=1;i<=n;i++)
		{
			sx[i]=x[i].size();
			sy[i]=y[i].size();
		}
		ok=0x7fffffff;
		search(1,0,0);
		printf("Case #%d:",tot);
		if(ok==0x7fffffff)
			printf(" IMPOSSIBLE\n");
		else
		{
			for(i=1;i<=n;i++)
				printf(" %d",res[i]);
			printf("\n");
		}
	}
	return 0;
}