#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;
#define M 1210

int n;
int c[M],ss;
int maxx;

int ab(int x)
{
	if(x<0)
		return -x;
	return x;
}

void dfs(int id,int va,int vb,int v)
{
	if(id==n)
	{
		if(va==vb)
		{
			if(v==ss||v==0)
				return;
			if(v>maxx)
				maxx=v;
		}
		return;
	}
	dfs(id+1,va^c[id],vb,v);
	dfs(id+1,va,vb^c[id],v+c[id]);
}

int main()
{
	int i,j,k,t,tc=1;
	freopen("out.txt","w",stdout);
	freopen("gcj/C-large.in","r",stdin);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(ss=0,k=0,i=0;i<n;i++)
		{
			scanf("%d",c+i);
			ss+=c[i];
			k^=c[i];
		}
		//maxx=-1;
		sort(c,c+n);
		printf("Case #%d: ",tc++);
		if(i<2||k)
			printf("NO");
		else
			printf("%d",ss-c[0]);
		putchar(10);
	}
	return 0;
}


