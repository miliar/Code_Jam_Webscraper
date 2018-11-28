#include <stdio.h>

#include <map>

using namespace std;

int main()
{
	int ic,nc,x,s,r,t,n,b,e,w,i,p;
	double ne,tot;
	map<int,int> xx;
	scanf("%d",&nc);
	for (ic=1;ic<=nc;++ic)
	{
		p=0;
		xx.clear();
		scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
		for (i=0;i<n;++i)
		{
			scanf("%d %d %d",&b,&e,&w);
			xx[s]+=b-p;
			xx[w+s]+=e-b;
			p=e;
		}
		xx[s]+=x-p;
		tot=0.0;
		for (map<int,int>::iterator it=xx.begin();it!=xx.end();++it)
		{
			ne=it->second/(double)(it->first+r-s);
			if (tot<t && ne+tot>t)
			{
				ne=(t-tot)*(it->first+r-s);
				tot=t;
				tot+=(it->second-ne)/(double)it->first;
			} else
			{
				if (tot<t) tot+=ne;	else tot+=it->second/(double)(it->first);
			}
		}
		printf("Case #%d: %.8lf\n",ic,tot);
	}
	return 0;
}
