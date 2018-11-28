#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
const int maxn=1005;
struct Tnode
{
	int x,y,z;
}	o[maxn*10];
int x,s,r,n,m,test,a[maxn],b[maxn],c[maxn];
double ans,RT,t;

bool Cmp(Tnode a,Tnode b)
{
	return a.z<b.z;
}

void Add(int x,int y,int z)
{
	o[++m].x=x;o[m].y=y;o[m].z=z;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		for (int i=1;i<=n;i++)
			scanf("%d%d%d",&a[i],&b[i],&c[i]);
		m=0;
		if (a[1]) Add(0,a[1],0);
		for (int i=1;i<=n;i++)
		{
			Add(a[i],b[i],c[i]);
			if (i<n&&b[i]<a[i+1]) Add(b[i],a[i+1],0);
		}
		if (b[n]!=x) Add(b[n],x,0);
		sort(o+1,o+m+1,Cmp);
		ans=0;
		for (int i=1;i<=m;i++)
		if (fabs(t)<=1e-9) ans+=(double)(o[i].y-o[i].x)/(o[i].z+s); else
		{
			RT=(double)(o[i].y-o[i].x)/(o[i].z+r);
			if (RT<=t)
			{
				ans+=RT;
				t=t-RT;
			}	else
			{
				ans+=t;
				ans+=(double)(o[i].y-o[i].x-(double)(o[i].z+r)*t)/(o[i].z+s);
				t=0;
			}
		}
		printf("Case #%d: %.6lf\n",kase,ans);
	}
	
	return 0;
}
