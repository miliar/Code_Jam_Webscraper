#include<stdio.h>
#include<algorithm>
using namespace std;
struct walk{int a,b,c;} w[1005];
bool cmp(walk a,walk b)
{
	return a.c<b.c;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);

	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		int x,s,r,T,n;
		int l;
		double time = 0.0;
		scanf("%d %d %d %d %d",&x,&s,&r,&T,&n);
		l=x;
		if(r<s) r=s;
		for(int i=0;i<n;i++)
		{
			scanf("%d %d %d",&w[i].a,&w[i].b,&w[i].c);
			l-=(w[i].b-w[i].a);
		}
		sort(w,w+n,cmp);
		double rt = double(T);
		double nt;
		
		nt = l/double(r);
		if(rt<nt)
		{
			time+=rt+(l-(r*rt))/double(s);
			rt=0.0;
		}
		else
		{
			rt-=nt;
			time+=nt;
		}
		for(int i=0;i<n;i++)
		{
			nt = (w[i].b-w[i].a)/double(r+w[i].c);
			if(rt<nt)
			{
				time+=rt+(w[i].b-w[i].a-((r+w[i].c)*rt))/double(s+w[i].c);
				rt=0.0;
			}
			else
			{
				rt-=nt;
				time+=nt;
			}
		}
		printf("Case #%d: %.8lf\n",t,time);
	}

	return 0;
}
