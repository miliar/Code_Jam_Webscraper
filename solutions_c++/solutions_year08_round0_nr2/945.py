#include <stdio.h>
#include <map>
#include <set>

using namespace std;

char s[100];

int ti(char * x)
{
	int h,m;
	sscanf(x,"%d:%d",&h,&m);
	return h*60+m;
}

int main()
{
	int j,n,t,a,b,i,p,q1,q2,r;
	map<int,map<int,int> > aa;
	map<int,map<int,int> > bb;
	map<int,map<int,int> >::iterator x,y;
	scanf("%d",&n);
	for (j=0;j<n;++j)
	{
		aa.clear();
		bb.clear();
		scanf("%d",&t);
		scanf("%d %d",&a,&b);
		for (i=0;i<a;++i)
		{
			scanf("%s",s);
			p=ti(s);
			scanf("%s",s);
			aa[p][ti(s)]++;
		}
		for (i=0;i<b;++i)
		{
			scanf("%s",s);
			p=ti(s);
			scanf("%s",s);
			bb[p][ti(s)]++;
		}
		q1=q2=0;
		while (aa.size() || bb.size())
		{
			x=aa.lower_bound(0);
			y=bb.lower_bound(0);
			if (x==aa.end() || (y!=bb.end() && y->first<x->first))
			{
				x=y;
				r=1;
				++q2;
			} else
			{
				r=0;
				++q1;
			}
			while (1)
			{
				i=x->second.begin()->first;
				x->second.begin()->second=x->second.begin()->second-1;
				if (x->second.begin()->second==0)
				{
					x->second.erase(x->second.begin());
				}
				if (x->second.size()==0)
				{
					if (r==0) aa.erase(x->first); else bb.erase(x->first);
				}
				i+=t;
				if (r==0)
				{
					x=bb.lower_bound(i);
					if (x==bb.end()) break;
				} else
				{
					x=aa.lower_bound(i);
					if (x==aa.end()) break;
				}
				r=1-r;
			}
		}
		printf("Case #%d: %d %d\n",j+1,q1,q2);
	}
	return 0;
}
