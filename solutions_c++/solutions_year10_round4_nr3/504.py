#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=1100;
struct rect
{
	int x1,y1,x2,y2;
};
int n;
rect r[maxn];
int f[maxn],a[maxn],b[maxn],c[maxn];
bool touch(rect a,rect b)
{
	if(a.x2+1<b.x1||a.x1>b.x2+1||a.y2+1<b.y1||a.y1>b.y2+1) return false;
	return true;
}
void init()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		int x1,y1,x2,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		r[i].x1=min(x1,x2);
		r[i].x2=max(x1,x2);
		r[i].y1=min(y1,y2);
		r[i].y2=max(y1,y2);
	}
}
int find(int v)
{
	if(f[v]==v) return v;
	return f[v]=find(f[v]);
}
int solve()
{
	for(int i=0;i<n;i++)
	{
		f[i]=i;
		a[i]=r[i].x1+r[i].y1;
		//b[i]=r[i].x2+r[i].y2;
		b[i]=r[i].x2;
		c[i]=r[i].y2;
	}
	for(int i=0;i<n;i++)
		for(int j=0;j<i;j++)
		{
			if(!touch(r[i],r[j])) continue;
			int u=find(i),v=find(j);
			if(i==j) continue;
			f[u]=v;
			a[v]=min(a[v],a[u]);
			b[v]=max(b[v],b[u]);
			c[v]=max(c[v],c[u]);
		}
	int ans=0;
	for(int i=0;i<n;i++)
	{
		int v=find(i);
		//printf("%d: %d %d,%d,%d\n",i,v,a[v],b[v],c[v]);
		ans=max(ans,b[v]+c[v]-a[v]);
	}
	return ans+1;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		init();
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
