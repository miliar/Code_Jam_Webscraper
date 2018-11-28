#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct interv{
	interv(int _l = 0,int _r = 0,int _w = 0) : l(_l), r(_r), w(_w) {};
	int l,r,w;
};

bool sortX(const interv & a,const interv & b)
{
	return a.l<b.l||a.l==b.l&&a.r<b.r||a.l==b.l&&a.r==b.r&&a.w<b.w;
}

bool sortS(const interv & a,const interv & b)
{
	return a.w>b.w||a.w==b.w&&a.r<b.r||a.w==b.w&&a.r==b.r&&a.l<b.l;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		int x,s,r,n,a,b,c;
		double t;
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		vector <interv> v;
		for(int i=0;i<n;i++)
		{
			scanf("%d%d%d",&a,&b,&c);
			v.push_back(interv(a,b,c));
		}
		sort(v.begin(),v.end(),sortX);
		int lx=0,k=v.size();
		for(int i=0;i<k;i++)
		{
			if (lx<v[i].l) v.push_back(interv(lx,v[i].l,0));
			lx=v[i].r;
		}
		if (lx<x) v.push_back(interv(lx,x,0));
		sort(v.rbegin(),v.rend(),sortS);
//		for(int i=0;i<v.size();i++)
//			cout << v[i].l << "	" << v[i].r << "	" << v[i].w << endl;
		double tm=0;
		for(int i=0;i<v.size();i++)
		{
			if (t>0)
			{
				double cur=min(0.0+v[i].r-v[i].l,1.0*t*(v[i].w+r));
				tm+=1.0*(cur)/(v[i].w+r);
				t-=1.0*cur/(v[i].w+r);
				if (v[i].r-v[i].l>1.0*t*(v[i].w+r))
				{
					tm+=1.0*(v[i].r-v[i].l-cur)/(v[i].w+s);
				}
			}
			else
			{
				for(int j=i;j<v.size();j++)
					tm+=1.0*(v[j].r-v[j].l)/(v[j].w+s);
				break;
			}
		}
		printf("%.7lf\n",tm);
	}
	return 0;
}