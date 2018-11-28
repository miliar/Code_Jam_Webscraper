#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

const int N=201;

typedef struct train
{
	int dep,arr;
} train;
train a[N],b[N];
char ch[11];
int n,m,T,f[N],p[N];
vector<int> c[N],d[N];
bool use[N];

int code(char str[11])
{
   int i;
   i=(str[0]-'0')*10+str[1]-'0';
   i=i*60+(str[3]-'0')*10+str[4]-'0';
   return i;
}

int dfs(int k)
{
	vector<int>::iterator it;
	int i,j;
	use[k]=1;
	for (it=c[k].begin();it!=c[k].end();it++)
	{
		i=*it;
		if (p[i]<0)
		{
			p[i]=k;
			return 1;
		}
		else
		if (use[p[i]]==0)
		{
			j=p[i];
			p[i]=k;
			if (dfs(j)) return 1;
			p[i]=j;
		}
	}
	return 0;
}

int main()
{
	int i,j,test,t=1;
	freopen("blarge.txt","r",stdin);
	freopen("blarge.out","w",stdout);
	scanf("%d",&test);
	while (t<=test)
	{
		scanf("%d",&T);
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
		{
			scanf("%s",ch);
			a[i].dep=code(ch);
			scanf("%s",ch);
			a[i].arr=code(ch);
		}
		for (i=0;i<m;i++)
		{
			scanf("%s",ch);
			b[i].dep=code(ch);
			scanf("%s",ch);
			b[i].arr=code(ch);
		}
		for (i=0;i<N;i++) c[i].clear();
		for (i=0;i<n;i++)
		 for (j=0;j<m;j++)
		 if (a[i].arr+T<=b[j].dep) c[i].push_back(j+n);
		for (i=0;i<m;i++)
		 for (j=0;j<n;j++)
		 if (b[i].arr+T<=a[j].dep) c[i+n].push_back(j);

		memset(p,0xff,sizeof(p));
		for (i=0;i<n+m;i++)
		{
			memset(use,0,sizeof(use));
			dfs(i);
		}
		int ans1=0,ans2=0;
		for (i=0;i<n;i++)
		if (p[i]<0) ans1++;
		for (i=n;i<n+m;i++)
		if (p[i]<0) ans2++;
		printf("Case #%d: %d %d\n",t++,ans1,ans2);
	}
	return 0;
}