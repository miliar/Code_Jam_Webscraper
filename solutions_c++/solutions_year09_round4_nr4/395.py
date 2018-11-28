#include<iostream>
#include<cmath>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<cstdlib>
#include<stack>
#include<list>
#include<deque>
#include<queue>
using namespace std;

typedef long long LL;

#define EPS (1e-8)
#define INF 0x7fffffff
#define SZ(p) ((p).size())

struct node
{
	int x,y,r;
}p[3];

double dis(node p,node q)
{
	return sqrt(double(p.x-q.x)*(p.x-q.x)+double(p.y-q.y)*(p.y-q.y));
}

double get(int i,int j)
{
	return 0.5*(dis(p[i],p[j])+p[i].r+p[j].r);
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	//freopen("2.in","r",stdin);
	//freopen("2.out","w",stdout);

	int T,CS;
	scanf("%d",&T);
	for(CS=1;CS<=T;CS++)
	{
		int n,i,j;
		double ans=0.0,t=INF;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&p[i].x,&p[i].y,&p[i].r);
			if(ans<p[i].r)
				ans=p[i].r;
		}
		if(n==3)
		{
			for(i=0;i<n;i++)
				for(j=i+1;j<n;j++)
				{
					t=min(t,get(i,j));
				}
			if(t!=INF&&ans<t)
				ans=t;
		}
		printf("Case #%d: ",CS);
		fflush(stdout);

		printf("%lf\n",ans);
	}
}