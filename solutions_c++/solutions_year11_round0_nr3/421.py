#include <cstdio>
#include <cstring>

int t,n;
int data[1010],min,sum,ans,ok;

void init()
{
		scanf("%d",&n);
		ans=sum=0;min=1000000;
		for (int i=0;i<n;i++)
		{
			scanf("%d",&data[i]);
			sum+=data[i];
			ans^=data[i];
			if (min>data[i])min=data[i];
		}
		if (ans==0)ok=-1;else ok=0;
}

void dfs(int top,int num,int p,int q)
{
	if (ok>=1)return;
	if (p!=0 && num==(ans^num)) ok++;
	if (top>=n)return ;
	dfs(top+1,num^data[top],p+q,q*2);
	dfs(top+1,num,p,q*2);
}

bool solve_small()
{
	dfs(0,0,0,1);
	if (ok<1)return true;
	else return false;
}

int main()
{
	freopen("C-large.in","r",stdin);freopen("c.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		init();

		if (ans!=0) printf("Case #%d: NO\n",id);
		else printf("Case #%d: %d\n",id,sum-min);
	}
	return 0;
}
