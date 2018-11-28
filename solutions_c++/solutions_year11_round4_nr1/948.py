#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#define MAXN 1005
typedef long long ll;
const double eps=1e-10;
int n,x,s,r;
double t;
struct Node
{
	int a,b;
}node[MAXN];
int cmp(Node x,Node y)
{
	//return 1ll*x.a*y.b*(y.b+r-s)>1ll*y.a*x.b*(x.b+r-s);
	return x.b<y.b;
}
using namespace std;
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int _,cas=0;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		int y=x;
		for(int i=0;i<n;i++)
		{
			int a,b,w;
			scanf("%d%d%d",&a,&b,&w);
			node[i].a=b-a;
			node[i].b=s+w;
			y-=(b-a);
		}
		node[n].a=y;
		node[n].b=s;
		sort(node,node+n+1,cmp);
		//for(int i=0;i<=n;i++) printf("%d %d\n",node[i].a,node[i].b);
		double ans=0;
		for(int i=0;i<=n;i++)
		{
			if(t<eps)
			{
				ans+=1.*node[i].a/node[i].b;
				continue;
			}
			double tmp=1.*node[i].a/(node[i].b+r-s);
			//printf("%.6f\n",tmp);
			if(tmp+eps>t)
			{
				ans+=t;
				ans+=(1.*node[i].a-t*(node[i].b+r-s))/node[i].b;
				t=0.;
			}
			else
			{
				ans+=tmp;
				t-=tmp;
			}
		}
		printf("Case #%d: %.10f\n",++cas,ans);
	}
}
