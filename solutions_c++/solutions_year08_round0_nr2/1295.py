#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
const int MAXN=210;
int T,n0,n1,n;
int t[MAXN][2];
int link[MAXN];
void sTime(int& tm)
{
	int t;
	scanf("%d:%d",&t,&tm);
	tm+=t*60;
}
void init()
{
	scanf("%d",&T);
	scanf("%d%d",&n0,&n1);
	n=n0+n1;
	for(int i=1;i<=n;i++)
	{
		sTime(t[i][0]);
		sTime(t[i][1]);
	}
}
bool y[MAXN];
bool find(int u)
{
	int st,ed;
	if(u<=n0)
	{
		st=n0+1;
		ed=n;
	}
	else
	{
		st=1;
		ed=n0;
	}
	for(int i=st;i<=ed;i++)
	{
		if(t[i][0]>=t[u][1]+T&&!y[i])
		{
			y[i]=true;
			if(!link[i]||find(link[i]))
			{
				link[i]=u;
				return true;
			}
		}
	}
	return false;
}
int l[MAXN];
void work()
{
	memset(link+1,0,sizeof(int)*n);
	memset(l+1,0,sizeof(int)*n);
	for(int i=1;i<=n;i++)
	{
		memset(y+1,0,sizeof(bool)*n);
		find(i);
	}
	for(int i=1;i<=n;i++)if(link[i])l[link[i]]=i;
	int a=0,b=0;
	for(int i=1;i<=n;i++)
	{
		if(!link[i])
		{
			if(i<=n0)a++;
			else b++;
		}
	}
	printf("%d %d\n",a,b);
}
int main()
{
	int cases;
	scanf("%d",&cases);
	int t=0;
	while(cases--)
	{
		++t;
		printf("Case #%d: ",t);
		init();
		work();
	}
}
