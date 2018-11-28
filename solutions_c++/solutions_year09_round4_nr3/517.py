#include<Cstdio>
#include<queue>
#include<vector>
#include<stack>
#include<algorithm>
#include<cmath>
#include<Cstring>
#include<string>
#include<memory>

using namespace std;

int n,m;
int a[200][200];
__int64 g[200];
int e[200];
__int64 chk;
pair<int,int> b[200];
int res;
int used;

void process(__int64 st,int i,int size)
{
	int j;
	__int64 temp;
	if(size>=res) return;
	if(used==n)
	{
		res=size;
		return;
	}
	for(;i<n;i++)
	{
		temp=chk&((__int64)1<<i);
		if(temp) continue;
		if((g[i]&st)!=st) continue;
		used++;
		process(st|(__int64)1<<i,i+1,size);
		used--;
		if(st==0) return;
	}
	chk=chk|st;
	process(0,0,size+1);
	chk=chk^st;
}

void input()
{
	memset(g,0,sizeof(g));
	chk=0;
	res=99999999;
	used=0;
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for(int i=0;i<n;i++)
	{
		e[i]=0;
		for(int j=0;j<n;j++)
		{
			int k;
			if(a[i][0]>=a[j][0]) continue;
			for(k=0;k<m;k++)
			{
				if(a[i][k]>=a[j][k]) break;
			}
			if(k<m) continue;
			g[i]=g[i]|(__int64)1<<j;
			g[j]=g[j]|(__int64)1<<i;
			e[i]++;
		}
		g[i]=g[i]|(__int64)1<<i;
		e[i]++;
	}
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		input();
		vector<int> v;
		process(0,0,1);
		printf("Case #%d: %d\n",i+1,res);
	}
}